import sys
import typing
from pyfyre.styles import Style
from pyfyre.states import State
from abc import ABC, abstractmethod
from pyfyre.nodes import Node, Element, FutureElement
from typing import Optional, Dict, List, Callable, Awaitable, Any


class Widget(Element, ABC):
	def __init__(self) -> None:
		try:
			el = self.build()
		except BaseException:
			error_children = self.on_build_error(*sys.exc_info())
			el = Element("div", lambda: error_children)
		
		super().__init__(
			el.tag_name, el._children_builder,
			styles=el._styles, states=el.states, attrs=el.attrs
		)
	
	@abstractmethod
	def build(self) -> Element:
		raise NotImplementedError


class FutureWidget(FutureElement, ABC):
	def __init__(
		self, *,
		tag_name: str = "div",
		styles: Optional[List[Style]] = None,
		states: Optional[List[State[Any]]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		async def build() -> List[Element]:
			return [await self.build()]
		
		super().__init__(
			tag_name, typing.cast(Callable[[], Awaitable[List[Node]]], build),
			styles=styles, states=states, attrs=attrs
		)
	
	@abstractmethod
	async def build(self) -> Element:
		raise NotImplementedError
