import shutil
from pathlib import Path

import pytest

from cs_test.constants import Paths
from cs_test.project import Project


def create_test_path(folder: str) -> Path:
    (Paths.TEST_PATH / folder).mkdir(exist_ok=True, parents=True)
    return Paths.TEST_PATH / folder


@pytest.fixture(name="project")
def fix_project() -> Project:
    """Fixture to create default Project class."""
    return Project(
        project_name="project_name",
        project_path=Path(),
        test_path=Path(),
        ignored_files=["choicescript_stats"],
    )


def pytest_unconfigure() -> None:
    """Runs at end of all tests."""
    shutil.rmtree(Paths.TEST_PATH)
