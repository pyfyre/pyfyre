from pyfyre.nodes import Node
from typing import Dict, Callable
from browser import window, DOMEvent
from pyfyre.router import RouteManager
from pyfyre.events import PyFyreEventType
from pyfyre.exceptions import PyFyreException
from .states import State, EventState, MediaQuery
from .styles import Style
from .decorators import on_mount, create_effect

__all__ = [
    "PRODUCTION",
    "render",
    "State",
    "EventState",
    "MediaQuery",
    "Style",
    'on_mount',
    'create_effect'
]

_rendered = False
PRODUCTION: bool = False
"""Whether the app is running on production environment or not."""


def _set_custom_window_events() -> Dict[str, DOMEvent]:
    events = {}

    for pyfyre_event in PyFyreEventType:
        event = window.Event.new("Event")
        event.initEvent(pyfyre_event.value, True, True)
        events[pyfyre_event.value] = event

    return events


def render(routes: Dict[str, Callable[..., Node]]) -> None:
    """The main function for initializing a PyFyre application.
    This function can only be called once.

    Args:
        routes: Pairs of route name and its corresponding route builder.
            The route builder returns a ``Node`` that will be rendered on the web page.
            The route builder optionally accepts a single argument.
            The value of the argument may be passed in by a ``RouterLink``.

    Raises:
        PyFyreException: When this function is called again.

    **Example:**

    .. code-block:: python

        RouterLink("/random", arg="A Random Title")

        render({
            "/": lambda: HomePage(),
            "/about": lambda: AboutPage(),
            "/contact": lambda: ContactPage(),
            "/random": lambda title: RandomPage(title)  # The argument defaults to None.
        })
    """

    global _rendered
    if _rendered:
        raise PyFyreException("'render' function can only be called once")
    _rendered = True

    custom_events = _set_custom_window_events()

    RouteManager.initialize(routes)
    RouteManager.render_route(window.location.pathname)
    window.dispatchEvent(custom_events["pyfyreload"])
