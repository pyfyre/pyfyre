from typing import List, Optional
from pyfyre.utils import EventMixin


class Style(EventMixin):
    """Provides styling to elements.

    Args:
        **props: CSS properties but the hyphens (-) are replaced by underscores (_).
            The values are unchanged.

    Attributes:
        props (Dict[str, str]): Packed form of the ``**props`` argument.

    **Example:**

    .. code-block:: python

        theme = Style(background_color="gray")

        Element(
            "p",
            lambda: [Text("PyFyre is amazing!")],
            styles=[theme]  # Sets the background color of the element to gray.
        )

        theme["background_color"]  # Returns "gray".
        theme["background_color"] = "black"  # Change the background color of the element to black.
        del theme["background_color"]  # Remove the background color styling of the element.
    """

    @classmethod
    def from_styles(cls, styles: List["Style"], *, dynamic: bool = True) -> "Style":
        """Construct a ``Style`` object from multiple ``Style`` objects.
        The styles are evaluated in order from left to right.

        Args:
            dynamic: If True, the constructed ``Style`` object will listen
                to the changes of the ``styles``.
                That means if one of the ``styles`` is updated,
                the constructed ``Style`` object will also get updated.
                If False, the constructed ``Style`` object will not
                listen to the changes of the ``styles``.
        """

        s = Style()
        props = {}

        def update_style() -> None:
            s.props = Style.from_styles(styles, dynamic=False).props.copy()
            s.call_listeners()

        for style in styles:
            for prop, value in style.props.items():
                props[prop] = value

            if dynamic:
                style.add_listener(update_style)

        s.props = props
        return s

    def __init__(self, **props: str) -> None:
        super().__init__()
        self.props = props

    def __getitem__(self, prop: str) -> Optional[str]:
        return self.props.get(prop)

    def __setitem__(self, prop: str, value: str) -> None:
        self.props[prop] = value
        self.call_listeners()

    def __delitem__(self, prop: str) -> None:
        del self.props[prop]
        self.call_listeners()

    def css(self) -> str:
        """CSS representation of this object."""
        return "; ".join(
            [f"{prop.replace('_', '-')}: {value}" for prop, value in self.props.items()]
        )
