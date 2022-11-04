from browser import DOMEvent
from pyfyre.styles import Style
from pyfyre.states import State
from pyfyre.nodes.base import Node, Element
from typing import Callable, Optional, Dict, List, Any


class Button(Element):
    """Represents an HTML ``<button>``.

    Args:
        onclick: Called when this button is clicked.
    """

    def __init__(
        self,
        onclick: Callable[[DOMEvent], None],
        children: Optional[Callable[[], List[Node]]] = None,
        *,
        styles: Optional[List[Style]] = None,
        states: Optional[List[State[Any]]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__("button", children, styles=styles, states=states, attrs=attrs)
        self.add_event_listener("click", onclick)
