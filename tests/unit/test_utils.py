import os

import pytest

from toponym import settings
from toponym import utils


def test_get_available_languages():
    """get available languages as ISO 639-1
    """

    languages = utils.get_available_language_codes()
    assert languages


def test_get_language_code_success():
    language_code = utils.get_language_code("russian")
    assert language_code
    assert language_code == "ru"


def test_get_language_code_fails():
    with pytest.raises(KeyError):
        language_code = utils.get_language_code("kaudawelsh")
        assert language_code


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
