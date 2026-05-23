"""Загрузка Vosk-модели и инициализация распознавателя."""

import json
import os

import vosk

from jarvis.config import MODEL_PATH, SAMPLE_RATE


def load_vosk_model() -> vosk.Model:
    """
    Загрузить Vosk-модель.
    Использует локальную папку с моделью, если она существует,
    иначе скачивает маленькую русскую модель автоматически.
    """
    if os.path.isdir(MODEL_PATH):
        print(f"[JARVIS] Загрузка локальной модели из '{MODEL_PATH}'...")
        model = vosk.Model(model_path=MODEL_PATH)
    else:
        print(f"[JARVIS] Локальная папка '{MODEL_PATH}' не найдена.")
        print("[JARVIS] Автоматическая загрузка маленькой русской модели...")
        model = vosk.Model(lang="ru")
        print("[JARVIS] Модель загружена.")
    return model


def create_recognizer(model: vosk.Model) -> vosk.KaldiRecognizer:
    """Создать распознаватель Vosk для заданной модели."""
    recognizer = vosk.KaldiRecognizer(model, SAMPLE_RATE)
    recognizer.SetWords(False)
    return recognizer


def parse_result(raw: str) -> str:
    """Извлечь финальный текст из JSON-ответа Vosk."""
    data = json.loads(raw)
    return data.get("text", "").strip()


def parse_partial(raw: str) -> str:
    """Извлечь промежуточный текст из JSON-ответа Vosk."""
    data = json.loads(raw)
    return data.get("partial", "").strip()