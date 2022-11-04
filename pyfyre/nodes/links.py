from pyfyre.styles import Style
from pyfyre.states import State
from pyfyre.nodes.base import Node, Element
from browser import DOMEvent, window, document
from typing import Optional, Dict, List, Callable, Any


class Link(Element):
    """Represents an HTML ``<a>``.

    Args:
        href: Hyperlink of the page the link goes to.

    Attributes:
        href (str): Hyperlink of the page the link goes to.
    """

    def __init__(
        self,
        href: str,
        children: Optional[Callable[[], List[Node]]] = None,
        *,
        styles: Optional[List[Style]] = None,
        states: Optional[List[State[Any]]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        self.href = href
        attrs = attrs or {}
        attrs["href"] = href
        super().__init__("a", children, styles=styles, states=states, attrs=attrs)

    @property
    def url(self) -> str:
        """URL of the page the link goes to."""
        el = document.createElement("a")
        el.href = self.href
        return el.href

    def is_internal(self) -> bool:
        """Whether the href is linked within the same domain."""
        el = document.createElement("a")
        el.href = self.href
        return bool(el.host == window.location.host)


class RouterLink(Link):
    """Navigates to a different route inside the website as a single-page application."""

    def __init__(
        self,
        href: str,
        children: Optional[Callable[[], List[Node]]] = None,
        *,
        styles: Optional[List[Style]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(href, children, styles=styles, attrs=attrs)

        def change_route(event: DOMEvent) -> None:
            # Import here due to cicular import problem
            from pyfyre.router import RouteManager

            window.history.pushState(None, None, self.url)
            event.preventDefault()
            RouteManager.change_route(href)

        self.add_event_listener("click", change_route)
