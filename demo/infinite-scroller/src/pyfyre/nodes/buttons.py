from browser import DOMEvent
from pyfyre.events import MouseEventType
from pyfyre.nodes.base import Node, Element
from typing import Callable, Optional, Dict, List, Union


class Button(Element):
	def __init__(
		self, onclick: Callable[[DOMEvent], None], *,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		super().__init__("button", attrs=attrs, children=children)
		self.add_event_listener(MouseEventType.Click, onclick)
