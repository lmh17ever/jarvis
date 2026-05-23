"""Воспроизведение MP3-ответов через pygame."""

import os
import random
import time

import pygame

from jarvis.config import (
    AUDIO_ACCEPTED_DIR,
    AUDIO_ACCEPTED_FILES,
    AUDIO_NOT_RECOGNIZED_DIR,
    AUDIO_NOT_RECOGNIZED_FILES,
    AUDIO_TEST_DIR,
    AUDIO_TEST_FILES
)

pygame.mixer.init()


def play_mp3(file_path: str) -> None:
    """Воспроизвести MP3-файл (синхронно)."""
    if not os.path.isfile(file_path):
        print(f"[JARVIS] MP3 не найден: {file_path}")
        return
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
    except Exception as e:
        print(f"[JARVIS] Ошибка воспроизведения MP3: {e}")


def speak_random_accepted() -> None:
    """Случайный звуковой ответ из директории accepted."""
    filename = random.choice(AUDIO_ACCEPTED_FILES)
    file_path = os.path.join(AUDIO_ACCEPTED_DIR, filename)
    play_mp3(file_path)


def speak_random_not_recognized() -> None:
    """Случайный звуковой ответ когда команда не распознана."""
    filename = random.choice(AUDIO_NOT_RECOGNIZED_FILES)
    file_path = os.path.join(AUDIO_NOT_RECOGNIZED_DIR, filename)
    play_mp3(file_path)

def speak_random_test() -> None:
    """Случайный звуковой ответ из директории test."""
    filename = random.choice(AUDIO_TEST_FILES)
    file_path = os.path.join(AUDIO_TEST_DIR, filename)
    play_mp3(file_path)