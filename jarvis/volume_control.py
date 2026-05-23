"""Управление громкостью Windows через pycaw."""

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  # noqa: F401


from jarvis.audio_output import speak_random_accepted


def get_volume_percent() -> int:
    """Получить текущую громкость в процентах."""
    try:
        volume = _get_endpoint_volume()
        current = volume.GetMasterVolumeLevelScalar()
        return int(current * 100)
    except Exception as e:
        print(f"[JARVIS] Ошибка получения громкости: {e}")
        return 0


def _get_endpoint_volume():
    """Получить интерфейс IAudioEndpointVolume для speakers."""
    device = AudioUtilities.GetSpeakers()
    return device.EndpointVolume


def set_volume(percent: int) -> None:
    """
    Установить громкость системных динамиков в процентах [0..100].
    После успеха — голосовой ответ.
    """
    percent = max(0, min(100, percent))
    try:
        volume = _get_endpoint_volume()
        volume.SetMasterVolumeLevelScalar(percent / 100.0, None)
        print(f"[JARVIS] Громкость установлена на {percent}%")
        speak_random_accepted()
    except Exception as e:
        print(f"[JARVIS] Ошибка установки громкости: {e}")


def mute_audio() -> None:
    """Выключить звук."""
    try:
        speak_random_accepted()
        volume = _get_endpoint_volume()
        volume.SetMute(True, None)
        print("[JARVIS] Звук выключен")
    except Exception as e:
        print(f"[JARVIS] Ошибка отключения звука: {e}")


def unmute_audio() -> None:
    """Включить звук."""
    try:
        volume = _get_endpoint_volume()
        volume.SetMute(False, None)
        print("[JARVIS] Звук включён")
        speak_random_accepted()
    except Exception as e:
        print(f"[JARVIS] Ошибка включения звука: {e}")


def increase_volume(step: int) -> None:
    """Увеличить громкость на указанное количество процентов."""
    try:
        current = get_volume_percent()
        new_volume = min(100, current + step)

        volume = _get_endpoint_volume()
        volume.SetMasterVolumeLevelScalar(new_volume / 100.0, None)

        print(f"[JARVIS] Громкость увеличена до {new_volume}%")
        speak_random_accepted()

    except Exception as e:
        print(f"[JARVIS] Ошибка увеличения громкости: {e}")


def decrease_volume(step: int) -> None:
    """Уменьшить громкость на указанное количество процентов."""
    try:
        current = get_volume_percent()
        new_volume = max(0, current - step)

        volume = _get_endpoint_volume()
        volume.SetMasterVolumeLevelScalar(new_volume / 100.0, None)

        print(f"[JARVIS] Громкость уменьшена до {new_volume}%")
        speak_random_accepted()

    except Exception as e:
        print(f"[JARVIS] Ошибка уменьшения громкости: {e}")


from pycaw.pycaw import AudioUtilities

# ...


def pause_media() -> None:
    """Поставить медиа на паузу."""
    try:
        import pyautogui

        pyautogui.press("playpause")

        print("[JARVIS] Медиа поставлено на паузу")

        speak_random_accepted()

    except Exception as e:
        print(f"[JARVIS] Ошибка паузы медиа: {e}")


def resume_media() -> None:
    """Продолжить воспроизведение медиа."""
    try:
        import pyautogui

        speak_random_accepted()

        pyautogui.press("playpause")

        print("[JARVIS] Медиа продолжено")

    except Exception as e:
        print(f"[JARVIS] Ошибка продолжения медиа: {e}")


def next_media() -> None:
    """Следующий трек / видео / серия."""
    try:
        import pyautogui

        pyautogui.press("nexttrack")

        print("[JARVIS] Следующий медиа-элемент")
        speak_random_accepted()

    except Exception as e:
        print(f"[JARVIS] Ошибка next media: {e}")


def previous_media() -> None:
    """Предыдущий трек / видео / серия."""
    try:
        import pyautogui

        pyautogui.press("prevtrack")

        print("[JARVIS] Предыдущий медиа-элемент")
        speak_random_accepted()

    except Exception as e:
        print(f"[JARVIS] Ошибка previous media: {e}")