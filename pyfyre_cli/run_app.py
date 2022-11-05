from livereload import Server
from pyfyre_cli.web_app import create_static_flask_app
from pyfyre_cli.build_app import build_app, bundle_scripts, create_pages


def run_app() -> None:
    """Builds the app in the `_pyfyre` directory and starts a live server hosting that directory.
    The live server watches for changes in the `public` and `src` directories,
    as well as the `settings.py` and `template.html` files.
    When the live server detects changes, it will rebuild the app.
    """
    build_app()

    app = create_static_flask_app("_pyfyre")
    app.debug = True

    server = Server(app.wsgi_app)
    server.watch("public/", build_app)
    server.watch("src/", lambda: bundle_scripts(production=False))
    server.watch("settings.py", build_app)
    server.watch("template.html", lambda: create_pages(production=False))
    server.serve()
