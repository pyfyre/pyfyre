from typing import Dict
from pyfyre.nodes import Node
from browser import document, window
from pyfyre.router import RouteManager
from pyfyre.exceptions import NodeNotFound

__all__ = [
	"render"
]


def render(root_selector: str, routes: Dict[str, Node]) -> None:
	RouteManager.routes = routes
	nodes = document.select(root_selector)
	
	if nodes:
		RouteManager.root_node = nodes[0]
		RouteManager.render_route(window.location.pathname)
	else:
		raise NodeNotFound(root_selector)
