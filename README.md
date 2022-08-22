# Hockey Clock

## Getting Started

### Setup Environment

```bash
# Install Python virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat

# Install Python packages
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Deactivate virtual environment
deactivate
```

### Execute Tools

```bash
# Activate virtual environment
.venv\Scripts\activate.bat

# Format Python code
yapf --style google -i -r hockeyclock

# Lint Python code
pylint --rcfile .pylintrc hockeyclock

# Type check Python code
mypy hockeyclock

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
