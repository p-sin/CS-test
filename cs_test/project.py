from dataclasses import dataclass
from pathlib import Path

# from cstest.content.files.file import File


@dataclass
class Project:
    """Project class container for all CS_test functionality."""

    project_name: str
    project_folder: Path
    test_path: Path
    ignored_files: list[str]
    # files: list[File] = field(init=False)

    @property
    def file_list(self) -> list[Path]:
        """All txt files in the project folder."""
        return [
            file
            for file in self.project_folder.glob("*.txt")
            if not any(ignored == file.stem for ignored in self.ignored_files)
        ]

    @property
    def file_number(self) -> int:
        """Number of txt files in the project folder."""
        return len(self.file_list)

    # def parse_files(self) -> None:
    #     self.files = [File(self.project_folder / file) for file in self.file_list]
    #     for file in self.files:
    #         file.parse_code()

    def test_project(self) -> None:
        """pass."""
        # self.parse_files()
