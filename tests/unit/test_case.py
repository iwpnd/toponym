from toponym.case import build_case_from_string
from toponym.case import Case

default_recipe = {
    "nominative": [[""], 0],
    "genitive": [[""], 0],
    "accusative": [[""], 0],
    "vocative": [[""], 0],
}


def test_case_constructor_config():
    constructor_config = {"input_word": "Test", "recipe": default_recipe["nominative"]}

    test_case = Case()
    test_case._constructor(constructor_config)


def test_case_build_from_string_single_ending_success(case_config):
    case_config.input_word = "Test"
    case_config.new_word_ending = "i"
    case_config.cut_ending_by = 1

    output_word = build_case_from_string(case_config)

    assert output_word == "Tesi"


def test_case_build_from_string_multiple_ending_success():
    constructor_config = {"input_word": "Test", "recipe": [["i", "o"], 1]}

    test_case = Case()
    output_words = test_case._constructor(constructor_config)

    assert "Tesi" in output_words
    assert "Teso" in output_words
