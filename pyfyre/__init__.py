from pyfyre.nodes import Node
from typing import Dict, Callable
from browser import document, window
from pyfyre.router import RouteManager
from pyfyre.exceptions import PyFyreException, NodeNotFound

__all__ = [
	"render",
	"PRODUCTION"
]

_rendered = False
PRODUCTION: bool = False


def render(root_selector: str, routes: Dict[str, Callable[[], Node]]) -> None:
	global _rendered
	if _rendered:
		raise PyFyreException("'render' function can only be called once")
	_rendered = True
	
	nodes = document.select(root_selector)
	if nodes:
		RouteManager.set_routes(routes)
		RouteManager.root_node = nodes[0]
		RouteManager.render_route(window.location.pathname)
	else:
		raise NodeNotFound(root_selector)
