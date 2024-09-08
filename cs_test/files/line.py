from dataclasses import dataclass


@dataclass
class Line:
    # row_number: int
    # orig_line: str
    # command: Command = field(init=False)
    # next_line: int = field(init=False)

    # @property
    # def indent(self) -> int:
    #     """Calculate length of whitespace indent for the line."""
    #     return len(self.orig_line) - len(self.orig_line.lstrip(" "))

    # @property
    # def clean_line(self) -> str:
    #     """Replace new line characters, remove indent and uppercase."""
    #     return self.orig_line.replace("\n", "").lstrip().upper()

    # def set_command(self) -> None:
    #     """Calculate the type of line (prose, creation, access, comment)."""
    #     command = self.clean_line.split(" ")[0].replace("*", "")

    #     if self.clean_line.startswith("*"):
    #         try:
    #             self.command = command_mapper[command]
    #         except Exception:
    #             self.command = "Unknown command"
    #     else:
    #         try:  # If it's a valid command missing an *
    #             self.command = command_mapper[command]
    #         except Exception:
    #             self.command = "Prose"

    def process_line(self) -> None:
        # self.set_command()
        pass
