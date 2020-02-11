import itertools
from collections import defaultdict
from typing import Generator

from loguru import logger

from toponym.case import Case
from toponym.case import DeclineConfig
from toponym.recipes import Recipes


class Toponym:
    def __init__(self, input_word: str, recipes: Recipes) -> None:

        self.input_word = input_word
        self.recipes = recipes
        self.input_is_multiple_words = len(input_word.split()) > 1

        if self.input_is_multiple_words:
            self.input_words = input_word.split()

    def build(self) -> None:
        decline_config = DeclineConfig()

        if self.input_is_multiple_words:
            self.merged_toponym_dictionaries = merge_list_of_case_dictionaries(
                self._build_toponym_for_multiple_input_words(
                    decline_config=decline_config
                )
            )
            print(self.merged_toponym_dictionaries)

            self.toponyms = concat_case_dictionaries(self.merged_toponym_dictionaries)

        else:
            self.toponyms = self._build_toponym_for_input_word(
                decline_config=decline_config
            )

    def _build_toponym_for_input_word(self, decline_config: DeclineConfig) -> dict:
        """ builds a toponym from a single input_word
        """

        recipe = get_recipe_for_input_word(
            input_word=self.input_word, recipes=self.recipes
        )
        toponyms = dict()

        decline_config.input_word = self.input_word

        for grammatical_case in recipe:
            decline_config.recipe = recipe[grammatical_case]
            toponyms[grammatical_case] = Case.decline(decline_config=decline_config)

        return toponyms

    def _build_toponym_for_multiple_input_words(
        self, decline_config: DeclineConfig
    ) -> Generator:
        """builds toponyms if self.input_is_multiple_words == True

        Since there is more than one word, there should be a toponym for
        every input word present.
        """

        for _, input_word in enumerate(self.input_words):
            recipe = get_recipe_for_input_word(
                input_word=input_word, recipes=self.recipes
            )
            decline_config.input_word = input_word

            temp = dict()

            for grammatical_case in recipe:
                decline_config.recipe = recipe[grammatical_case]
                temp[grammatical_case] = Case.decline(decline_config=decline_config)

            yield temp

    def list_toponyms(self) -> list:
        """ Put all created toponyms in a list
        """

        if self.toponyms:
            all_toponyms_all_cases = list(
                map(self.toponyms.__getitem__, self.toponyms.keys())
            )
            return list(set(itertools.chain.from_iterable(all_toponyms_all_cases)))

        else:
            raise Exception(".build() first")


def merge_list_of_case_dictionaries(list_of_case_dictionaries: Generator) -> dict:
    """Take a generator of case dictionaries and hash them into a
    defaultdict.

    If the input_word is a combination of two words, the input_word is split()
    and _build_toponym_for_multiple_input_words() is used to build the toponym.
    In the process it is possible that one of the input words has more than one
    possible new_word_ending, so the possible toponyms are appended as list.

    returns

    Example:

    {
        'nominative': [['Beograq'], ['Begraf']],
        'genitive': [['Beograq'], ['Begrafa']],
        'dative': [['Beograq'], ['Begrafu']],
        'accusative': [['Beograq'], ['Begrafa']],
        'locative': [['Beograq'], ['Begrafu']],
        'instrumental': [['Beograq'], ['Begrafem', 'Begrafom']]
        }
    """

    merged_toponym_dictionaries = defaultdict(list)

    for case_dictionary in list_of_case_dictionaries:
        for case, toponym_word in case_dictionary.items():
            merged_toponym_dictionaries[case].append(toponym_word)

    return merged_toponym_dictionaries


def concat_case_dictionaries(merged_toponym_dictionaries: defaultdict) -> dict:
    """ Take a defaultdict and create products from the dicts values.

    In case there are multiple input_words and one of them has multiple possible
    new endings, we have to create products of those.

    returns
    Example:

    {
        'nominative': ['Beograq Begraf'],
        'genitive': ['Beograq Begrafa'],
        'dative': ['Beograq Begrafu'],
        'accusative': ['Beograq Begrafa'],
        'locative': ['Beograq Begrafu'],
        'instrumental': ['Beograq Begrafem', 'Beograq Begrafom']
        }
    """

    for case, toponym_word in merged_toponym_dictionaries.items():

        product = itertools.product(*toponym_word)
        permutation = [" ".join([y for y in x]) for x in product]
        merged_toponym_dictionaries[case] = permutation

    return merged_toponym_dictionaries


def get_recipe_for_input_word(input_word: str, recipes: Recipes) -> dict:
    """Get a recipe from a list of recipes based on the longest matching
    character sequence found in the input_word that is also in Recipes.keys()

    returns recipe

    {
        'nominative': [[''], 0],
        'genitive': [['e'], 1],
        'dative': [['i'], 1],
        'accusative': [['u'], 1],
        'locative': [['i'], 1],
        'instrumental': [['om'], 1]
        }
    """
    recipe = recipes[get_longest_word_ending(input_word=input_word, recipes=recipes)]
    return recipe


def get_longest_word_ending(input_word: str, recipes: Recipes) -> str:
    """Disect word into differnet size shifs and return the longest shif that
    is also within recipes.keys()

    returns str

    Example:

    recipes = {
        "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
        "i": {"nominative": [[""], 0], "genitive": [["o"], 1]},
        "o": {"nominative": [[""], 0], "genitive": [["a"], 1]},
        "ti": {"nominative": [[""], 0], "genitive": [["o"], 1]},
        "esti": {"nominative": [[""], 0], "genitive": [["o", "a"], 1]},
    }

    input_word = "Testi"
    >> "esti"
    """

    matching_endings = [
        input_word[i:]
        for i in range(len(input_word))
        if input_word[i:] in recipes._dict.keys()
    ]

    if matching_endings:
        return max(matching_endings, key=len)
    else:
        logger.debug("No word ending found for: {word}".format(word=input_word))
        return ""
