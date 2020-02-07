from toponym.case import Case

default_recipe = {
    "nominative": [[""], 0],
    "genitive": [[""], 0],
    "accusative": [[""], 0],
    "vocative": [[""], 0],
}


def test_case_build_case_config():
    config = {"input_word": "Test", "new_word_ending": "i", "cut_ending_by": 1}

    test_case = Case()
    test_case._build_case(config)


def test_case_constructor_config():
    config = {"input_word": "Test", "recipe": default_recipe["nominative"]}

    test_case = Case()
    test_case._constructor(config)
