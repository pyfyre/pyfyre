import os
import sys
import subprocess
from livereload import Server
from build import export_pyfyre_path

sys.path.append("..")
from pyfyre_cli import web_app


def _make_html() -> None:
    subprocess.run(
        f"{export_pyfyre_path()} && make html",
        shell=True,
    )


if __name__ == "__main__":
    if os.path.dirname(__file__) == os.getcwd():
        subprocess.run(
            "pip install -e .. && "
            f"{export_pyfyre_path()} && "
            "sphinx-apidoc -f -o source ../pyfyre && "
            "make clean html && make html",
            shell=True,
        )

        app = web_app.create_static_flask_app(os.path.join("build", "html"))
        app.debug = True

        server = Server(app.wsgi_app)
        server.watch("source/", _make_html)
        server.serve(port=9050, host="localhost")
    else:
        print("You must be in the directory of pyfyre/docs to run this script.")
