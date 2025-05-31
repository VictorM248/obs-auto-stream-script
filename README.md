# OBS Auto Stream Scheduler

This Python script allows OBS Studio to automatically start and stop streaming at specified times each day, excluding Sundays. It is designed to run within OBS using its built-in Python scripting interface.

## Features

- Automatically starts streaming at a defined time
- Automatically stops streaming at a defined time
- Skips Sundays
- Logs stream start/stop actions to the OBS log
- Simple and customizable by editing the script

## Requirements

- **OBS Studio 31.0.2**
  - This script is tested and confirmed to work on version **31.0.2**.
  - Other versions may work, but compatibility is not guaranteed.
- **Python 3.10.0**
  - OBS scripting currently works best with **Python 3.10.0**.
  - Newer or Store-installed Python versions (e.g., 3.11+, WindowsApps) may not work.

> ⚠️ **Notice:** You must use Python **3.10.0** and link OBS to it under `Tools > Scripts > Python Settings`.

📥 [Download Python 3.10.0](https://www.python.org/downloads/release/python-3100/)

## Installation

1. Install Python 3.10.0 and make sure to check **“Add Python to PATH”** during installation.
2. Open OBS (version 31.0.2 or later).
3. Go to `Tools > Scripts`.
4. Click the **Python Settings** button and set the path to your Python 3.10 install directory (e.g., `C:\Program Files\Python310\`).
5. Click the ➕ button and load `script.py`.

## Configuration

Open `script.py` and edit the following lines to set your preferred start and stop times:

```python
START_TIME = "16:40"
STOP_TIME = "16:42"
