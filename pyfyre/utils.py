from typing import List, Callable


class EventMixin:
    """A mixin class which implements event-like functionalities
    to the class inheriting this.
    """

    def __init__(self) -> None:
        self._listeners: List[Callable[[], None]] = []

    def call_listeners(self) -> None:
        """Call all the listeners of this event."""
        for listener in self._listeners:
            listener()

    def add_listener(self, listener: Callable[[], None]) -> None:
        """Add the ``listener`` to this event."""
        self._listeners.append(listener)

    def remove_listener(self, listener: Callable[[], None]) -> int:
        """Remove the ``listener`` to this event.

        Returns:
            The number of listeners removed, which is typically 1,
            unless the ``listener`` was added more than once.
        """
        remaining_listeners = []
        removed = 0

        for c in self._listeners:
            if c == listener:
                removed += 1
            else:
                remaining_listeners.append(c)

        self._listeners = remaining_listeners
        return removed
