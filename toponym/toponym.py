import itertools
import logging
from collections import defaultdict

from toponym import case
from toponym.topodict import Topodict

logger = logging.getLogger(__name__)


class Toponym(case.Case):
    def __init__(self, input_term: str, topodict: Topodict) -> None:

        self.word = input_term
        self.topodict = topodict

        if len(input_term.split()) > 1:
            self.word = input_term.split()

        self.topo_recipe = False

    def build(self) -> None:

        if isinstance(self.word, list):

            self.topo = list()

            for _, w in enumerate(self.word):
                self.recipe = self.topodict[self._get_longest_word_ending(w)]

                temp = dict()
                for grammatical_case in self.recipe:
                    temp[grammatical_case] = self._constructor(
                        w, self.recipe, grammatical_case
                    )

                self.topo.append(temp)

            self.topo = self._concat_case_dictionaries(self.topo)

        else:
            self.recipe = self.topodict[self._get_longest_word_ending(self.word)]

            self.topo = dict()

            for grammatical_case in self.recipe:
                self.topo[grammatical_case] = self._constructor(
                    self.word, self.recipe, grammatical_case
                )

    def list_toponyms(self) -> list:
        """ Put all created toponyms in a list
        """

        if self.topo:
            all_toponyms_all_cases = list(map(self.topo.__getitem__, self.topo.keys()))
            return list(set(itertools.chain.from_iterable(all_toponyms_all_cases)))

        else:
            raise Exception(".build() first")

    def _get_longest_word_ending(self, word: str) -> str:
        """Disect word into differnet size shifs
        """
        # TODO: write TIL about max(list, key=len)
        possible_endings = [word[i:] for i in range(len(word))]
        matching_endings = [
            x for x in possible_endings if x in self.topodict._dict.keys()
        ]

        if matching_endings:
            return max(matching_endings, key=len)
        else:
            logger.debug("No word ending found for: {word}".format(word=word))
            return ""

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
