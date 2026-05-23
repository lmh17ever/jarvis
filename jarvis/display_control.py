import ctypes

from jarvis.audio_output import speak_random_accepted


def turn_off_display() -> None:
    """Выключить дисплей (монитор)."""
    try:
        print("[JARVIS] Выключаю дисплей...")

        # WM_SYSCOMMAND = 0x0112
        # SC_MONITORPOWER = 0xF170
        # 2 = power off
        ctypes.windll.user32.SendMessageW(
            0xFFFF,
            0x0112,
            0xF170,
            2
        )

        speak_random_accepted()

        print("[JARVIS] Дисплей выключен")

    except Exception as e:
        print(f"[JARVIS] Ошибка выключения дисплея: {e}")