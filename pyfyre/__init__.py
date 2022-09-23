from typing import Dict
from browser import document, window
from pyfyre.widgets import BaseWidget
from pyfyre.router import RouteManager
from pyfyre.virtual_dom import VirtualDOM
from pyfyre.exceptions import NodeNotFound

__all__ = [
	"render"
]


def render(root_selector: str, routes: Dict[str, BaseWidget]) -> None:
	RouteManager.routes = routes
	nodes = document.select(root_selector)
	
	if nodes:
		VirtualDOM.root = nodes[0]
		widget = RouteManager.get_widget(window.location.pathname)
		VirtualDOM.render(widget.dom())
	else:
		raise NodeNotFound(root_selector)
