import shutil
from unittest.mock import Mock, PropertyMock, patch

from cs_test.project import Project
from tests.conftest import TestPathType


def test_project_file_list(test_path: TestPathType, project: Project) -> None:
    """Asseert that the file_list property correctly parses the project folder."""
    path = test_path("project_file_list")

    for file in ["A.txt", "B.csv", "C.txt", "D.toml"]:
        (path / file).touch()

    project.project_path = path

    assert sorted(project.file_list) == [path / "A.txt", path / "C.txt"]

    shutil.rmtree(path)


@patch("cs_test.project.Project.file_list", new_callable=PropertyMock)
def test_project_file_number(mock_file_list: Mock, project: Project) -> None:
    """Assert that the file_number property correctly calculates the length of file_list."""
    mock_file_list.return_value = ["A.txt", "B.txt", "C.txt"]
    assert project.file_number == 3
