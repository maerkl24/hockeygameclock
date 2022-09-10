:: Activate virtual environment
call .venv\Scripts\activate.bat

:: Generate Qt user interface Python files
pyside6-uic qt_ui/main_window.ui -o hockeygameclock/frontend/ui/main_window.py --from-imports

:: Generate Qt resource Python file
pyside6-rcc qt_ui/resources.qrc -o hockeygameclock/frontend/ui/resources_rc.py

:: Deactivate virtual environment
call deactivate
