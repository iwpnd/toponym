from toponym.case import Case
from toponym.case import CaseConfig
from toponym.case import decline_input_word
from toponym.case import get_case_config


def test_case_decline_config(decline_config_test_case):

    test_case = Case()
    output = test_case.decline(decline_config_test_case)

    assert output


def test_case_build_from_string_multiple_ending_success(decline_config_test_case):

    test_case = Case()
    output_words = test_case.decline(decline_config_test_case)

    assert "Tesi" in output_words
    assert "Teso" in output_words


def test_get_case_config(decline_config_test_case):

    case_config = get_case_config(decline_config=decline_config_test_case)

    assert isinstance(case_config, CaseConfig)


def test_case_build_from_string_single_ending_success():
    case_config = CaseConfig(input_word="Test", new_word_ending="i", cut_ending_by=1)
    output_word = decline_input_word(case_config)

    assert output_word == "Tesi"
