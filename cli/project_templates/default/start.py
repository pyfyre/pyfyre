from build import build_app
from livereload import Server

if __name__ == "__main__":
	build_app(verbose=False)
	
	server = Server()
	server.watch("src/*")
	server.watch("public/*")
	server.serve(root="public")
