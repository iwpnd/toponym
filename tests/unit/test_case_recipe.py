import json
import os

import pytest

from toponym import settings
from toponym.recipes import Recipes
from toponym.utils import is_consistent_recipes
from toponym.utils import is_json
from toponym.utils import LanguageNotFoundError


@pytest.mark.parametrize("language", settings.LANGUAGE_DICT.keys())
def test_load_recipes_from_languages(language):
    recipes = Recipes()
    recipes.load_from_language(language=language)

    assert recipes._dict


def test_recipes_load_failed_language_not_supported():
    """test load
    """

    with pytest.raises(LanguageNotFoundError):
        recipes_fails = Recipes()
        recipes_fails.load_from_language(language="funkytown")


def test_recipes_load_with_input_dictionary():

    recipe = {
        "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
        "i": {"nominative": [[""], 0], "genitive": [["o"], 1]},
    }

    recipes_test = Recipes()
    recipes_test.load_from_dict(input_dict=recipe, language="test")

    assert recipes_test._dict


@pytest.mark.parametrize(
    "input_dict, expectation",
    [
        [1, pytest.raises(TypeError)],
        [[1, 2, 3], pytest.raises(TypeError)],
        ["test", pytest.raises(TypeError)],
    ],
)
def test_recipes_load_with_input_dictionary_fails(input_dict, expectation):

    with expectation:
        recipes_test = Recipes()
        recipes_test.load_from_dict(language="bla", input_dict=input_dict)


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
        recipes = Recipes()
        recipes.load_from_file(language=language, filepath=file)


def test_recipes_load_file():
    recipes_test = Recipes()
    recipes_test.load_from_file(
        language="test", filepath="./toponym/resources/_test.json"
    )

    assert recipes_test.is_loaded


def test_recipes_consistency():
    list_dir = os.listdir(settings.PARENT_DIRECTORY + "/resources")
    filepaths = [
        settings.PARENT_DIRECTORY + "/resources" + "/{}".format(x)
        for x in list_dir
        if x.endswith(".json")
    ]

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
