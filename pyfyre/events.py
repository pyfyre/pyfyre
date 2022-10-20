from enum import Enum
from typing import Callable
from browser import DOMEvent, window


class PyFyreEventType(Enum):
	pyfyreload = "pyfyreload"


def window_event_listener(
	event_type: str
) -> Callable[[Callable[[DOMEvent], None]], Callable[[DOMEvent], None]]:
	def window_event_listener_decorator(
		callback: Callable[[DOMEvent], None]
	) -> Callable[[DOMEvent], None]:
		window.bind(event_type, callback)
		return callback
	
	return window_event_listener_decorator
