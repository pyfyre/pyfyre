from browser import document
from pyfyre.widgets import BaseWidget
from pyfyre.virtual_dom import VirtualDOM
from pyfyre.exceptions import NodeNotFound

__all__ = [
	"render"
]


def render(root_selector: str, widget: BaseWidget) -> None:
	nodes = document.select(root_selector)
	
	if nodes:
		VirtualDOM.render(nodes[0], widget.dom())
	else:
		raise NodeNotFound(root_selector)
