from browser import document, window
from pyfyre.router import RouteManager
from pyfyre.exceptions import NodeNotFound

__all__ = [
	"render",
	"PRODUCTION"
]

PRODUCTION: bool = False


def render(root_selector: str, routes) -> None:
	nodes = document.select(root_selector)
	
	if nodes:
		RouteManager.set_routes(routes)
		RouteManager.root_node = nodes[0]
		RouteManager.render_route(window.location.pathname)
	else:
		raise NodeNotFound(root_selector)
