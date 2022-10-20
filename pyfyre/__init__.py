from pyfyre.nodes import Node
from typing import Dict, Callable
from pyfyre.router import RouteManager
from pyfyre.events import PyFyreEventType
from browser import document, window, DOMEvent
from pyfyre.exceptions import PyFyreException, NodeNotFound

__all__ = [
	"render",
	"PRODUCTION"
]

_rendered = False
PRODUCTION: bool = False


def _set_custom_window_events() -> Dict[str, DOMEvent]:
	events = {}
	
	for pyfyre_event in PyFyreEventType:
		event = window.Event.new("Event")
		event.initEvent(pyfyre_event.value, True, True)
		events[pyfyre_event.value] = event
	
	return events


def render(root_selector: str, routes: Dict[str, Callable[[], Node]]) -> None:
	global _rendered
	if _rendered:
		raise PyFyreException("'render' function can only be called once")
	_rendered = True
	
	custom_events = _set_custom_window_events()
	node = document.select_one(root_selector)
	
	if node is not None:
		RouteManager.initialize(node, routes)
		RouteManager.render_route(window.location.pathname)
		window.dispatchEvent(custom_events["pyfyreload"])
	else:
		raise NodeNotFound(root_selector)
