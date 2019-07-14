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
            for w in self.word:
                self.recipe = self.topodict[
                    self._get_longest_word_ending(w)
                ]

                self.topo = dict()

                for case in self.recipe:
                    self.topo[case] = self._constructor(
                        w,
                        self.recipe,
                        case
                    )
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
        matching_endings = [x for x in possible_endings if x in self.topodict._dict.keys()]

        return max(matching_endings, key=len)
