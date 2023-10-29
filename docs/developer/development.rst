Development
===========

Some text ...

Frontend
--------

The ``hockeygameclock`` relies on `Qt <https://www.qt.io/>`_ as frontend and therefore uses the ``PySide6`` Python
binding.

The GUI is developed and designed with help of the `Qt Designer <https://doc.qt.io/qt-6/qtdesigner-manual.html>`_. You
can open the Qt Designer with the following command:

.. code-block:: shell

    # Open the Qt Designer
    pdm run pyside6-designer

    # Open the Qt Designer for a specific .ui file
    pdm run pyside6-designer ui/clock_widget.ui

The Qt Designer works with ``.ui`` files to describe the developed GUI. However, to uses these information in
combination with Python, we have to convert them to Python code. This can be done with the following commands:

.. code-block:: shell

    # Convert user interface files to Python
    pdm run pyside6-uic ui/clock_widget.ui -o hockeygameclock/frontend/generated/clock_widget.py --from-imports

    # Convert resource file to Python
    # pdm run pyside6-rcc ui/resources.qrc -o hockeygameclock/frontend/ui/resources_rc.py

Backend
-------

Some text ...
