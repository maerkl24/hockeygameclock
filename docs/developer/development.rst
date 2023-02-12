Development
===========

Some text ...

Frontend
--------

The ``hockeygameclock`` relies on `Qt <https://www.qt.io/>`_ as frontend and therefore uses the ``PySide6`` Python
binding.

The GUI is developed and designed with help of the `Qt Designer <https://doc.qt.io/qt-6/qtdesigner-manual.html>`_. You
can open the Qt Designer with the following commands:

.. code-block:: batch

    :: Activate virtual environment
    .venv\Scripts\activate.bat

    :: Open Qt Designer
    pyside6-designer

The Qt Designer works with ``.ui`` files to describe the developed GUI. However, to uses these information in
combination with Python, we have to convert them to Python code. This can be done with the following commands:

.. code-block:: batch

    :: Activate virtual environment
    .venv\Scripts\activate.bat

    :: Convert user interface files to Python
    pyside6-uic ui/main_window.ui -o hockeygameclock/frontend/ui/main_window.py --from-imports

    :: Convert resource file to Python
    pyside6-rcc ui/resources.qrc -o hockeygameclock/frontend/ui/resources_rc.py

Backend
-------

Some text ...
