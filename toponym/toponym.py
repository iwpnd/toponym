from toponym import case


class Toponym(case.Case):

    def __init__(self, input_term, topodict):

        self.word = input_term
        self.topodict = topodict

        if len(input_term.split()) > 1:
            self.word = input_term.split()

        self.topo_recipe = False

    def build(self):

        if isinstance(self.word, list):
            for _ in self.word:
                break

        else:
            self.recipe = self.topodict[
                self._get_longest_word_ending()
            ]

            self.topo = dict()
            for case in self.recipe:

                self.topo[case] = self._constructor(
                    self.word,
                    self.recipe,
                    case
                )

    def _get_longest_word_ending(self):
        """
        """
        possible_endings = [self.word[i:] for i in range(len(self.word))]
        matching_endings = [x for x in possible_endings if x in self.topodict._dict.keys()]

        return max(matching_endings, key=len)
