"""Базовый класс команды и реестр для диспетчеризации голосовых команд."""

import re
from abc import ABC, abstractmethod
from typing import Dict


class Command(ABC):
    """
    Базовый класс для голосовой команды.

    Каждая команда определяет:
    - `pattern` — регулярное выражение для поиска в распознанном тексте
    - `execute` — действие при совпадении
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Уникальное имя команды (для логирования/отладки)."""

    @property
    @abstractmethod
    def pattern(self) -> re.Pattern:
        """Regex-шаблон для поиска в тексте (через search)."""

    @abstractmethod
    def execute(self, text: str, match: re.Match) -> bool:
        """
        Выполнить команду.

        Args:
            text: Исходный распознанный текст (lowercase, stripped).
            match: Результат re.search(pattern, text).

        Returns:
            True если команда обработана, иначе False.
        """


_registry: Dict[str, Command] = {}


def register(command: Command) -> None:
    """Зарегистрировать экземпляр команды в глобальном реестре."""
    _registry[command.name] = command


def dispatch(text: str) -> bool:
    """
    Найти подходящую команду по regex и выполнить её.

    Args:
        text: Распознанный текст.

    Returns:
        True если хотя бы одна команда выполнилась.
    """
    text = text.strip().lower()
    for cmd in list(_registry.values()):
        m = cmd.pattern.search(text)
        if m:
            try:
                if cmd.execute(text, m):
                    return True
            except Exception as e:
                print(f"[JARVIS] Ошибка в команде '{cmd.name}': {e}")
    return False


def list_commands() -> Dict[str, Command]:
    """Вернуть копию реестра команд (для отладки)."""
    return dict(_registry)