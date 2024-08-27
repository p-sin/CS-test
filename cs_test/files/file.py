from dataclasses import dataclass, field
from pathlib import Path

from cs_test.files.line import Line


@dataclass
class File:
    """File class container for all code within each CS project file."""

    file_path: Path
    code: dict[int, Line] = field(init=False)

    def parse_code(self) -> None:
        """Read in and store every line of code in the file.

        Creates a dictionary of Line objects, where the key is the line number.
        """
        self.code = {}
        with self.file_path.open(encoding="utf-8") as cs_file:
            code = cs_file.readlines()

        for _, code_line in enumerate(code):
            if str.isspace(code_line) or not code_line:
                continue

            # self.code[row_number] = Line(row_number, code_line)
            # self.code[row_number].process_line()
