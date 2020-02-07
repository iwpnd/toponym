from typing import Union


class DeclineConfig:
    """A configuration to handle declinsion

    Attributes:
    input_word: Input word/words
    recipe: topodictionary recipe by grammatical_case
    """

    input_word = Union[list, str]
    recipe: dict


class CaseConfig(DeclineConfig):
    """A configuration for the case

    Attributes:
    input_word: Input word/words
    new_word_ending: word ending or multiple
    cut_ending_by: amount of characters cut from input_word before new_word_ending is added
    """

    new_word_ending: Union[list, str]
    cut_ending_by: int


class Case(object):
    def decline(self, decline_config: DeclineConfig) -> Union[list, str]:
        """Declines a word based on
        """

        case_config = CaseConfig()
        case_config.cut_ending_by = decline_config.recipe[1]

        if (
            isinstance(decline_config.input_word, str)
            and len(decline_config.recipe[0]) == 1
        ):
            case_config.input_word = decline_config.input_word
            case_config.new_word_ending = decline_config.recipe[0][0]

            output_word = build_case_from_string(config=case_config)
            return [output_word]

        elif (
            isinstance(decline_config.input_word, str)
            and len(decline_config.recipe[0]) > 1
        ):
            case_config.input_word = decline_config.input_word

            output_words = []

            for new_word_ending in decline_config.recipe[0]:
                case_config.new_word_ending = new_word_ending
                output_word = build_case_from_string(config=case_config)
                output_words.append(output_word)

            return output_words

        elif (
            isinstance(decline_config.input_word, list)
            and len(decline_config.recipe[0]) > 1
        ):

            case_config.input_word = decline_config.input_word
            case_config.new_word_ending = decline_config.recipe[0]

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
