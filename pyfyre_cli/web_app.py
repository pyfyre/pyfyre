import os
from flask import Flask, send_from_directory, Response


def create_static_flask_app(directory: str) -> Flask:
    app = Flask(__name__, root_path=os.path.abspath(directory))

    @app.route("/", defaults={"filename": "index.html"})
    @app.route("/<path:filename>")
    def index(filename: str) -> Response:
        target = os.path.join(directory, *filename.split("/"))

        if os.path.isfile(target):
            return send_from_directory(".", filename)

        return send_from_directory(".", os.path.join(filename, "index.html"))

    return app
