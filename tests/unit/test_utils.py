import os
from os import path
from typing import Generator

import pytest

from toponym import settings
from toponym.utils import file_exists
from toponym.utils import get_available_language_codes
from toponym.utils import get_language_code
from toponym.utils import get_recipes
from toponym.utils import get_recipes_from_dict
from toponym.utils import get_recipes_from_file
from toponym.utils import LanguageNotFoundError
from toponym.utils import lazy_load_csv


def test_get_available_languages():
    """get available languages as ISO 639-1
    """

    languages = get_available_language_codes()
    assert languages
    assert isinstance(languages, list)


def test_get_language_code_success():
    language_code = get_language_code("russian")
    assert language_code
    assert language_code == "ru"


def test_get_language_code_fails():
    with pytest.raises(LanguageNotFoundError):
        language_code = get_language_code("kaudawelsh")


def test_topodict_dir():
    list_dir = os.listdir(settings.RECIPES_DIR)

    assert "hr.json" in list_dir
    assert "ru.json" in list_dir


def test_parent_directory():
    list_dir = os.listdir(settings.PARENT_DIRECTORY)

    assert all(
        [
            file in list_dir
            for file in [
                "toponym.py",
                "resources",
                "__init__.py",
                "utils.py",
                "topodict.py",
                "settings.py",
                "case.py",
            ]
        ]
    )


def test_get_recipe_success():
    recipes_test = get_recipes("ru")

    assert isinstance(recipes_test, dict)


def test_get_recipe_fails():
    with pytest.raises(LanguageNotFoundError):
        recipes_test = get_recipes("de")


def test_get_recipes_from_dict():
    recipes_dict = {}

    recipes = get_recipes_from_dict(input_dict=recipes_dict)

    assert isinstance(recipes, dict)


def test_get_recipes_from_file():
    file = "./toponym/resources/_test.json"
    recipes = get_recipes_from_file(file_input=file)

    assert isinstance(recipes, dict)


def test_file_exists_true(monkeypatch):
    def mock_path_exists(filename: str):
        return True

    monkeypatch.setattr(path, "exists", mock_path_exists)

    assert file_exists("test.csv") is True


def test_file_exists_false(monkeypatch):
    def mock_path_exists(filename: str):
        return False

    monkeypatch.setattr(path, "exists", mock_path_exists)

    assert file_exists("test.csv") is False


def test_lazy_load(tmpdir):
    file = tmpdir.join("test.csv")

    assert lazy_load_csv(file)
    assert isinstance(lazy_load_csv(file), Generator)
