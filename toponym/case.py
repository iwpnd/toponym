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
    def _constructor(self, config: dict) -> Union[list, str]:
        """Depending on the recipe and input, execute build_case accordingly
        """

        case_config = CaseConfig()
        case_config.cut_ending_by = config["recipe"][1]

        if isinstance(config["input_word"], str) and len(config["recipe"][0]) == 1:
            case_config.input_word = config["input_word"]
            case_config.new_word_ending = config["recipe"][0][0]

            output_word = build_case_from_string(config=case_config)
            return output_word

        if isinstance(config["input_word"], str) and len(config["recipe"][0]) > 1:
            case_config.input_word = config["input_word"]

            output_words = []

            for new_word_ending in config["recipe"][0]:
                case_config.new_word_ending = new_word_ending
                output_word = build_case_from_string(config=case_config)
                output_words.append(output_word)

            return output_words

        elif isinstance(config["input_word"], list) and len(config["recipe"][0]) > 1:

            case_config.input_word = config["input_word"]
            case_config.new_word_ending = config["recipe"][0]

            list_of_output_words = build_cases_from_list(case_config)

            return list_of_output_words


def build_cases_from_list(config: CaseConfig) -> str:
    list_of_output_words = []

    for input_word in config.input_word:
        output_words = []
        for ending in config.new_word_ending:
            if config.cut_ending_by != 0:
                output_word = input_word[: -config.cut_ending_by] + ending
                output_words.append(output_word)
            else:
                output_word = input_word + ending
                output_words.append(output_word)

        list_of_output_words.append(output_words)

    return list_of_output_words


def build_case_from_string(config: CaseConfig) -> str:
    if config.cut_ending_by != 0:
        output_word = (
            config.input_word[: -config.cut_ending_by] + config.new_word_ending
        )
    else:
        output_word = config.input_word + config.new_word_ending

    return output_word
