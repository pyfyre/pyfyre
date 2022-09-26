import sys
from typing import Type
from browser import document
from types import TracebackType
from abc import ABC, abstractmethod
from browser import DOMNode, DOMEvent
from pyfyre.events import BaseEventType
from typing import Any, Dict, List, Optional, Callable, Union


class Node(ABC):
	def __init__(self) -> None:
		self.dom = self.create_dom()
	
	@abstractmethod
	def create_dom(self) -> DOMNode:
		raise NotImplementedError
	
	@abstractmethod
	def update_dom(self) -> None:
		raise NotImplementedError


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
		self.children = (
			self._secure_build() if callable(children) else children
		) or []
		
		super().__init__()
	
	def _secure_build(self) -> List[Node]:
		if self._children_builder is None:
			return self.children
		
		try:
			return self._children_builder()
		except BaseException:
			return self.on_build_error(*sys.exc_info())
	
	def on_build_error(
		self, exc_type: Type[BaseException],
		exc_value: BaseException, exc_traceback: TracebackType
	) -> List[Node]:
		return [
			Element("p", children=[TextNode(exc_type)]),
			Element("p", children=[TextNode(exc_value)]),
			Element("p", children=[TextNode(exc_traceback)])
		]
	
	def create_dom(self) -> DOMNode:
		el = document.createElement(self.tag_name)
		
		for attr_name, attr_value in self.attrs.items():
			el.setAttribute(attr_name, attr_value)
		
		el.replaceChildren(*[c.dom for c in self.children])
		return el
	
	def update_dom(self) -> None:
		for attr_name, attr_value in self.attrs.items():
			self.dom.setAttribute(attr_name, attr_value)
		
		self.children = self._secure_build()
		self.dom.replaceChildren(*[c.dom for c in self.children])
	
	def add_event_listener(
		self, event_type: BaseEventType, callback: Callable[[DOMEvent], None]
	) -> None:
		self.dom.bind(event_type.value, callback)


class TextNode(Node):
	def __init__(self, value: Any) -> None:
		self._value = str(value)
		super().__init__()
	
	@property
	def value(self) -> str:
		return self._value
	
	def set_value(self, value: Any) -> None:
		self._value = str(value)
	
	def create_dom(self) -> DOMNode:
		return document.createTextNode(self.value)
	
	def update_dom(self) -> None:
		self.dom.nodeValue = self.value
