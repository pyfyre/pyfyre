from pyfyre.events import MouseEventType
from pyfyre.nodes.base import Element


class Button(Element):
	def __init__(
		self,
		onclick,
		children = None,
		*,
		attrs = None
	) -> None:
		super().__init__("button", children, attrs=attrs)
		self.add_event_listener(MouseEventType.Click, onclick)
