from typing import TypeVar, Generic
from pyfyre.utils import EventMixin

T = TypeVar("T")


class State(Generic[T], EventMixin):
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
