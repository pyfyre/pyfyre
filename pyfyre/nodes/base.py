import sys
import pyfyre
import traceback
from typing import Type
from browser import document
from types import TracebackType
from pyfyre.styles import Style
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
	
	@abstractmethod
	def html(self) -> str:
		raise NotImplementedError


class Element(Node):
	def __init__(
		self,
		tag_name: str,
		children: Optional[Callable[[], List[Node]]] = None,
		*,
		styles: Optional[List[Style]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		self.tag_name = tag_name
		self.children: List[Node] = []
		self.style = Style.from_styles(styles) if styles else None
		self.attrs = attrs or {}
		self._children_builder = children
		
		def update_style_attr() -> None:
			self.attrs = attrs or {}
			
			if self.style is not None:
				if "style" in self.attrs:
					self.attrs["style"] += f"; {self.style.css()}"
				else:
					self.attrs["style"] = self.style.css()
			
			if getattr(self, "dom", None) is not None:
				self.update_attrs()
		
		if self.style is not None:
			self.style.add_listener(update_style_attr)
			update_style_attr()
		
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
		if pyfyre.PRODUCTION:
			from pyfyre.presets.errors import ErrorMessage
			return [ErrorMessage("An error occurred while loading this element")]
		
		from pyfyre.presets.errors import DebugError
		return [DebugError(
			exc_type=exc_type,
			exc_value=exc_value,
			exc_traceback=traceback.format_exc()
		)]
	
	def build_children(self) -> None:
		self.children = self._secure_build()
		
		for child in self.children:
			self.dom.attach(child.dom)
			
			if isinstance(child, Element):
				child.build_children()
	
	def create_dom(self) -> DOMNode:
		el = document.createElement(self.tag_name)
		
		for attr_name, attr_value in self.attrs.items():
			el.setAttribute(attr_name, attr_value)
		
		return el
	
	def update_dom(self) -> None:
		self.update_attrs()
		self.children = self._secure_build()
		self.dom.replaceChildren(*[c.dom for c in self.children])
		
		for child in self.children:
			child.update_dom()
	
	def update_attrs(self) -> None:
		for attr_name, attr_value in self.attrs.items():
			self.dom.setAttribute(attr_name, attr_value)
	
	def html(self) -> str:
		def attributes() -> str:
			attrs = [
				f'{name}="{value}"'
				for name, value in self.attrs.items()
			]
			return " " + " ".join(attrs) if attrs else ""
		
		result = f"<{self.tag_name}{attributes()}>"
		
		for child in self.children:
			result += child.html()
		
		return result + f"</{self.tag_name}>"
	
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
	
	def html(self) -> str:
		return self.value


E = Element
Text = TextNode
