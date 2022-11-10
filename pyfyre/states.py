import pyfyre
from abc import ABC
from typing import TypeVar, Generic, Optional
from browser import window
from pyfyre.utils import EventMixin

T = TypeVar("T")


class BaseState(ABC, EventMixin):
    """Abstract base class for state dependencies used for rebuilding nodes."""


class State(Generic[T], BaseState):
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


class EventState(BaseState):
    """A state which changes state whenever the specified
    ``event_type`` is delivered to the ``target``.
    If the ``target`` is None, will listen to the window instead.

    This object is used as a state dependency for elements.

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
        super().__init__()

        if target is not None:
            target.add_event_listener(event_type, lambda ev: self.call_listeners())
        else:
            window.bind(event_type, lambda ev: self.call_listeners())
