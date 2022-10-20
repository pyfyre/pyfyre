from browser import DOMEvent
from pyfyre.styles import Style
from pyfyre.events import ElementEventType
from pyfyre.nodes.base import Node, Element
from typing import Callable, Optional, Dict, List


class Button(Element):
	def __init__(
		self,
		onclick: Callable[[DOMEvent], None],
		children: Optional[Callable[[], List[Node]]] = None,
		*,
		styles: Optional[List[Style]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		super().__init__("button", children, styles=styles, attrs=attrs)
		self.add_event_listener(ElementEventType.click, onclick)
