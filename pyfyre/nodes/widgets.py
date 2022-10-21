import typing
from pyfyre.styles import Style
from abc import ABC, abstractmethod
from pyfyre.nodes import Node, Element, FutureElement
from typing import Optional, Dict, List, Callable, Awaitable


class Widget(Element, ABC):
	def __init__(
		self, *,
		styles: Optional[List[Style]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		super().__init__("div", lambda: [self.build()], styles=styles, attrs=attrs)
	
	@abstractmethod
	def build(self) -> Element:
		raise NotImplementedError


class FutureWidget(FutureElement, ABC):
	def __init__(
		self, *,
		styles: Optional[List[Style]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		async def build() -> List[Element]:
			return [await self.build()]
		
		super().__init__(
			"div", typing.cast(Callable[[], Awaitable[List[Node]]], build),
			styles=styles, attrs=attrs
		)
	
	@abstractmethod
	async def build(self) -> Element:
		raise NotImplementedError
