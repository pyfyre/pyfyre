from enum import Enum
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class WidgetType(Enum):
	Element = "Widget"
	TextNode = "TextWidget"


class BaseWidget(ABC):
	@abstractmethod
	def dom(self) -> Dict[str, Any]:
		pass


class Widget(BaseWidget):
	def __init__(
		self, tag_name: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		self.tag_name = tag_name
		self.props = props or {}
		self.children = children or []
	
	def dom(self) -> Dict[str, Any]:
		return {
			"_type": WidgetType.Element,
			"tag_name": self.tag_name,
			"props": self.props,
			"children": [c.dom() for c in self.children]
		}


class TextWidget(BaseWidget):
	def __init__(self, content: str):
		self.content = content
	
	def dom(self) -> Dict[str, Any]:
		return {
			"_type": WidgetType.TextNode,
			"content": self.content
		}
