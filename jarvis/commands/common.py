import re

from jarvis.command_registry import Command
from jarvis.common_functions import jarvis_test
from jarvis.config import JARVIS_PATTERN


class TestCommand(Command):
    """Команда: 'Тест'."""

    @property
    def name(self) -> str:
        return "test"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"^\s*{JARVIS_PATTERN}(?:\s+(ты\s+(тут|здесь)))?\s*$",
            re.IGNORECASE
        )

    def execute(self, text: str, match: re.Match) -> bool:
        jarvis_test()
        return True