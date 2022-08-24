# Hockey Clock

## Getting Started

### Setup Environment

```bash
# Install Python virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat

# Install Python hockeyclock module and its dependencies
python -m pip install -e .
# Install Python hockeyclock module and its dev dependencies
python -m pip install -e .[dev]

# Deactivate virtual environment
deactivate
```

### Execute Tools

```bash
# Activate virtual environment
.venv/Scripts/activate.bat

# Sort imports
isort hockeyclock
isort tests

# Format Python code
black hockeyclock
black tests

# Lint Python code
pylint hockeyclock
pylint tests

# Type check Python code
mypy hockeyclock
mypy tests

# Build the docs
cd docs
make html

# Execute Python tests
pytest tests
```

## Create Executable

```bash
pyinstaller --onefile --windowed --name HockeyClock --icon=icon/HockeyClock.ico py/main.py
```

## ToDos

* A lot ...
