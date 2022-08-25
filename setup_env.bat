:: Install Python virtual environment
python -m venv .venv

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Upgrade pip
python -m pip install --upgrade pip

:: Install Python hockeyclock module and its dependencies
::python -m pip install -e .
:: Install Python hockeyclock module and its development dependencies
python -m pip install -e .[dev]

:: Deactivate virtual environment
call deactivate
