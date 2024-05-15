from abc import ABC
from typing import Literal


class Command(ABC):
    """Abstract base class for defining all ChoiceScript commands."""

    command_type: Literal["Bug", "Code", "Comment", "Misc", "Script", "Stats"]
    command_name: str


class Achieve(Command):
    command_type = "Code"
    command_name = "ACHIEVE"


class Achievement(Command):
    command_type = "Code"
    command_name = "ACHIEVEMENT"


class AllowReuse(Command):
    command_type = "Code"
    command_name = "ALLOW_REUSE"


class Author(Command):
    command_type = "Misc"
    command_name = "AUTHOR"


class Bug(Command):
    command_type = "Bug"
    command_name = "BUG"


class CheckAchievements(Command):
    command_type = "Code"
    command_name = "CHECK_ACHIEVEMENTS"


class Choice(Command):
    command_type = "Code"
    command_name = "CHOICE"


class Commwnr(Command):
    command_type = "Comment"
    command_name = "COMMENT"


class Create(Command):
    command_type = "Code"
    command_name = "CREATE"


class Delete(Command):
    command_type = "Code"
    command_name = "DELETE"


class DisableReuse(Command):
    command_type = "Code"
    command_name = "DISABLE_REUSE"


class Else(Command):
    command_type = "Code"
    command_name = "ELSE"


class ElseIf(Command):
    command_type = "Code"
    command_name = "ELSEIF"


class Ending(Command):
    command_type = "Code"
    command_name = "ENDING"


class FakeChoice(Command):
    command_type = "Code"
    command_name = "FAKE_CHOICE"


class Finish(Command):
    command_type = "Code"
    command_name = "FINISH"


class Gosub(Command):
    command_type = "Code"
    command_name = "GOSUB"


class GosubScene(Command):
    command_type = "Code"
    command_name = "GOSUB_SCENE"


class Goto(Command):
    command_type = "Code"
    command_name = "GOTO"


class GotoRef(Command):
    command_type = "Code"
    command_name = "GOTOREF"


class GotoRandomScene(Command):
    command_type = "Code"
    command_name = "GOTO_RANDOM_SCENE"


class GotoScene(Command):
    command_type = "Code"
    command_name = "GOTO_SCENE"


class HideReuse(Command):
    command_type = "Code"
    command_name = "HIDE_REUSE"


class If(Command):
    command_type = "Code"
    command_name = "IF"


class Image(Command):
    command_type = "Misc"
    command_name = "IMAGE"


class ImplicitControlFlow(Command):
    command_type = "Code"
    command_name = "IMPLICIT_CONTROL_FLOW"


class InputNumber(Command):
    command_type = "Code"
    command_name = "INPUT_NUMBER"


class InputText(Command):
    command_type = "Code"
    command_name = "INPUT_TEXT"


class Label(Command):
    command_type = "Code"
    command_name = "LABEL"


class LineBreak(Command):
    command_type = "Misc"
    command_name = "LINE_BREAK"


class Link(Command):
    command_type = "Misc"
    command_name = "LINK"


class LoopLimit(Command):
    command_type = "Code"
    command_name = "LOOPLIMIT"


class MoreGames(Command):
    command_type = "Misc"
    command_name = "MORE_GAMES"


class Multireplace(Command):
    command_type = "Code"
    command_name = "MULTIREPLACE"


class PageBreak(Command):
    command_type = "Misc"
    command_name = "PAGE_BREAK"


class Print(Command):
    command_type = "Misc"
    command_name = "PRINT"


class Rand(Command):
    command_type = "Code"
    command_name = "RAND"


class SetRef(Command):
    command_type = "Code"
    command_name = "SETREF"


class SceneList(Command):
    command_type = "Code"
    command_name = "SCENE_LIST"


class Script(Command):
    command_type = "Script"
    command_name = "SCRIPT"


class SelectableIf(Command):
    command_type = "Code"
    command_name = "SELECTABLE_IF"


class Set(Command):
    command_type = "Code"
    command_name = "SET"


class ShareThisGame(Command):
    command_type = "Misc"
    command_name = "SHARE_THIS_GAME"


class ShowPassword(Command):
    command_type = "Misc"
    command_name = "SHOW_PASSWORD"


class Sound(Command):
    command_type = "Misc"
    command_name = "SOUND"


class StatChart(Command):
    command_type = "Stats"
    command_name = "ACHIEVE"


class Temp(Command):
    command_type = "Code"
    command_name = "TEMP"


class Title(Command):
    command_type = "Misc"
    command_name = "TITLE"
