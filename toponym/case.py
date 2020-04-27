from typing import Union

from pydantic import BaseModel
from pydantic import conint
from pydantic import StrictStr


class DeclineConfig(BaseModel):
    """A configuration to handle declinsion

    Attributes:
    input_word: Input word/words
    recipe: topodictionary recipe by grammatical_case
    """

    input_word: StrictStr
    recipe: list


class CaseConfig(BaseModel):
    """A configuration for the case

    Attributes:
    input_word: Input word/words
    new_word_ending: word ending or multiple
    cut_ending_by: amount of characters cut from input_word before new_word_ending is added
    """

    input_word: StrictStr
    cut_ending_by: conint(strict=True, ge=0)
    new_word_ending: StrictStr = None


class Case(object):
    """
    """

    @staticmethod
    def decline(decline_config: DeclineConfig) -> Union[list, str]:
        """Declines a word based on
        """

        case_config = get_case_config(decline_config=decline_config)
        output_words = []

        if len(decline_config.recipe[0]) == 1:
            case_config.new_word_ending = decline_config.recipe[0][0]
            output_word = decline_input_word(config=case_config)
            output_words.append(output_word)

        elif len(decline_config.recipe[0]) > 1:

            for new_word_ending in decline_config.recipe[0]:
                case_config.new_word_ending = new_word_ending
                output_word = decline_input_word(config=case_config)
                output_words.append(output_word)

        return output_words


def get_case_config(decline_config: DeclineConfig) -> CaseConfig:
    case_config = CaseConfig(
        cut_ending_by=decline_config.recipe[1], input_word=decline_config.input_word
    )

    return case_config


def decline_input_word(config: CaseConfig) -> str:
    if config.cut_ending_by != 0:
        output_word: str = (
            config.input_word[: -config.cut_ending_by] + config.new_word_ending
        )
    else:
        output_word: str = config.input_word + config.new_word_ending

    return output_word
