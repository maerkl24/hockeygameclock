Getting Started
===============

You would like to develop and contribute to this project? Then this chapter is what you were looking for.

The recommended IDE is `Visual Studio Code <https://code.visualstudio.com/>`_.

Install PDM
-----------

This project uses PDM as Python package and dependency manager. In order to develop on this project, it is recommended
to install PDM. For more information, check the `PDM installation guide <https://pdm.fming.dev/latest/#installation>`_.

Install JAVA
------------

If you want to build the documentation, JAVA is needed in order to generate the Plantuml diagrams. For more information,
check the `Java download guide <https://www.java.com/en/download/>`_.

Install Development Tools
-------------------------

To install the Python dependencies and all the development tools, execute the following command:

.. code-block:: shell

    pdm install --dev

Execute Development Tools
-------------------------

To execute the formatter, run the following commands:

.. code-block:: shell

    pdm run isort hockeygameclock
    pdm run isort tests
    pdm run black hockeygameclock
    pdm run black tests

To execute the linter, run the following commands:

.. code-block:: shell

    pdm run pylint hockeygameclock
    pdm run pylint tests
    pdm run mypy hockeygameclock
    pdm run mypy tests

To execute the tests, run the following commands:

.. code-block:: shell

    pdm run pytest

To build the documentation, run the following commands:

.. code-block:: shell

    cd docs
    pdm run make html
