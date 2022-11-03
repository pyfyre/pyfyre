from typing import TypeVar, Generic
from pyfyre.utils import EventMixin

T = TypeVar("T")


class State(Generic[T], EventMixin):
    def __init__(self, value: T) -> None:
        super().__init__()
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    def set_value(self, value: T) -> None:
        if self._value != value:
            self._value = value
            self.call_listeners()
