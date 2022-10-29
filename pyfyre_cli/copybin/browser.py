from typing import Any


class EmptyObject:
    def __getattr__(self, attr: str) -> Any:
        return EmptyObject()

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return EmptyObject()

    def __getitem__(self, key: str) -> Any:
        return EmptyObject()


alert = EmptyObject()
bind = EmptyObject()
confirm = EmptyObject()
console = EmptyObject()
document = EmptyObject()
DOMEvent = EmptyObject()
DOMNode = EmptyObject()
load = EmptyObject()
prompt = EmptyObject()
run_script = EmptyObject()
window = EmptyObject()
aio = EmptyObject()
ajax = EmptyObject()
html = EmptyObject()
local_storage = EmptyObject()
markdown = EmptyObject()
object_storage = EmptyObject()
session_storage = EmptyObject()
svg = EmptyObject()
template = EmptyObject()
timer = EmptyObject()
webcomponent = EmptyObject()
websocket = EmptyObject()
worker = EmptyObject()
widgets = EmptyObject()
