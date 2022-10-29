from typing import Any


class EmptyObject:
    def __getattr__(self, attr: str) -> Any:
        return EmptyObject()

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return EmptyObject()

    def __getitem__(self, key: str) -> Any:
        return EmptyObject()


import_js = EmptyObject()
py2js = EmptyObject()
this = EmptyObject()
Date = EmptyObject()
JSON = EmptyObject()
Math = EmptyObject()
NULL = EmptyObject()
Number = EmptyObject()
RegExp = EmptyObject()
String = EmptyObject()
UNDEFINED = EmptyObject()
