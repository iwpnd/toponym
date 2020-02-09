import json
import os

import pytest

from toponym import settings
from toponym.recipes import Recipes
from toponym.utils import LanguageNotFoundError


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


def test_recipes_load_success_russian():
    """test load
    """

    recipes_russian = Recipes("russian")
    recipes_russian.load()

    assert recipes_russian.is_loaded


def test_recipes_load_success_croatian():
    """test load
    """

    recipes_croatian = Recipes("croatian")
    recipes_croatian.load()

    assert recipes_croatian.is_loaded


def test_recipes_load_success_ukrainian():
    """test load
    """

    recipes_ukrainian = Recipes("ukrainian")
    recipes_ukrainian.load()

    assert recipes_ukrainian.is_loaded


def test_recipes_load_success_romanian():
    """test load
    """

    recipes_romanian = Recipes("romanian")
    recipes_romanian.load()

    assert recipes_romanian.is_loaded


def test_recipes_load_success_latvian():
    """test load
    """

    recipes_latvian = Recipes("latvian")
    recipes_latvian.load()

    assert recipes_latvian.is_loaded


def test_recipes_load_success_hungarian():
    """test load
    """

    recipes_hungarian = Recipes("hungarian")
    recipes_hungarian.load()

    assert recipes_hungarian.is_loaded


def test_recipes_load_success_greek():
    """test load
    """

    recipes_greek = Recipes("greek")
    recipes_greek.load()

    assert recipes_greek.is_loaded


def test_recipes_load_failed_language_not_supported():
    """test load
    """

    with pytest.raises(LanguageNotFoundError):
        recipes_german = Recipes("german")
        recipes_german.load()


def test_recipes_load_with_input_dictionary():

    recipe = {
        "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
        "i": {"nominative": ["", 0], "genitive": ["o", 1]},
    }

    recipes_test = Recipes(language="test", file=recipe)
    recipes_test.load()

    assert recipes_test._dict


@pytest.mark.parametrize(
    "language, file, expectation",
    [
        ["test", 123, pytest.raises(TypeError)],
        ["test", "test", pytest.raises(FileNotFoundError)],
        ["test", [1, 2, 3], pytest.raises(TypeError)],
    ],
)
def test_recipes_load_with_input_filepath_fails(language, file, expectation):
    with expectation:
        recipes = Recipes(language=language, file=file)
        recipes.load()


def test_recipes_load_file():
    recipes_test = Recipes(language="test", file="./toponym/resources/_test.json")
    recipes_test.load()

    assert recipes_test.is_loaded


def test_recipes_consistency():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

    def is_consistent_recipes(filepath):
        with open(filepath, "r", encoding="utf8") as f:
            recipes_check = json.loads(f.read())

        recipes_consistent = list()

        for word_ending in recipes_check:
            for case in recipes_check[word_ending]:
                if isinstance(recipes_check[word_ending][case][0], list):
                    recipes_consistent.append(True)
                else:
                    print(filepath, word_ending)
                    recipes_consistent.append(False)

        if all([x for x in recipes_consistent]):
            return True
        else:
            return False

    assert all([is_consistent_recipes(recipes) for recipes in filepaths])


def test_recipes_valid_json():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

    for filepath in filepaths:
        with open(filepath, "r", encoding="utf8") as f:
            assert is_json(f.read())


def test_recipes_default_in_json():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

    for filepath in filepaths:
        with open(filepath, "r", encoding="utf8") as f:
            recipes_check = json.loads(f.read())
            assert isinstance(recipes_check, dict)
            assert "_default" in recipes_check
