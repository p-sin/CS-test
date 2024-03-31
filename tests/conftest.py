import shutil
from pathlib import Path
from typing import Callable

import pytest

from CS_test.constants import Paths

TestPathType = Callable[[str], Path]


@pytest.fixture(name="test_path")
def fix_test_path() -> TestPathType:
    def test_path(folder: str) -> Path:
        (Paths.TEST_PATH / folder).mkdir(exist_ok=True, parents=True)
        return Paths.TEST_PATH / folder

    return test_path


def pytest_unconfigure() -> None:
    shutil.rmtree(Paths.TEST_PATH)
