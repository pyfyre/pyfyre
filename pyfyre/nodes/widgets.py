from types import TracebackType
from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Any, Type
from pyfyre.styles import Style
from pyfyre.states import State
from pyfyre.nodes import Node, Element, FutureElement


class Widget(Element, ABC):
    """User-defined ``Element`` class.

    Inherit this class if you wish to define your own ``Element`` class.

    **Example:**

    .. code-block:: python

        class MyElement(Widget):
            def build(self) -> list[Node]:
                return [Element("p", lambda: [Text("Hello, World!")])]
    """

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
        """Builder for the children nodes of this element.

        This is an abstract method so you must override this and define its implementation.
        """
        raise NotImplementedError

    def on_build_error(
        self,
        exc_type: Type[Exception],
        exc_value: Exception,
        exc_traceback: TracebackType,
    ) -> List[Node]:
        """Error handler for the ``build`` method.

        This replaces the ``build`` method as the children builder for this element
        if an error occurred inside the ``build`` method.

        You may override this method to customize your error message.

        Args:
            exc_type: Type of the exception.
            exc_value: The exception itself.
            exc_traceback: Traceback object which typically encapsulates the
                call stack at the point where the exception last occurred.

        Returns:
            By default, a simple error message on production environment
            and a traceback message on development environment.
        """
        return super().on_build_error(exc_type, exc_value, exc_traceback)


class FutureWidget(FutureElement, ABC):
    """User-defined ``FutureElement`` class.

    Inherit this class if you wish to define your own ``FutureElement`` class.

    **Example:**

    .. code-block:: python

        class MyFutureElement(FutureWidget):
            async def build(self) -> list[Node]:
                return await ...  # asynchronous operation
    """

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
        """Asynchronous builder for the children nodes of this Future element.

        This is an abstract method so you must override this and define its implementation.

        Error handling for the ``build`` method is currently not yet supported.
        """
        raise NotImplementedError

    def while_no_result(self) -> List[Node]:
        """Initial children builder for this element
        while the result of the Future is not yet ready.

        You may override this method to customize your loading message.

        Returns:
            By default, a loading animation.
        """
        return super().while_no_result()
