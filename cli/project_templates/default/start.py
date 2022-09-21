from livereload import Server
from build import build_app as app_builder


def build_app() -> None:
	app_builder(verbose=False)


if __name__ == "__main__":
	build_app()
	server = Server()
	server.watch("src/*", build_app)
	server.watch("public/*", build_app)
	server.serve(root="public")
