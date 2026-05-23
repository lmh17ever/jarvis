import re

from jarvis.command_registry import Command
from jarvis.display_control import turn_off_display


class TurnOffDisplayCommand(Command):
    """Команда: 'джарвис выключи дисплей'."""

    @property
    def name(self) -> str:
        return "turn_off_display"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            r"джарвис.*(выключи|погаси)\s+(монитор|экран|дисплей)"
        )

    def execute(self, text: str, match: re.Match) -> bool:
        turn_off_display()
        return True