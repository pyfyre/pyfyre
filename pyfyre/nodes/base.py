from browser import document
from abc import ABC, abstractmethod
from pyfyre.events import EventType
from browser import DOMNode, DOMEvent
from typing import Any, Dict, List, Optional, Callable, Union


class Node(ABC):
	def __init__(self) -> None:
		self.dom = self.create_dom()
	
	@abstractmethod
	def create_dom(self) -> DOMNode:
		raise NotImplementedError
	
	def update_dom(self) -> None:
		new_dom = self.create_dom()
		self.dom.replaceWith(new_dom)
		self.dom = new_dom


class Element(Node):
	def __init__(
		self, tag_name: str, *,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		self.tag_name = tag_name
		self.attrs = attrs or {}
		
		self._children_builder = children if callable(children) else None
		self.children = (children() if callable(children) else children) or []
		
		super().__init__()
	
	def create_dom(self) -> DOMNode:
		el = document.createElement(self.tag_name)
		
		for attr_name, attr_value in self.attrs.items():
			el.setAttribute(attr_name, attr_value)
		
		for child in self.children:
			el.appendChild(child.dom)
		
		return el
	
	def update_dom(self) -> None:
		if self._children_builder is not None:
			self.children = self._children_builder()
		
		super().update_dom()
	
	def add_event_listener(
		self, event_type: EventType, callback: Callable[[DOMEvent], None]
	) -> None:
		self.dom.bind(event_type.value, callback)


class TextNode(Node):
	def __init__(self, content: Any) -> None:
		self.content = str(content)
		super().__init__()
	
	def create_dom(self) -> DOMNode:
		return document.createTextNode(self.content)
