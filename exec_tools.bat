:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Sort imports
isort hockeyclock
isort tests

:: Format Python code
black hockeyclock
black tests

:: Lint Python code
pylint hockeyclock
pylint tests

:: Type check Python code
mypy hockeyclock
mypy tests

:: Execute Python tests and measure coverage
pytest

:: Build the docs
cd docs
call make html
cd ..

:: Deactivate virtual environment
call deactivate
