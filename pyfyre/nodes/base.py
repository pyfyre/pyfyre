import sys
import traceback
from typing import Type
from types import TracebackType
from browser import document, aio
from abc import ABC, abstractmethod
from browser import DOMNode, DOMEvent
from pyfyre.events import BaseEventType
from typing import Any, Dict, List, Optional, Callable


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
		self,
		tag_name: str,
		children: Optional[Callable[[], List[Node]]] = None,
		*,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		self.tag_name = tag_name
		self.children: List[Node] = []
		self.attrs = attrs or {}
		self._children_builder = children
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
		tr = traceback.format_exc()
		return [
			Element(
				"div",
				lambda: [
					Element("p", lambda: [TextNode("Unhandled Runtime Error")], attrs={
						"style": "color: black; font-size: 1.5rem; font-weight: bold; "
						"margin-top: 0; margin-bottom: 7px;"
					}),
					Element(
						"span", lambda: [TextNode(f"{exc_type.__name__}: {exc_value}")],
						attrs={
							"style": "color: #ff3131; font-weight: bold; "
							"font-family: monospace; font-size: 0.91rem;"
						}
					),
					Element("p", lambda: [TextNode("Traceback")], attrs={
						"style": "color: black; font-size: 1.3rem; font-weight: bold; "
						"margin-bottom: 7px;"
					}),
					Element(
						"p",
						lambda: [Element("pre", lambda: [TextNode(tr)])],
						attrs={
							"style": "background-color: black; color: white; "
							"padding: 1px 15px"
						}
					)
				],
				attrs={
					"style": "padding: 15px; background-color: white; "
					"box-shadow: 0 0 10px #888888; border-top: 5px solid #ff726f; "
					"border-radius: 5px; font-family: Arial;"
				}
			)
		]
	
	async def build_children(self) -> None:
		self.children = self._secure_build()
		
		for child in self.children:
			self.dom.appendChild(child.dom)
			await aio.sleep(0)
		
		for child in self.children:
			if isinstance(child, Element):
				await child.build_children()
	
	def create_dom(self) -> DOMNode:
		el = document.createElement(self.tag_name)
		
		for attr_name, attr_value in self.attrs.items():
			el.setAttribute(attr_name, attr_value)
		
		return el
	
	def update_dom(self) -> None:
		for attr_name, attr_value in self.attrs.items():
			self.dom.setAttribute(attr_name, attr_value)
		
		self.children = self._secure_build()
		self.dom.replaceChildren(*[c.dom for c in self.children])
		
		for child in self.children:
			child.update_dom()
	
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
