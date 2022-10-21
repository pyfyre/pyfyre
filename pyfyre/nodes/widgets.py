from pyfyre.styles import Style
from pyfyre.nodes import Element
from abc import ABC, abstractmethod
from typing import Optional, Dict, List


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
