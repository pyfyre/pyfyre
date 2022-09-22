from enum import Enum

__all__ = [
	"EventType",
	"MouseEventType"
]


class EventType(Enum):
	pass


class MouseEventType(EventType):
	"""https://developer.mozilla.org/en-US/docs/Web/API/Element#mouse_events"""
	AuxClick = "auxclick"
	Click = "click"
	ContextMenu = "contextmenu"
	DbClick = "dblclick"
	MouseDown = "mousedown"
	MouseEnter = "mouseenter"
	MouseLeave = "mouseleave"
	MouseMove = "mousemove"
	MouseOut = "mouseout"
	MouseOver = "mouseover"
	MouseUp = "mouseup"
