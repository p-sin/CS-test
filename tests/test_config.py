import shutil
from unittest.mock import Mock, patch

import pytest

from CS_test.config import Config
from CS_test.constants import Paths
from tests.conftest import TestPathType


def test_ask_folder_name() -> None:
    """Assert that given project_name is returned."""
    config = Config()
    with patch("builtins.input", return_value="test"):
        assert config.ask_folder_name() == "test"


@pytest.mark.parametrize(
    ("folder_names", "call_count"),
    [
        (["A"], 1),
        (["D", "C", "B", "A"], 4),
        (["C", "A", "B"], 2),
    ],
)
@patch("CS_test.config.Config.ask_folder_name", autospec=True)
def test_set_folder_path(
    mock_folder: Mock,
    folder_names: list[str],
    call_count: int,
    test_path: TestPathType,
) -> None:
    """Assert that the returned project_name is correctly set.

    if the folder exists, then return. Otherwise the ask_folder_name method is called again
    until a valid project_name is provided.
    """
    path = test_path("set_folder")
    (path / "A").mkdir(exist_ok=True, parents=True)

    mock_folder.side_effect = folder_names

    with patch("CS_test.config.Paths.PROJECTS_PATH", path):
        config = Config()
        config.set_folder_path()

    assert config.project_path == Paths.TEST_PATH / "set_folder" / "A"
    assert mock_folder.call_count == call_count

    shutil.rmtree(path)


def test_create_test_folder(test_path: TestPathType) -> None:
    """Asseert that the correct test path is generated."""
    path = test_path("test_folder")

    config = Config()
    config.project_name = "A"

    with patch("CS_test.config.Paths.DATA_PATH", path), patch(
        "CS_test.config.TIMESTAMP", "B"
    ):
        config.create_test_folder()

    assert config.test_path == path / "A" / "B"

    shutil.rmtree(path)


@patch("CS_test.config.Config.set_folder_path")
@patch("CS_test.config.Config.create_test_folder")
def test_config_test(mock_folder: Mock, mock_path: Mock) -> None:
    """Assert that the correct methods are called."""
    config = Config()
    config.config_test()

    assert mock_folder.call_count == 1
    assert mock_path.call_count == 1
    assert config.ignored_files == ["choicescript_stats"]
