from typing import Optional, Dict, List
from pyfyre.widgets.base import Widget, BaseWidget


class TextInput(Widget):
	def __init__(
		self, *,
		placeholder: str = "",
		multiline: bool = False,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		props = props or {}
		props["placeholder"] = placeholder
		super().__init__(
			"textarea" if multiline else "input",
			props=props, children=children
		)


class TextController:
	def __init__(self) -> None:
		raise NotImplementedError
