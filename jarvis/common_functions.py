from jarvis.audio_output import speak_random_test


def jarvis_test() -> None:
    """Проверка работы."""
    try:
        print("[JARVIS] Проверка работы...")

        speak_random_test()

        print("[JARVIS] Проверка завершена")

    except Exception as e:
        print(f"[JARVIS] Ошибка проверки работы: {e}")