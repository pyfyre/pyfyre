from typing import List, Callable


class EventMixin:
    """:meta private:"""

    def __init__(self) -> None:
        self._listeners: List[Callable[[], None]] = []

    def call_listeners(self) -> None:
        for listener in self._listeners:
            listener()

    def add_listener(self, listener: Callable[[], None]) -> None:
        self._listeners.append(listener)

    def remove_listener(self, listener: Callable[[], None]) -> int:
        remaining_listeners = []
        removed = 0

        for c in self._listeners:
            if c == listener:
                removed += 1
            else:
                remaining_listeners.append(c)

        self._listeners = remaining_listeners
        return removed
