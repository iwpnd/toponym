import pytest

from toponym.case import CaseConfig
from toponym.case import DeclineConfig
from toponym.recipes import Recipes


@pytest.fixture
def case_config():
    case_config = CaseConfig()

    yield case_config


@pytest.fixture
def decline_config():
    decline_config = DeclineConfig()

    yield decline_config


@pytest.fixture
def test_recipes():
    topodictionary = {
        "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
        "i": {"nominative": [[""], 0], "genitive": [["o"], 1]},
        "o": {"nominative": [[""], 0], "genitive": [["a"], 1]},
        "ti": {"nominative": [[""], 0], "genitive": [["o"], 1]},
        "esti": {"nominative": [[""], 0], "genitive": [["o", "a"], 1]},
    }
    recipes_test = Recipes(language="test", file=topodictionary)
    recipes_test.load()

    yield recipes_test
