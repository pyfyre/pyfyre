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


import_js: Any = EmptyObject("import_js")
py2js: Any = EmptyObject("py2js")
this: Any = EmptyObject("this")
Date: Any = EmptyObject("Date")
JSON: Any = EmptyObject("JSON")
Math: Any = EmptyObject("Math")
NULL: Any = EmptyObject("NULL")
Number: Any = EmptyObject("Number")
RegExp: Any = EmptyObject("RegExp")
String: Any = EmptyObject("String")
UNDEFINED: Any = EmptyObject("UNDEFINED")
