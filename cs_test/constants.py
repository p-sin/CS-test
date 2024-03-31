import datetime as dt
from pathlib import Path

TIMESTAMP = dt.datetime.now(tz=dt.timezone.utc).strftime("%Y%M%d-%H%M%S")
CS_PATH = Path.cwd()


class Paths:
    USER_DATA = CS_PATH / "user_data"
    DATA_PATH = CS_PATH / "data"
    PROJECTS_PATH = CS_PATH.parents[0]
    INVALID_LINE_FILE = "invalid_line.csv"
    TEST_PATH = Path("tests/test_data")


OPERATORS = ["(", ")", ">=", "<=", ">", "<", "=", "!=", "!", "NOT"]
CONNECTORS = ["AND", "OR"]


IF_COMMANDS = {
    "(": "[",
    ")": "],",
    "AND": "'AND',",
    "OR": "'OR',",
}

COMMON_NON_VARIABLE_WORDS = [
    r"\bAND\b",
    r"\bOR\b",
    r"\bTRUE\b",
    r"\bFALSE\b",
    r"\bNOT\b",
]

KEYWORDS: dict[str, list[str]] = {
    "common": [
        "ROUND(",
        "MODULO",
        "LENGTH(",
        "(",
        ")",
        "+",
        "=",
        "<",
        ">",
        "-",
        "&",
        "!",
        "%",
        "*IF",
        "*",
        "[B]",
        "[I]",
        "[/B]",
        "[/I]",
        "/",
        "$",
        "@",
        ":",
        ".",
        ",",
        ";",
        "£",
    ],
    "code": [
        "{",
        "}",
        "*SET",
        "*ELSEIF",
        "*SELECTABLE_IF",
        "*ALLOW_REUSE",
        "*DISABLE_REUSE",
        "*HIDE_REUSE",
        "*ELSE",
        "*INPUT_TEXT",
        "*INPUT_NUMBER",
        "'",
        "NOT(",
    ],
    "prose": [
        '"',
        "*page_break",
        "*line_break",
    ],
}
