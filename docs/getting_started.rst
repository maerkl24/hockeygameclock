Getting Started
===============


Setup Environment
-----------------

.. code-block:: bash

    # Install Python virtual environment
    python -m venv .venv

    # Activate virtual environment
    .venv\Scripts\activate.bat

    # Install Python packages
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt

    # Deactivate virtual environment
    deactivate


Execute Tools
-------------

.. code-block:: bash

    # Activate virtual environment
    .venv\Scripts\activate.bat

    # Format Python code
    yapf --style google -i -r hockeygameclock

    # Lint Python code
    pylint --rcfile pylintrc hockeygameclock

    # Build the docs
    cd docs
    make html

    # Execute Python tests
    pytest tests
