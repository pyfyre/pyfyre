from browser import DOMEvent
from pyfyre.events import MouseEventType
from pyfyre.nodes.base import Node, Element
from typing import Callable, Optional, Dict, List


class Button(Element):
	def __init__(
		self,
		onclick: Callable[[DOMEvent], None],
		children: Optional[Callable[[], List[Node]]] = None,
		*,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		super().__init__("button", children, attrs=attrs)
		self.add_event_listener(MouseEventType.Click, onclick)
