from pyfyre.nodes import Element


class Loading(Element):
    """A loading animation.

    Source: https://loading.io/css/
    """

    def __init__(self) -> None:
        super().__init__(
            "div", lambda: [Element("div") for _ in range(12)], attrs={"class": "lds"}
        )
