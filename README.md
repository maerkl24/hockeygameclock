# Hockey Clock

## Getting Started

### Setup Environment

```bat
:: Install Python virtual environment
python -m venv .venv

:: Activate virtual environment
.venv\Scripts\activate.bat

:: Install Python hockeyclock module and its dependencies
python -m pip install -e .
:: Install Python hockeyclock module and its dev dependencies
python -m pip install -e .[dev]

:: Deactivate virtual environment
deactivate
```

### Execute Tools

```bat
:: Execute tools
tools.bat
```

## Create Executable

```bat
:: Create executable
pyinstaller --onefile --windowed --name HockeyClock --icon=icon\HockeyClock.ico py\main.py
```

## TODOs

- [ ] Backend
- [ ] Tests
- [ ] Packaging/Executable
- [ ] User Inferface
- [ ] ...
