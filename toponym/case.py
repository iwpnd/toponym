from pydantic import BaseModel
from pydantic import conint
from pydantic import StrictStr


class DeclineConfig(BaseModel):
    """A configuration to handle declinsion

    Attributes:
        input_word: Input word
        recipe: topodictionary recipe by grammatical_case
    """

    input_word: StrictStr
    case: StrictStr
    recipe: list


class CaseConfig(BaseModel):
    """A configuration for a case

    Attributes:
        input_word: Input word/words
        new_word_ending: word ending or multiple
        cut_ending_by: amount of characters cut from input_word before new_word_ending is added
    """

    input_word: StrictStr
    cut_ending_by: conint(strict=True, ge=0)
    new_word_ending: StrictStr = None


class Case(object):
    """ grammatical case up for declinsion

    Attributes:
        decline_config: DeclineConfig object
        name: name of grammatical case
    """

    def __init__(self, decline_config: DeclineConfig):
        self.decline_config = decline_config
        self.name = decline_config.case

    def decline(self) -> list:
        """Declines a word based on configuration in decline_config

        Returns:
            output_words: list of words after declinsion
        """

        case_config = get_case_config(decline_config=self.decline_config)
        output_words = []

        if len(self.decline_config.recipe[0]) == 1:
            case_config.new_word_ending = self.decline_config.recipe[0][0]
            output_word = decline_input_word(config=case_config)
            output_words.append(output_word)

        elif len(self.decline_config.recipe[0]) > 1:

            for new_word_ending in self.decline_config.recipe[0]:
                case_config.new_word_ending = new_word_ending
                output_word = decline_input_word(config=case_config)
                output_words.append(output_word)

        return output_words


def get_case_config(decline_config: DeclineConfig) -> CaseConfig:
    """ Get a CaseConfig object from a DeclineConfig object

    Attributes:
        decline_config: DeclineConfig object

    Returns:
        case_config: CaseConfig
    """
    case_config = CaseConfig(
        cut_ending_by=decline_config.recipe[1], input_word=decline_config.input_word
    )

    return case_config


def decline_input_word(config: CaseConfig) -> str:
    """ Use config to construct a word after declinsion

    Attributes:
        config: CaseConfig

    Returns:
        output_word (str): a new word after declinsion
    """
    if config.cut_ending_by != 0:
        output_word = (
            config.input_word[: -config.cut_ending_by] + config.new_word_ending
        )
    else:
        output_word = config.input_word + config.new_word_ending

    return output_word
