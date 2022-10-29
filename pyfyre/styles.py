from typing import List, Optional
from pyfyre.utils import EventMixin


class Style(EventMixin):
    @classmethod
    def from_styles(cls, styles: List["Style"], *, dynamic: bool = True) -> "Style":
        """
        If [dynamic] is `True`, if one of the [styles] is updated,
        this [Style] will also update.
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
        return "; ".join(
            [f"{prop.replace('_', '-')}: {value}" for prop, value in self.props.items()]
        )
