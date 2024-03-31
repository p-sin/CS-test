from dataclasses import dataclass, field
from pathlib import Path

from CS_test.constants import Paths, TIMESTAMP


@dataclass
class Config:
    """Class to encapsulate all project level configuration for powering CS_test.

    Contains:
    - project_name [str]: Folder name containing CS project to be tested
    - project_path [Path]: Pathlib object containing path to CS project folder
    - test_path [Path]: Pathlib object containing path to output folder for CS_test
    for this CS project
    - ignored_files [list[str]]: Any files in the CS project to be ignored
    """
    project_name: str = field(init=False)
    project_path: Path = field(init=False)
    test_path: Path = field(init=False)
    ignored_files: list[str] = field(default_factory=list)

    def ask_folder_name(self) -> str:
        """Requests CS project folder name from user.

        Returns:
            str: Name of CS project folder
        """
        return input(
            "What is the folder name of the project you would like to test?"
        )

    def set_folder_path(self) -> None:
        """Sets project path based on user input.

        if a CS project with that name exists in the projects_path.

        Returns:
        None
        """
        self.project_name = self.ask_folder_name()
        self.project_path = Paths.PROJECTS_PATH / self.project_name

        if self.project_path.exists():
            return

        print(
            f"The folder: {self.project_name} does not exist in directory:"
            f" {Paths.PROJECTS_PATH}."
        )
        self.set_folder_path()



    def create_test_folder(self) -> None:
        """Creates output directory for this run of CS_test."""
        self.test_path = Paths.DATA_PATH / self.project_name / str(TIMESTAMP)
        Path.mkdir(self.test_path, parents=True)

    def config_test(self) -> None:
        """Entry point for setting CS_test configuration."""
        self.set_folder_path()
        self.create_test_folder()
        self.ignored_files = ["choicescript_stats"]
