import pytest

from toponym.case import CaseConfig


@pytest.fixture
def case_config():
    case_config = CaseConfig()

    yield case_config
