from toponym import case
from collections import defaultdict
import itertools


class Toponym(case.Case):

    def __init__(self, input_term, topodict):

        self.word = input_term
        self.topodict = topodict

        if len(input_term.split()) > 1:
            self.word = input_term.split()

        self.topo_recipe = False

    def build(self):

        if isinstance(self.word, list):

            self.topo = list()

            for _, w in enumerate(self.word):
                self.recipe = self.topodict[
                    self._get_longest_word_ending(w)
                ]

                temp = dict()
                for case in self.recipe:
                    temp[case] = self._constructor(w, self.recipe, case)

                self.topo.append(temp)
            
            self.topo = self.concat_case_dictionaries(self.topo)

        else:
            self.recipe = self.topodict[
                self._get_longest_word_ending(self.word)
            ]

            self.topo = dict()

            for case in self.recipe:
                self.topo[case] = self._constructor(
                    self.word,
                    self.recipe,
                    case
                )

    def _get_longest_word_ending(self, word):
        """
        """
        # TODO: write TIL about max(list, key=len)
        possible_endings = [word[i:] for i in range(len(word))]
        matching_endings = [
            x for x in possible_endings if x in self.topodict._dict.keys()]

        return max(matching_endings, key=len)


    def concat_case_dictionaries(self, list_of_dictionaries):
        """ Concate list of dictionaries
        """
        dd = defaultdict(list)

        for dictionary in list_of_dictionaries:
            for key, val in dictionary.items():
                dd[key].append(val)

        for k, v in dd.items():
            if isinstance(v[0], str):
                dd[k] = " ".join([x for x in dd[k]])
    
            if isinstance(v[0], list):
                prd = list(itertools.product(*v))
                perm = [" ".join([y for y in x]) for x in prd]
                dd[k] = perm

        return dd