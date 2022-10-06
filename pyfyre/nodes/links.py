from pyfyre.events import MouseEventType
from pyfyre.nodes.base import Node, Element
from browser import DOMEvent, window, document
from typing import Optional, Dict, List, Callable


class Anchor(Element):
	def __init__(
		self,
		href: str,
		children: Optional[Callable[[], List[Node]]] = None,
		*,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		self.href = href
		attrs = attrs or {}
		attrs["href"] = href
		
		super().__init__("a", children, attrs=attrs)
		
		if self.is_internal():
			def change_route(event: DOMEvent) -> None:
				# Import here due to cicular import problem
				from pyfyre.router import RouteManager
				
				window.history.pushState(None, None, self.absolute_href)
				event.preventDefault()
				RouteManager.change_route(href)
			
			self.add_event_listener(MouseEventType.Click, change_route)
	
	@property
	def absolute_href(self) -> str:
		el = document.createElement("a")
		el.href = self.href
		return el.href
	
	def is_internal(self) -> bool:
		el = document.createElement("a")
		el.href = self.href
		return bool(el.host == window.location.host)
