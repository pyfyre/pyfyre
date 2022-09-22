from browser import DOMEvent
from pyfyre.events import MouseEventType
from typing import Callable, Optional, Dict, List
from pyfyre.widgets.base import Widget, BaseWidget


class Button(Widget):
	def __init__(
		self, onclick: Callable[[DOMEvent], None], *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		super().__init__("button", props=props, children=children)
		self.add_event_listener(MouseEventType.Click, onclick)
