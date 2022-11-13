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


alert: Any = EmptyObject("alert")
bind: Any = EmptyObject("bind")
confirm: Any = EmptyObject("confirm")
console: Any = EmptyObject("console")
document: Any = EmptyObject("document")
DOMEvent: Any = EmptyObject("DOMEvent")
DOMNode: Any = EmptyObject("DOMNode")
load: Any = EmptyObject("load")
prompt: Any = EmptyObject("prompt")
run_script: Any = EmptyObject("run_script")
window: Any = EmptyObject("window")
aio: Any = EmptyObject("aio")
ajax: Any = EmptyObject("ajax")
html: Any = EmptyObject("html")
local_storage: Any = EmptyObject("local_storage")
markdown: Any = EmptyObject("markdown")
object_storage: Any = EmptyObject("object_storage")
session_storage: Any = EmptyObject("session_storage")
svg: Any = EmptyObject("svg")
template: Any = EmptyObject("template")
timer: Any = EmptyObject("timer")
webcomponent: Any = EmptyObject("webcomponent")
websocket: Any = EmptyObject("websocket")
worker: Any = EmptyObject("worker")
widgets: Any = EmptyObject("widgets")
