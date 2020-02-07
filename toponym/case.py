from typing import Union


class Case(object):
    def __init__(self):
        pass

    def _build_case(self, config: dict) -> Union[list, str]:
        """ Modify a word given an ending and a cutending parameter
        """

        is_str = isinstance(config["input_word"], str)
        is_list = isinstance(config["input_word"], list)

        if not (is_str or is_list):
            raise TypeError(
                type(config["input_word"]),
                "- is not supported. Either provide str or list of str",
            )

        if is_str:
            if config["cut_ending_by"] != 0:
                output_word = (
                    config["input_word"][: -config["cut_ending_by"]]
                    + config["new_word_ending"]
                )
            else:
                output_word = config["input_word"] + config["new_word_ending"]
            return output_word

        if is_list:
            output_words = list()

            for ending in config["new_word_ending"]:
                if config["cut_ending_by"] != 0:
                    output_word = (
                        config["input_word"][: -config["cut_ending_by"]] + ending
                    )
                    output_words.append(output_word)
                else:
                    output_word = config["input_word"] + ending
                    output_words.append(output_word)
            return output_words

    def _constructor(
        self, word: str, topo_recipe: dict, grammatical_case: str
    ) -> Union[list, str]:
        """Depending on the recipe and input, execute build_case accordingly
        """
        if isinstance(word, str):
            word = self._build_case(
                word,
                ending=topo_recipe[grammatical_case][0],
                cutending=topo_recipe[grammatical_case][1],
            )
            return word

        elif isinstance(word, list) and len(topo_recipe[grammatical_case][0]) == 1:
            words = []
            for w in word:
                word = self._build_case(
                    w,
                    ending=topo_recipe[grammatical_case][0],
                    cutending=topo_recipe[grammatical_case][1],
                )
                words.append(word)

                return words

        elif isinstance(word, list) and len(topo_recipe[grammatical_case][0]) > 1:
            words = []
            for ending in topo_recipe[grammatical_case][0]:
                for w in word:

                    word = self._build_case(
                        w, ending=ending, cutending=topo_recipe[grammatical_case][1]
                    )
                    words.append(word)

                return words
