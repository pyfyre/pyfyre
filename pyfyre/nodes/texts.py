from pyfyre.nodes.base import Node, Element
from typing import Optional, Dict, List, Union, Callable


class Span(Element):
	def __init__(
		self, *,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		super().__init__("span", attrs=attrs, children=children)


class Paragraph(Element):
	def __init__(
		self, *,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		super().__init__("p", attrs=attrs, children=children)
