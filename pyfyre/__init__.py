from pyfyre.nodes import Node
from typing import Dict, Callable
from browser import window, DOMEvent
from pyfyre.router import RouteManager
from pyfyre.events import PyFyreEventType
from pyfyre.exceptions import PyFyreException
from .states import State
from .styles import Style

__all__ = ["PRODUCTION", "render", "State", "Style"]

_rendered = False
PRODUCTION: bool = False


def _set_custom_window_events() -> Dict[str, DOMEvent]:
    events = {}

    for pyfyre_event in PyFyreEventType:
        event = window.Event.new("Event")
        event.initEvent(pyfyre_event.value, True, True)
        events[pyfyre_event.value] = event

    return events


def render(routes: Dict[str, Callable[[], Node]]) -> None:
    global _rendered
    if _rendered:
        raise PyFyreException("'render' function can only be called once")
    _rendered = True

    custom_events = _set_custom_window_events()

    RouteManager.initialize(routes)
    RouteManager.render_route(window.location.pathname)
    window.dispatchEvent(custom_events["pyfyreload"])
