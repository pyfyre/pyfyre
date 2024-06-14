import pyfyre
from abc import ABC
from typing import TypeVar, Generic, Optional
from browser import window, DOMEvent
from pyfyre.utils import EventMixin

T = TypeVar("T")


class ReferenceDependency(ABC, EventMixin):
    """Abstract base class for state dependencies used for rebuilding nodes."""


class NodeRef(Generic[T], ReferenceDependency):
    
    def __init__(self, value: T) -> None:
        super().__init__()
        self._node = value

    @property
    def node(self):
        return self._node

CreateRef = NodeRef