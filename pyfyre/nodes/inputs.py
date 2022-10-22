from pyfyre.styles import Style
from pyfyre.states import State
from pyfyre.nodes.base import Node, Element
from typing import Any, Callable, Optional, Dict, List


class TextInput(Element):
	def __init__(
		self,
		children: Optional[Callable[[], List[Node]]] = None, *,
		placeholder: str = "",
		multiline: bool = False,
		styles: Optional[List[Style]] = None,
		states: Optional[List[State[Any]]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		attrs = attrs or {}
		attrs["placeholder"] = placeholder
		
		super().__init__(
			"textarea" if multiline else "input",
			children, styles=styles, states=states, attrs=attrs
		)
	
	@property
	def value(self) -> str:
		return str(self.dom.value)
	
	def set_value(self, value: Any) -> None:
		self.dom.value = str(value)
		self.update_dom()
