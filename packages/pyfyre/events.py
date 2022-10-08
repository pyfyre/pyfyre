from enum import Enum


class BaseEventType(Enum):
	pass


class EventType(BaseEventType):
	"""https://developer.mozilla.org/en-US/docs/Web/API/Element#events"""
	Cancel = "cancel"
	Error = "error"
	Scroll = "scroll"
	Select = "select"
	Wheel = "wheel"


class MouseEventType(BaseEventType):
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
