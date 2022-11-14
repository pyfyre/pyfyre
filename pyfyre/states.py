import pyfyre
from abc import ABC
from typing import TypeVar, Generic, Optional
from browser import window, DOMEvent
from pyfyre.utils import EventMixin

T = TypeVar("T")


class StateDependency(ABC, EventMixin):
    """Abstract base class for state dependencies used for rebuilding nodes."""


class State(Generic[T], StateDependency):
    """An object which stores a ``value`` of generic type ``T``.

    This object is used as a state dependency for nodes.

    **Example:**

    .. code-block:: python

        state = State(0)
        state = State[int](0)  # With generic type.

        Element(
            "p",
            lambda: [Text(f"Count: {state.value}")],  # It uses the value of the ``state``.
            states=[state]  # Set the ``state`` as a state dependency for this element.
        )

        state.set_value(1)  # The element will rebuild since it is depending on the ``state``.
    """

    def __init__(self, value: T) -> None:
        super().__init__()
        self._value = value

    @property
    def value(self) -> T:
        """The value of this state object."""
        return self._value

    def set_value(self, value: T) -> None:
        """Set the value and notify the dependers of this state object.

        If the ``value`` is the same, nothing will happen.
        """
        if self._value != value:
            self._value = value
            self.call_listeners()


class EventState(StateDependency):
    """A state which updates whenever the specified ``event_type`` is delivered to the ``target``.
    If the ``target`` is None, will listen to the window instead.

    This object is used as a state dependency for elements.

    Attributes:
        value (Optional[DOMEvent]): Brython ``DOMEvent`` type.
            The event delivered to the ``target``.
            None if the event hasn't been delivered yet.

    **Example:**

    .. code-block:: python

        Element(
            "p",
            lambda: [Text()],
            # The element will rebuild every time the window is scrolled.
            states=[EventState("scroll")]
        )
    """

    def __init__(
        self, event_type: str, target: "Optional[pyfyre.nodes.Element]" = None
    ) -> None:
        self.value: Optional[DOMEvent] = None
        super().__init__()

        def set_value(event: DOMEvent) -> None:
            self.value = event
            self.call_listeners()

        if target is not None:
            target.add_event_listener(event_type, set_value)
        else:
            window.bind(event_type, set_value)


class MediaQuery(StateDependency):
    """A state which updates whenever the media query match has changed its state.

    This is similar to JavaScript ``window.matchMedia``.

    This object is used as a state dependency for elements.

    Args:
        media_query_string: Specifies the media query string to match.

    **Example:**

    .. code-block:: python

        Element(
            "p",
            lambda: [Text()],
            # The element will rebuild every time the media query matches.
            states=[MediaQuery("(max-width: 700px)")]
        )
    """

    def __init__(self, media_query_string: str) -> None:
        super().__init__()
        self._media_query = window.matchMedia(media_query_string)
        self._media_query.addListener(lambda mq: self.call_listeners())

    @property
    def matches(self) -> bool:
        """True if the window currently matches the media query, False otherwise."""
        return bool(self._media_query.matches)
