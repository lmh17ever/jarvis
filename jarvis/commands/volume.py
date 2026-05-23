"""Команды управления громкостью Windows."""

import re

from jarvis.command_registry import Command
from jarvis.config import NUMBER_WORDS, JARVIS_PATTERN
from jarvis.volume_control import (
    set_volume,
    mute_audio,
    unmute_audio,
    increase_volume,
    decrease_volume,
    pause_media,
    resume_media,
    next_media,
    previous_media
)


def _parse_volume_value(value: str):
    """Преобразовать значение громкости: цифры или слова."""
    value = value.strip().lower()
    if value.isdigit():
        return int(value)
    return NUMBER_WORDS.get(value)


class VolumeCommand(Command):
    """Команда: '<имя> громкость <число>' (цифрами или словами)."""

    @property
    def name(self) -> str:
        return "volume"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(rf"{JARVIS_PATTERN}.*громкост[ьи]\s+(.+)")

    def execute(self, text: str, match: re.Match) -> bool:
        raw_value = match.group(1).strip()
        level = _parse_volume_value(raw_value)
        if level is not None:
            set_volume(level)
            return True
        return False


class MuteCommand(Command):
    """Команда: '<имя> выключи звук'."""

    @property
    def name(self) -> str:
        return "mute"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(rf"{JARVIS_PATTERN}.*выключ(и|ь)\s+звук")

    def execute(self, text: str, match: re.Match) -> bool:
        mute_audio()
        return True


class UnmuteCommand(Command):
    """Команда: '<имя> включи звук'."""

    @property
    def name(self) -> str:
        return "unmute"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(rf"{JARVIS_PATTERN}.*включ(и|ь)\s+звук")

    def execute(self, text: str, match: re.Match) -> bool:
        unmute_audio()
        return True


class IncreaseVolumeCommand(Command):
    """Команда: '<имя> увеличь громкость на <число>'."""

    @property
    def name(self) -> str:
        return "increase_volume"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"{JARVIS_PATTERN}.*(?:"
            rf"увелич(ь|ить)\s+громкость\s+на|"
            rf"громкость\s+больш(е|е сделать)\s+на"
            rf")\s+(.+)",
            re.IGNORECASE
        )

    def execute(self, text: str, match: re.Match) -> bool:
        raw_value = match.group(3).strip()
        level = _parse_volume_value(raw_value)
        if level is not None:
            increase_volume(level)
            return True
        return False


class DecreaseVolumeCommand(Command):
    """Команда: '<имя> уменьши громкость на <число>'."""

    @property
    def name(self) -> str:
        return "decrease_volume"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"{JARVIS_PATTERN}.*(?:"
            rf"уменьш(и|ить)\s+громкость\s+на|"
            rf"громкость\s+меньш(е|е сделать)\s+на"
            rf")\s+(.+)",
            re.IGNORECASE
        )

    def execute(self, text: str, match: re.Match) -> bool:
        raw_value = match.group(3).strip()
        level = _parse_volume_value(raw_value)
        if level is not None:
            decrease_volume(level)
            return True
        return False


class PauseMediaCommand(Command):
    """Команда: 'джарвис пауза'."""

    @property
    def name(self) -> str:
        return "pause_media"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"{JARVIS_PATTERN}.*(пауза|останови|поставь на паузу)"
        )

    def execute(self, text: str, match: re.Match) -> bool:
        pause_media()
        return True


class ResumeMediaCommand(Command):
    """Команда: 'джарвис продолжи'."""

    @property
    def name(self) -> str:
        return "resume_media"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"{JARVIS_PATTERN}.*(продолжи|воспроизведи|включи музыку)"
        )

    def execute(self, text: str, match: re.Match) -> bool:
        resume_media()
        return True


class NextMediaCommand(Command):
    """Команда: 'джарвис следующий'."""

    @property
    def name(self) -> str:
        return "next_media"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"{JARVIS_PATTERN}.*(следующ(ий|ая|ее)|дальше|next)\s*(трек|песня|видео|серия)?"
        )

    def execute(self, text: str, match: re.Match) -> bool:
        next_media()
        return True


class PreviousMediaCommand(Command):
    """Команда: 'джарвис предыдущий'."""

    @property
    def name(self) -> str:
        return "previous_media"

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"{JARVIS_PATTERN}.*(предыдущ(ий|ая|ее)|назад|previous)\s*(трек|песня|видео|серия)?"
        )

    def execute(self, text: str, match: re.Match) -> bool:
        previous_media()
        return True