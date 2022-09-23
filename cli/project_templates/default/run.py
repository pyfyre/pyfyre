import os
from build import build_app
from livereload import Server

if __name__ == "__main__":
	if os.path.dirname(__file__) == os.getcwd():
		build_app()
		server = Server()
		server.watch("src/*", build_app)
		server.serve(root="public")
	else:
		print("You must be in the directory of the project to run it.")
