:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Sort imports
isort hockeygameclock
isort tests

:: Format Python code
black hockeygameclock
black tests

:: Lint Python code
pylint hockeygameclock
pylint tests

:: Type check Python code
mypy hockeygameclock
mypy tests

:: Execute Python tests and measure coverage
pytest

:: Build the docs
cd docs
call make html
cd ..

:: Deactivate virtual environment
call deactivate
