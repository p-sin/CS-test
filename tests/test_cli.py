import json
from pathlib import Path
from unittest.mock import Mock, patch

from click.testing import CliRunner

from cs_test.cli import Config, Project, cs_test
from tests.conftest import create_test_path


@patch("cs_test.cli.Config.setup", autospec=True)
@patch("cs_test.cli.Project.test_project", autospec=True)
def test_cs_test(mock_project: Mock, mock_config: Mock) -> None:
    """Test the cs_test function."""
    path = create_test_path("cs_test")

    def mock_config_func(self: Config) -> None:
        self.project_name = "proj_name"
        self.project_path = Path("proj_path")
        self.test_path = Path("test_path")
        self.ignored_files = ["a", "b"]

    mock_config.side_effect = mock_config_func

    def mock_project_func(self: Project) -> None:
        with (path / "proj.json").open(mode="w", encoding="utf-8") as f:
            json.dump(
                {
                    "name": self.project_name,
                    "proj_path": str(self.project_path),
                    "test_path": str(self.test_path),
                    "ignored": self.ignored_files,
                },
                f,
            )

    mock_project.side_effect = mock_project_func

    runner = CliRunner()
    runner.invoke(cs_test, [])

    with (path / "proj.json").open(mode="r", encoding="utf-8") as f:
        proj = json.load(f)

    assert mock_config.call_count == 1
    assert proj["name"] == "proj_name"
    assert proj["proj_path"] == "proj_path"
    assert proj["test_path"] == "test_path"
    assert proj["ignored"] == ["a", "b"]
    assert mock_project.call_count == 1
