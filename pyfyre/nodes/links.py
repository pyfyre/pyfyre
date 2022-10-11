from pyfyre.events import MouseEventType
from pyfyre.nodes.base import Element
from browser import window, document


class Anchor(Element):
	def __init__(
		self,
		href: str,
		children = None,
		*,
		attrs = None
	) -> None:
		self.href = href
		attrs = attrs or {}
		attrs["href"] = href
		super().__init__("a", children, attrs=attrs)
	
	@property
	def absolute_href(self) -> str:
		el = document.createElement("a")
		el.href = self.href
		return el.href
	
	def is_internal(self) -> bool:
		el = document.createElement("a")
		el.href = self.href
		return bool(el.host == window.location.host)


class RouterLink(Anchor):
	def __init__(
		self,
		href: str,
		children = None,
		*,
		attrs = None
	) -> None:
		super().__init__(href, children, attrs=attrs)
		
		def change_route(event) -> None:
			# Import here due to cicular import problem
			from pyfyre.router import RouteManager
			
			window.history.pushState(None, None, self.absolute_href)
			event.preventDefault()
			RouteManager.change_route(href)
		
		self.add_event_listener(MouseEventType.Click, change_route)
