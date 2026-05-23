# Команды для голосового ассистента

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

__all__ = [
    "VolumeCommand",
    "MuteCommand",
    "UnmuteCommand",
    "IncreaseVolumeCommand",
    "DecreaseVolumeCommand",
    "PauseMediaCommand",
    "ResumeMediaCommand",
    "NextMediaCommand",
    "PreviosMediaCommand",
    "TurnOffDisplayCommand",
    "TestCommand"
]