from enum import Enum
from browser import DOMEvent
from collections import defaultdict
from abc import ABC, abstractmethod
from pyfyre.events import EventType
from typing import Any, Dict, List, Optional, Callable


class WidgetType(Enum):
	Element = "Widget"
	TextNode = "TextWidget"


class BaseWidget(ABC):
	@abstractmethod
	def dom(self) -> Dict[str, Any]:
		raise NotImplementedError


class Widget(BaseWidget):
	def __init__(
		self, tag_name: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		self.tag_name = tag_name
		self.props = props or {}
		self.children = children or []
		self._event_listeners: Dict[EventType, List[Callable[[DOMEvent], None]]] = \
			defaultdict(list)
	
	def dom(self) -> Dict[str, Any]:
		return {
			"_type": WidgetType.Element,
			"tag_name": self.tag_name,
			"props": self.props,
			"children": [c.dom() for c in self.children],
			"event_listeners": self._event_listeners
		}
	
	def add_event_listener(
		self, event_type: EventType, callback: Callable[[DOMEvent], None]
	) -> None:
		self._event_listeners[event_type].append(callback)


class TextWidget(BaseWidget):
	def __init__(self, content: Any):
		self.content = str(content)
	
	def dom(self) -> Dict[str, Any]:
		return {
			"_type": WidgetType.TextNode,
			"content": self.content
		}
