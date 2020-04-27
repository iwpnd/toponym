import pytest

from toponym.case import DeclineConfig
from toponym.recipes import Recipes


@pytest.fixture
def decline_config_test_case():
    decline_config = DeclineConfig(
        input_word="Test", case="genitive", recipe=[["i", "o"], 1]
    )

    return decline_config


@pytest.fixture
def test_recipes():
    recipes = {
        "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
        "i": {"nominative": [[""], 0], "genitive": [["o"], 1]},
        "o": {"nominative": [[""], 0], "genitive": [["a"], 1]},
        "ti": {"nominative": [[""], 0], "genitive": [["o"], 1]},
        "esti": {"nominative": [[""], 0], "genitive": [["o", "a"], 1]},
    }
    recipes_test = Recipes(language="test", file=recipes)
    recipes_test.load()

    yield recipes_test
