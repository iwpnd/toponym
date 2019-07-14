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
                self._get_biggest_word_ending()
            ]

            self.topo = dict()
            for case in self.recipe:

                self.topo[case] = self._constructor(
                    self.word,
                    self.recipe,
                    case
                )

    def _get_biggest_word_ending(self):
        deepest_word_ending = ""
        reversed_text = "".join([x for x in reversed(self.word)])

        if reversed_text[0] in self.topodict._dict.keys():
            deepest_word_ending = deepest_word_ending + reversed_text[0]

        x = True
        while x == True:
                for x in reversed_text[1:]:
                    if deepest_word_ending in self.topodict._dict.keys():
                        if x + deepest_word_ending in self.topodict._dict.keys():
                            deepest_word_ending = x + deepest_word_ending
                        else:
                            break
                    else:
                        break

        return deepest_word_ending
