from typing import Any


class EmptyObject:
    def __init__(self, class_name: str) -> None:
        self.class_name = class_name
        self.__qualname__ = class_name

    def __getattr__(self, attr: str) -> Any:
        return EmptyObject(attr)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return EmptyObject("")

    def __getitem__(self, key: str) -> Any:
        return EmptyObject(key)

    def __str__(self) -> str:
        return self.class_name

    def __add__(self, other: str) -> str:
        return str(self) + other

    def __radd__(self, other: str) -> str:
        return other + str(self)


Interpreter = EmptyObject("Interpreter")
Inspector = EmptyObject("Inspector")
