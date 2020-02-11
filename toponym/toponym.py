import itertools
import logging
from collections import defaultdict

from toponym.case import Case
from toponym.case import DeclineConfig
from toponym.recipes import Recipes

logger = logging.getLogger(__name__)


class Toponym(Case):
    def __init__(self, input_word: str, recipes: Recipes) -> None:

        self.input_word = input_word
        self.recipes = recipes
        self.input_is_multiple_words = len(input_word.split()) > 1

        if self.input_is_multiple_words:
            self.input_words = input_word.split()

    def build(self) -> None:
        decline_config = DeclineConfig()

        if self.input_is_multiple_words:

            self.topo = list()

            for _, input_word in enumerate(self.input_words):
                self.recipe = get_recipe_for_input_word(
                    input_word=input_word, recipes=self.recipes
                )
                decline_config.input_word = input_word

                temp = dict()

                for grammatical_case in self.recipe:
                    decline_config.recipe = self.recipe[grammatical_case]

                    temp[grammatical_case] = self.decline(decline_config)

                self.topo.append(temp)

            self.topo = self._concat_case_dictionaries(self.topo)

        else:
            self.recipe = self.recipe = get_recipe_for_input_word(
                input_word=self.input_word, recipes=self.recipes
            )
            self.topo = dict()

            decline_config.input_word = self.input_word

            for grammatical_case in self.recipe:
                decline_config.recipe = self.recipe[grammatical_case]
                self.topo[grammatical_case] = self.decline(decline_config)

    def list_toponyms(self) -> list:
        """ Put all created toponyms in a list
        """

        if self.topo:
            all_toponyms_all_cases = list(map(self.topo.__getitem__, self.topo.keys()))
            return list(set(itertools.chain.from_iterable(all_toponyms_all_cases)))

        else:
            raise Exception(".build() first")

    def _concat_case_dictionaries(self, list_of_dictionaries: list) -> dict:
        """ Concate list of dictionaries
        """
        dd = defaultdict(list)

        for dictionary in list_of_dictionaries:
            for key, value in dictionary.items():
                dd[key].append(value)

        for key, value in dd.items():

            if all([isinstance(x, str) for x in value]):
                dd[key] = " ".join([x for x in dd[key]])

            elif any([isinstance(x, list) for x in value]):
                value = [
                    [element] if not isinstance(element, list) else element
                    for element in value
                ]
                product = list(itertools.product(*value))
                permutation = [" ".join([y for y in x]) for x in product]
                dd[key] = permutation

        return dd


def get_recipe_for_input_word(input_word: str, recipes: Recipes) -> dict:
    recipe = recipes[get_longest_word_ending(input_word=input_word, recipes=recipes)]
    return recipe


def get_longest_word_ending(input_word: str, recipes: Recipes) -> str:
    """Disect word into differnet size shifs
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
