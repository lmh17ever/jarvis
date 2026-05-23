"""Бесконечный цикл захвата аудио с микрофона и распознавания через Vosk."""

import json
import sys

import pyaudio

from jarvis.config import SAMPLE_RATE, CHUNK_SIZE, CHANNELS, FORMAT, JARVIS_NAMES
from jarvis.stt import load_vosk_model, create_recognizer, parse_result, parse_partial
from jarvis.command_registry import dispatch
from jarvis.audio_output import speak_random_not_recognized


def _is_jarvis_name_in(text: str) -> bool:
    """Проверить, содержит ли текст одно из имён из JARVIS_NAMES."""
    text_lower = text.lower()
    for name in JARVIS_NAMES:
        if name in text_lower:
            return True
    return False


def listen_continuous() -> None:
    """
    Бесконечный цикл захвата аудио с микрофона и распознавания через Vosk.
    Распознанный текст передаётся в dispatch().
    """
    model = load_vosk_model()
    recognizer = create_recognizer(model)

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
    )
    stream.start_stream()

    print("[JARVIS] Слушаю... (скажите 'джарвис ...')")
    print("[JARVIS] Для выхода нажмите Ctrl+C\n")

    partial_prev = ""

    try:
        while True:
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)

            if recognizer.AcceptWaveform(data):
                final_text = parse_result(recognizer.Result())
                if final_text:
                    print(f"\n[JARVIS] Распознано: {final_text}")
                    if not dispatch(final_text) and _is_jarvis_name_in(final_text):
                        speak_random_not_recognized()
                partial_prev = ""
            else:
                partial_text = parse_partial(recognizer.PartialResult())
                if partial_text and partial_text != partial_prev:
                    print(f"  [{partial_text}]", end="\r", flush=True)
                    partial_prev = partial_text

    except KeyboardInterrupt:
        print("\n[JARVIS] Завершение по Ctrl+C")
    except Exception as e:
        print(f"\n[JARVIS] Критическая ошибка: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("[JARVIS] Поток аудио закрыт")