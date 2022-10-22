import typing
from pyfyre.styles import Style
from pyfyre.states import State
from abc import ABC, abstractmethod
from pyfyre.nodes import Node, Element, FutureElement
from typing import Optional, Dict, List, Callable, Awaitable, Any


class Widget(Element, ABC):
	def __init__(
		self, *,
		styles: Optional[List[Style]] = None,
		states: Optional[List[State[Any]]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		super().__init__(
			"div", lambda: [self.build()],
			styles=styles, states=states, attrs=attrs
		)
	
	@abstractmethod
	def build(self) -> Element:
		raise NotImplementedError


class FutureWidget(FutureElement, ABC):
	def __init__(
		self, *,
		styles: Optional[List[Style]] = None,
		states: Optional[List[State[Any]]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		async def build() -> List[Element]:
			return [await self.build()]
		
		super().__init__(
			"div", typing.cast(Callable[[], Awaitable[List[Node]]], build),
			styles=styles, states=states, attrs=attrs
		)
	
	@abstractmethod
	async def build(self) -> Element:
		raise NotImplementedError
