import shutil
from pathlib import Path
from typing import Callable

import pytest

from cs_test.constants import Paths
from cs_test.project import Project

TestPathType = Callable[[str], Path]


@pytest.fixture(name="test_path")
def fix_test_path() -> TestPathType:
    """Parametrised fixture to create test paths."""

    def test_path(folder: str) -> Path:
        (Paths.TEST_PATH / folder).mkdir(exist_ok=True, parents=True)
        return Paths.TEST_PATH / folder

    return test_path


@pytest.fixture(name="project")
def fix_project() -> Project:
    """Fixture to create default Project class."""
    return Project(
        project_name="project_name",
        project_folder=Path(),
        test_path=Path(),
        ignored_files=["choicescript_stats"],
    )


def pytest_unconfigure() -> None:
    """Runs at end of all tests."""
    shutil.rmtree(Paths.TEST_PATH)
