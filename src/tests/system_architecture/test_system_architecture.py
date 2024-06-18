import pytest

from src.tests.system_architecture.utils import check_system_architecture

pytestmark = pytest.mark.system_architecture


def test_system_architecture():
    check_system_architecture()
