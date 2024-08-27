from dataclasses import dataclass, field
from pathlib import Path

from cs_test.files.file import File


@dataclass
class Project:
    """Project class container for all CS_test functionality."""

    project_name: str
    project_path: Path
    test_path: Path
    ignored_files: list[str]
    files: dict[str, File] = field(init=False, default_factory=dict)

    @property
    def file_list(self) -> list[Path]:
        """All txt files in the project folder.

        Returns:
            list[Path]: List of all txt files in the project folder.
        """
        return [
            file
            for file in self.project_path.glob("*.txt")
            if not any(ignored == file.stem for ignored in self.ignored_files)
        ]

    @property
    def file_number(self) -> int:
        """Number of txt files in the project folder.

        Returns:
            int: Number of txt files in the project folder.
        """
        return len(self.file_list)

    def parse_files(self) -> None:
        """Read CS project files and convert them to the CS_test model.

        The code in each file is parsed and mapped into the File class.
        """
        self.files = {
            file.stem: File(self.project_path / file) for file in self.file_list
        }
        for file in self.files.values():
            file.parse_code()

    def test_project(self) -> None:
        """Control flow for the Project class."""
        self.parse_files()
