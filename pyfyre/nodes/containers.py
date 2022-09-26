from pyfyre.nodes.base import Node, Element
from typing import Optional, Dict, List, Union, Callable


class Division(Element):
	def __init__(
		self, *,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		super().__init__("div", attrs=attrs, children=children)
