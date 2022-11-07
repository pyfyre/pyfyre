Quick Start
===========

Prerequisites
-------------
- Python 3.x (3.9+ is recommended)

Installation
------------
In order to create and build PyFyre projects, you need to install the PyFyre CLI.
To install the PyFyre CLI, open a terminal window (cmd on Windows) and run the following command:

.. code-block:: bash
   
   pip install pyfyre

To verify if your installation is successful, run the following command:

.. code-block:: bash
   
   pyfyre help

Creating a PyFyre Project
-------------------------
To create a new PyFyre project, run the following command:

.. code-block:: bash
   
   pyfyre create my-cool-app

You can replace `my-cool-app` with the name of the project you desire.

Running a PyFyre Application
----------------------------
1. Navigate to your project directory (`my-cool-app` in our case) by running the following command:

.. code-block:: bash
   
   cd my-cool-app

2. Finally, run your app:

.. code-block:: bash
   
   pyfyre run

And voila! You now have a running PyFyre app on your local machine.
You can visit your app on your browser at ``http:localhost:8080``.

The source code of the app is inside the ``src/index.py`` file.
You may start making changes there and see it reflect on your browser.

The ``run`` command starts a development server with live reload that detects changes in the code and reloads the application automatically.

.. note::
   Once you have run the app, PyFyre will generate a folder called `_pyfyre`. The folder contains all the files the running server needs. You can safely delete it after the server has been stopped.
