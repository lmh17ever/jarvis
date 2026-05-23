"""
Jarvis — голосовой ассистент с оффлайн-распознаванием через Vosk.
Управление громкостью Windows (pycaw), звуковые ответы (pygame).
"""

import sys

from jarvis.bootstrap import init_commands
from jarvis.main_loop import listen_continuous


def main() -> None:
    print("=" * 50)
    print("  JARVIS — голосовой ассистент (Vosk + pycaw)")
    print("=" * 50)

    init_commands()

    try:
        listen_continuous()
    except Exception as e:
        print(f"[JARVIS] Фатальная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()