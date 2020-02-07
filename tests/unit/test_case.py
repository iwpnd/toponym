from toponym.case import Case


def test_case_config():
    config = {"input_word": "Test", "new_word_ending": "i", "cut_ending_by": 1}

    test_case = Case()
    test_case._build_case(config)
