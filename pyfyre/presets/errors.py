import traceback
from typing import Any, Type
from types import TracebackType
from pyfyre.styles import Style
from pyfyre.nodes import Element, Text


class DebugError(Element):
    """An error message with traceback.
    Typically used for debugging on development environment.

    Args:
        exc_type: Type of the exception.
        exc_value: The exception itself.
        exc_traceback: Traceback object which typically encapsulates the
            call stack at the point where the exception last occurred.
    """

    def __init__(
        self,
        exc_type: Type[Exception],
        exc_value: Exception,
        exc_traceback: TracebackType,
    ) -> None:
        tr = traceback.format_exc()
        super().__init__(
            "div",
            lambda: [
                Element(
                    "p",
                    lambda: [Text("Unhandled Runtime Error")],
                    styles=[
                        Style(
                            color="black",
                            font_size="1.5rem",
                            font_weight="bold",
                            margin_top="0",
                            margin_bottom="7px",
                        )
                    ],
                ),
                Element(
                    "span",
                    lambda: [Text(f"{exc_type.__name__}: {exc_value}")],
                    styles=[
                        Style(
                            color="#ff3131",
                            font_weight="bold",
                            font_family="monospace",
                            font_size="0.91rem",
                        )
                    ],
                ),
                Element(
                    "p",
                    lambda: [Text("Traceback")],
                    styles=[
                        Style(
                            color="black",
                            font_size="1.3rem",
                            font_weight="bold",
                            margin_bottom="7px",
                        )
                    ],
                ),
                Element(
                    "p",
                    lambda: [Element("pre", lambda: [Text(tr)])],
                    styles=[
                        Style(
                            background_color="black",
                            color="white",
                            padding="1px 15px",
                            font_size="0.9rem",
                            font_weight="normal",
                        )
                    ],
                ),
            ],
            styles=[
                Style(
                    padding="15px",
                    background_color="white",
                    box_shadow="0 0 10px #888888",
                    border_top="5px solid #ff726f",
                    border_radius="5px",
                    font_family="Arial",
                    display="inline-block",
                )
            ],
        )


class ErrorMessage(Element):
    """A simple error message. Typically used on production environment."""

    def __init__(self, message: Any) -> None:
        super().__init__(
            "div",
            lambda: [
                Element(
                    "p",
                    lambda: [Text(message)],
                    styles=[
                        Style(
                            color="black",
                            font_size="1rem",
                            margin="0",
                            font_weight="bold",
                        )
                    ],
                )
            ],
            styles=[
                Style(
                    padding="15px",
                    background_color="white",
                    box_shadow="0 0 10px #888888",
                    border_top="5px solid #ff726f",
                    border_radius="5px",
                    font_family="Arial",
                    display="inline-block",
                )
            ],
        )
