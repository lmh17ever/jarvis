"""Инициализация: регистрация всех команд при импорте."""

from jarvis.command_registry import register
from jarvis.commands.volume import (
    VolumeCommand,
    MuteCommand,
    UnmuteCommand,
    IncreaseVolumeCommand,
    DecreaseVolumeCommand,
    PauseMediaCommand,
    ResumeMediaCommand,
    NextMediaCommand,
    PreviousMediaCommand
)
from jarvis.commands.display import TurnOffDisplayCommand
from jarvis.commands.common import TestCommand

def init_commands() -> None:
    """Зарегистрировать все доступные команды."""
    register(VolumeCommand())
    register(MuteCommand())
    register(UnmuteCommand())
    register(IncreaseVolumeCommand())
    register(DecreaseVolumeCommand())
    register(PauseMediaCommand())
    register(ResumeMediaCommand())
    register(TurnOffDisplayCommand())
    register(TestCommand())
    register(NextMediaCommand())
    register(PreviousMediaCommand())