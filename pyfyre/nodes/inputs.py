from pyfyre.nodes.base import Node, Element
from typing import Optional, Dict, List, Union, Callable


class TextInput(Element):
	def __init__(
		self, *,
		placeholder: str = "",
		multiline: bool = False,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[Union[
			List[Node],
			Callable[[], List[Node]]
		]] = None
	) -> None:
		attrs = attrs or {}
		attrs["type"] = "text"
		attrs["placeholder"] = placeholder
		super().__init__(
			"textarea" if multiline else "input",
			attrs=attrs, children=children
		)


class TextController:
	def __init__(self) -> None:
		raise NotImplementedError
