import pytest
from pydantic import ValidationError

from toponym.case import Case
from toponym.case import CaseConfig
from toponym.case import decline_input_word
from toponym.case import DeclineConfig
from toponym.case import get_case_config


def test_case_decline_config(decline_config_test_case):

    test_case = Case(decline_config=decline_config_test_case)
    output = test_case.decline()

    assert output


@pytest.mark.parametrize(
    "input_word, recipe, case, expectation",
    [
        ["test", {"test": ["i", "o"]}, "genitive", pytest.raises(ValidationError)],
        [1, [["i", "o"], 1], "genitive", pytest.raises(ValidationError)],
        [[1, 1], [1, 2, 3], "genitive", pytest.raises(ValidationError)],
        ["test", [1, 2, 3], 1, pytest.raises(ValidationError)],
    ],
)
def test_case_decline_config_fails(input_word, case, recipe, expectation):
    with expectation:
        decline_config = DeclineConfig(input_word=input_word, recipe=recipe, case=case)


def test_case_build_from_string_multiple_ending_success(decline_config_test_case):

    test_case = Case(decline_config=decline_config_test_case)
    output_words = test_case.decline()

    assert test_case.name == decline_config_test_case.case
    assert "Tesi" in output_words
    assert "Teso" in output_words


def test_get_case_config(decline_config_test_case):

    case_config = get_case_config(decline_config=decline_config_test_case)

    assert isinstance(case_config, CaseConfig)


def test_case_build_from_string_single_ending_success():
    case_config = CaseConfig(input_word="Test", new_word_ending="i", cut_ending_by=1)
    output_word = decline_input_word(case_config)

    assert output_word == "Tesi"


def test_case_build_from_string_single_ending_success_zero():
    case_config = CaseConfig(input_word="Test", new_word_ending="i", cut_ending_by=0)
    output_word = decline_input_word(case_config)

    assert output_word == "Testi"


@pytest.mark.parametrize(
    "input_word, cut_ending_by, new_word_ending, expectation",
    [
        ["test", 1, 1, pytest.raises(ValidationError)],
        ["test", "1", "e", pytest.raises(ValidationError)],
        ["test", "1", "e", pytest.raises(ValidationError)],
        [1, 1, "e", pytest.raises(ValidationError)],
        ["test", -10, "e", pytest.raises(ValidationError)],
    ],
)
def test_case_caseconfig_fails(input_word, cut_ending_by, new_word_ending, expectation):
    with expectation:
        case_config = CaseConfig(
            input_word=input_word,
            cut_ending_by=cut_ending_by,
            new_word_ending=new_word_ending,
        )
