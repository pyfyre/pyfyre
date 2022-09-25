from typing import Optional, Dict, List
from pyfyre.events import MouseEventType
from browser import DOMEvent, window, document
from pyfyre.widgets.base import Widget, BaseWidget


class Link(Widget):
	def __init__(
		self, href: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		props = props or {}
		props["href"] = href
		super().__init__("a", props=props, children=children)
		
		self.href = href
		
		def prevent_leaving_page(event: DOMEvent) -> None:
			# Import here due to cicular import problem
			from pyfyre.router import RouteManager
			
			window.history.pushState(None, None, href)
			event.preventDefault()
			RouteManager.change_route(href)
		
		if self.is_internal():
			self.add_event_listener(MouseEventType.Click, prevent_leaving_page)
	
	def is_internal(self) -> bool:
		el = document.createElement("a")
		el.href = self.href
		return el.host == window.location.host
