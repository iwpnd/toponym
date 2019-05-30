class Case(object):
    def __init__(self):
        pass

    def _build_case(self, word, ending, cutending=0):
        is_str = isinstance(ending, str)
        is_list = isinstance(ending, list)

        if not (is_str or is_list):
            raise TypeError(
                type(ending),
                '- is not supported. Either provide str or list of str'
            )

        if is_str:
            if cutending is not 0:
                tmpWord = word[:-cutending] + ending
            else:
                tmpWord = word + ending
            return tmpWord

        if is_list:
            tmpWordList = list()

            for end in ending:
                if cutending is not 0:
                    tmpWord = word[:-cutending] + end
                    tmpWordList.append(tmpWord)
                else:
                    tmpWord = word + end
                    tmpWordList.append(tmpWord)
            return tmpWordList

    def _constructor(self, word, topo_recipe, case):

        word = self._build_case(
            word,
            ending=topo_recipe[case][0],
            cutending=topo_recipe[case][1]
        )

        return word
