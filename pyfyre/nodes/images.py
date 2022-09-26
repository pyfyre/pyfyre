from pyfyre.nodes.base import Node, Element
from typing import Optional, Dict, List, Union, Callable


class Image(Element):
	def __init__(
		self, src: str, *,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		attrs = attrs or {}
		attrs["src"] = src
		super().__init__("img", attrs=attrs, children=children)
