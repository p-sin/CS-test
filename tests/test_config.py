import shutil
from unittest.mock import Mock, patch

import pytest

from cs_test.config import Config
from cs_test.constants import Paths
from tests.conftest import create_test_path


def test_ask_folder_name() -> None:
    """Assert that given project_name is returned."""
    config = Config()
    with patch("builtins.input", return_value="test"):
        assert config._ask_folder_name() == "test"


@pytest.mark.parametrize(
    ("folder_names", "call_count"),
    [
        (["A"], 1),
        (["D", "C", "B", "A"], 4),
        (["C", "A", "B"], 2),
    ],
)
@patch("cs_test.config.Config._ask_folder_name", autospec=True)
def test_set_folder_path(
    mock_folder: Mock,
    folder_names: list[str],
    call_count: int,
) -> None:
    """Assert that the returned project_name is correctly set.

    if the folder exists, then return. Otherwise the ask_folder_name method is called again
    until a valid project_name is provided.
    """
    path = create_test_path("set_folder")
    (path / "A").mkdir(exist_ok=True, parents=True)

    mock_folder.side_effect = folder_names

    with patch("cs_test.config.Paths.PROJECTS_PATH", path):
        config = Config()
        config._set_folder_path()

    assert config.project_path == Paths.TEST_PATH / "set_folder" / "A"
    assert mock_folder.call_count == call_count

    shutil.rmtree(path)


def test_create_test_folder() -> None:
    """Asseert that the correct test path is generated."""
    path = create_test_path("test_folder")

    config = Config()
    config.project_name = "A"

    with patch("cs_test.config.Paths.DATA_PATH", path), patch(
        "cs_test.config.TIMESTAMP", "B"
    ):
        config._create_test_folder()

    assert config.test_path == path / "A" / "B"

    shutil.rmtree(path)


@patch("cs_test.config.Config._set_folder_path")
@patch("cs_test.config.Config._create_test_folder")
def test_config(mock_folder: Mock, mock_path: Mock) -> None:
    """Assert that the correct methods are called."""
    config = Config()
    config.setup()

    assert mock_folder.call_count == 1
    assert mock_path.call_count == 1
    assert config.ignored_files == ["choicescript_stats"]
