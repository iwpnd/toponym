from typing import Union


class CaseConfig:
    """A configuration for the case

    Attributes:
    input_word: Input word/words
    new_word_ending: word ending or multiple
    cut_ending_by: amount of characters cut from input_word before new_word_ending is added
    """

    input_word: Union[list, str]
    new_word_ending: Union[list, str]
    cut_ending_by: int


class Case(object):
    def __init__(self):
        pass

    def _build_case(self, config: CaseConfig) -> Union[list, str]:
        """ Modify a word given an ending and a cutending parameter
        """

        is_str = isinstance(config.input_word, str)
        is_list = isinstance(config.input_word, list)

        if not (is_str or is_list):
            raise TypeError(
                type(config.input_word),
                "- is not supported. Either provide str or list of str",
            )

        if is_str:
            if config.cut_ending_by != 0:
                output_word = (
                    config.input_word[: -config.cut_ending_by] + config.new_word_ending
                )
            else:
                output_word = config.input_word + config.new_word_ending
            return output_word

        if is_list:
            output_words = list()

            for ending in config.new_word_ending:
                if config.cut_ending_by != 0:
                    output_word = config.input_word[: -config.cut_ending_by] + ending
                    output_words.append(output_word)
                else:
                    output_word = config.input_word + ending
                    output_words.append(output_word)
            return output_words

    def _constructor(self, config: dict) -> Union[list, str]:
        """Depending on the recipe and input, execute build_case accordingly
        """
        case_config = {
            "input_word": config["input_word"],
            "new_word_ending": config["recipe"][0],
            "cut_ending_by": config["recipe"][1],
        }

        case_config = CaseConfig()
        case_config.input_word = config["input_word"]
        case_config.new_word_ending = config["recipe"][0]
        case_config.cut_ending_by = config["recipe"][1]

        if isinstance(config["input_word"], list) and len(config["recipe"][0]) == 1:
            output_words = []
            for input_word in config["input_word"]:
                output_word = self._build_case(config=case_config)
                output_words.append(output_word)

                return output_words

        elif isinstance(config["input_word"], list) and len(config["recipe"][0]) > 1:
            output_words = []
            for word_ending in config["recipe"][0]:
                for input_word in config["input_word"]:

                    output_word = self._build_case(case_config)
                    output_words.append(output_word)

                return output_words


def build_case_from_string(config: CaseConfig) -> str:
    if config.cut_ending_by != 0:
        output_word = (
            config.input_word[: -config.cut_ending_by] + config.new_word_ending
        )
    else:
        output_word = config.input_word + config.new_word_ending

    return output_word
