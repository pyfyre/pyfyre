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


alert = EmptyObject("alert")
bind = EmptyObject("bind")
confirm = EmptyObject("confirm")
console = EmptyObject("console")
document = EmptyObject("document")
DOMEvent = EmptyObject("DOMEvent")
DOMNode = EmptyObject("DOMNode")
load = EmptyObject("load")
prompt = EmptyObject("prompt")
run_script = EmptyObject("run_script")
window = EmptyObject("window")
aio = EmptyObject("aio")
ajax = EmptyObject("ajax")
html = EmptyObject("html")
local_storage = EmptyObject("local_storage")
markdown = EmptyObject("markdown")
object_storage = EmptyObject("object_storage")
session_storage = EmptyObject("session_storage")
svg = EmptyObject("svg")
template = EmptyObject("template")
timer = EmptyObject("timer")
webcomponent = EmptyObject("webcomponent")
websocket = EmptyObject("websocket")
worker = EmptyObject("worker")
widgets = EmptyObject("widgets")
