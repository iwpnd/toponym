from toponym.case import build_case_from_string
from toponym.case import Case


def test_case_decline_config(decline_config):
    decline_config.input_word = "Test"
    decline_config.recipe = [["i", "o"], 1]

    test_case = Case()
    output = test_case.decline(decline_config)

    assert output


def test_case_build_from_string_single_ending_success(case_config):
    case_config.input_word = "Test"
    case_config.new_word_ending = "i"
    case_config.cut_ending_by = 1

    output_word = build_case_from_string(case_config)

    assert output_word == "Tesi"


def test_case_build_from_string_multiple_ending_success(decline_config):
    decline_config.input_word = "Test"
    decline_config.recipe = [["i", "o"], 1]

    test_case = Case()
    output_words = test_case.decline(decline_config)

    assert "Tesi" in output_words
    assert "Teso" in output_words
