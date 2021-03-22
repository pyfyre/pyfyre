"""Run the app in a live server."""

import sys
from livereload import Server

def run_server(*, port: int):
	server = Server()
	server.watch("src/*")
	server.serve(port=port, host="localhost")

try:
	run_server(port=int(sys.argv[1]))
except IndexError:
	run_server(port=8080)
