from toponym.case import build_case_from_string
from toponym.case import Case

default_recipe = {
    "nominative": [[""], 0],
    "genitive": [[""], 0],
    "accusative": [[""], 0],
    "vocative": [[""], 0],
}


def test_case_build_case_config(case_config):
    test_case = Case()
    test_case._build_case(case_config)


def test_case_build_from_string_success(case_config):
    output_word = build_case_from_string(case_config)

    assert output_word


def test_case_constructor_config():
    config = {"input_word": "Test", "recipe": default_recipe["nominative"]}

    test_case = Case()
    test_case._constructor(config)
