# Jarvis (brainstorm)

Lightweight local voice assistant prototype (Python).

## Overview

This repository contains a small voice assistant / speech-to-text experiment using Vosk and local models. It includes a runnable entrypoint `jarvis.py` and a `jarvis/` package with audio, STT, and command components.

## Requirements

- Python 3.12 (tested)
- Virtual environment recommended
- Native audio dependencies (PyAudio / sound drivers) for microphone I/O

Install Python packages from `requirements.txt`:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
```

Place [vosk-model-small-ru-0.22](https://alphacephei.com/vosk/models) into the project folder (or use any other Vosk model and specify the model folder name in the config).


## Running

After activating the virtualenv, start the assistant:

```bash
python jarvis.py
```

There are example audio files under `audio/` and packaged model data under `vosk-model-small-ru-0.22/` used for offline STT.

## Project layout

- `jarvis.py` — entrypoint script
- `jarvis/` — package: STT, audio output, command registry, main loop
- `audio/` — recorded / test audio files
 
- `vosk-model*` — speech model folders (not all may be required)

## Usage

This project is used as a local voice assistant. Basic usage:

- Start the assistant:

```bash
python jarvis.py
```

- Speak to the assistant using the wake name ("джарвис" and similar variants). After the wake name, say a command in Russian. Example commands:

    - "Джарвис"
    - "Джарвис, ты тут/здесь?"
    - "Джарвис, выключи/погаси монитор/экран/дисплей"
    - "Джарвис, громкость десять/двадцать/тридцать итд"
    - "Джарвис, выключи звук"
    - "Джарвис, включи звук"
    - "Джарвис, громкость больше/меньше на десять/двадцать/тридцать итд"
    - "Джарвис, увеличь/уменьши громкость на десять/двадцать/тридцать итд"
    - "Джарвис, пауза/останови/поставь на паузу"
    - "Джарвис, продолжи/воспроизведи"
    - "Джарвис, следующий(ая)/предыдущий(ая) трек, песня, видео, серия или просто дальше/назад"


- Commands are defined as regex patterns in the `jarvis/commands/` package. To add or change behaviour, edit or add files there.

- Configure recognition and the list of recognized wake-name variants in `jarvis/config.py` (`JARVIS_NAMES` / `JARVIS_PATTERN`).

- The assistant plays short audio replies from `audio/accepted/` and `audio/not_recognized/` when it accepts or fails to recognize a command. For quick testing you can place recordings in `audio/test/`.


## Notes

 - Store large model files outside the repository or add `.gitignore` entries as needed to avoid committing them.
- If you plan to use a microphone on Windows, ensure proper audio drivers and that PyAudio is built for your Python version.

## License & Attribution

This repository is a personal project. Add a LICENSE file if you plan to publish or share.

---

If you'd like, I can expand the README with examples, a quickstart GIF, or platform-specific setup steps. 
