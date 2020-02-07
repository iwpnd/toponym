from toponym.case import build_case_from_string
from toponym.case import build_cases_from_list
from toponym.case import Case
from toponym.case import CaseConfig

default_recipe = {
    "nominative": [[""], 0],
    "genitive": [[""], 0],
    "accusative": [[""], 0],
    "vocative": [[""], 0],
}


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


def test_case_decline_multiple_words_multiple_endings():
    decline_config = CaseConfig()
    decline_config.input_word = ["Test", "Kest"]
    decline_config.recipe = [["i", "o"], 1]

    test_case = Case()
    list_of_output_words = test_case.decline(decline_config)

    assert all(
        [
            output_words in list_of_output_words
            for output_words in [["Tesi", "Teso"], ["Kesi", "Keso"]]
        ]
    )


def test_case_build_from_list(case_config):
    case_config.input_word = ["Test", "Kest"]
    case_config.new_word_ending = ["i", "o"]
    case_config.cut_ending_by = 1

    list_of_output_words = build_cases_from_list(config=case_config)

    assert all(
        [
            output_words in list_of_output_words
            for output_words in [["Tesi", "Teso"], ["Kesi", "Keso"]]
        ]
    )
