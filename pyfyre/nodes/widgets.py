from pyfyre.styles import Style
from pyfyre.states import State
from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Any
from pyfyre.nodes import Node, Element, FutureElement


class Widget(Element, ABC):
    def __init__(
        self,
        *,
        tag_name: str = "div",
        styles: Optional[List[Style]] = None,
        states: Optional[List[State[Any]]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(
            tag_name, self.build, styles=styles, states=states, attrs=attrs
        )

    @abstractmethod
    def build(self) -> List[Node]:
        raise NotImplementedError


class FutureWidget(FutureElement, ABC):
    def __init__(
        self,
        *,
        tag_name: str = "div",
        styles: Optional[List[Style]] = None,
        states: Optional[List[State[Any]]] = None,
        attrs: Optional[Dict[str, str]] = None
    ) -> None:
        super().__init__(
            tag_name, self.build, styles=styles, states=states, attrs=attrs
        )

    @abstractmethod
    async def build(self) -> List[Node]:
        raise NotImplementedError
