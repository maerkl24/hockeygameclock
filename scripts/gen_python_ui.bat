:: Move to project root
pushd %~dp0..

:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Generate Qt user interface Python files
pyside6-uic ui/main_window.ui -o hockeygameclock/frontend/ui/main_window.py --from-imports

:: Generate Qt resource Python file
pyside6-rcc ui/resources.qrc -o hockeygameclock/frontend/ui/resources_rc.py

:: Deactivate virtual environment
call deactivate

:: Move back
popd
