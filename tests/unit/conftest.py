import pytest

from toponym.case import CaseConfig
from toponym.case import DeclineConfig


@pytest.fixture
def case_config():
    case_config = CaseConfig()

    yield case_config


@pytest.fixture
def decline_config():
    decline_config = DeclineConfig()

    yield decline_config
