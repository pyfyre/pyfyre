"""
This module creates a PyFyre project in the `__dev__` directory.
This starts a live server hosting the `__dev__/_pyfyre` directory.
The live server watches for changes in the
`pyfyre` and `pyfyre_cli` directories.
When the live server detects changes, it will recreate the `__dev__` app.

This is useful to quickly test your changes while developing this project
on your local environment.
"""

import os
import importlib
from livereload import Server
from pyfyre_cli import utils
from pyfyre_cli import create_app
from pyfyre_cli import web_app


def _create_app() -> None:
    # Reload modules for possible changes
    importlib.reload(utils)
    importlib.reload(create_app)
    importlib.reload(web_app)

    create_app.create_app("__dev__", os.getcwd(), dev_mode=True)

    with utils.in_path("__dev__"):
        from pyfyre_cli import build_app

        importlib.reload(build_app)
        build_app.build_app()


if __name__ == "__main__":
    if os.path.dirname(__file__) == os.getcwd():
        _create_app()

        app = web_app.create_static_flask_app(os.path.join("__dev__", "_pyfyre"))
        app.debug = True

        server = Server(app.wsgi_app)
        server.watch("pyfyre/", _create_app)
        server.watch("pyfyre_cli/", _create_app)
        server.serve(port=8080, host="localhost")
    else:
        print("You must be in the directory of pyfyre to run the development server.")
