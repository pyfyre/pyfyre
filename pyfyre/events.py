from enum import Enum
from typing import Callable
from browser import DOMEvent, window


class BaseEventType(Enum):
	pass


class PyFyreEventType(BaseEventType):
	pyfyreload = "pyfyreload"


class ElementEventType(BaseEventType):
	"""https://developer.mozilla.org/en-US/docs/Web/API/Element#events"""
	cancel = "cancel"
	error = "error"
	scroll = "scroll"
	select = "select"
	wheel = "wheel"
	auxclick = "auxclick"
	click = "click"
	contextmenu = "contextmenu"
	dblclick = "dblclick"
	mousedown = "mousedown"
	mouseenter = "mouseenter"
	mouseleave = "mouseleave"
	mousemove = "mousemove"
	mouseout = "mouseout"
	mouseover = "mouseover"
	mouseup = "mouseup"


class WindowEventType(BaseEventType):
	"""https://developer.mozilla.org/en-US/docs/Web/API/Window#events"""
	error = "error"
	languagechange = "languagechange"
	devicemotion = "devicemotion"
	deviceorientation = "deviceorientation"
	resize = "resize"
	storage = "storage"
	animationcancel = "animationcancel"
	animationend = "animationend"
	animationiteration = "animationiteration"
	animationstart = "animationstart"
	copy = "copy"
	cut = "cut"
	paste = "paste"
	offline = "offline"
	online = "online"
	blur = "blur"
	focus = "focus"
	gamepadconnected = "gamepadconnected"
	gamepaddisconnected = "gamepaddisconnected"
	hashchange = "hashchange"
	pagehide = "pagehide"
	pageshow = "pageshow"
	popstate = "popstate"
	beforeunload = "beforeunload"
	DOMContentLoaded = "DOMContentLoaded"
	load = "load"
	unload = "unload"
	appinstalled = "appinstalled"
	beforeinstallprompt = "beforeinstallprompt"
	message = "message"
	messageerror = "messageerror"
	afterprint = "afterprint"
	beforeprint = "beforeprint"
	rejectionhandled = "rejectionhandled"
	unhandledrejection = "unhandledrejection"
	transitioncancel = "transitioncancel"
	transitionend = "transitionend"
	transitionrun = "transitionrun"
	transitionstart = "transitionstart"
	vrdisplayactivate = "vrdisplayactivate"
	vrdisplayblur = "vrdisplayblur"
	vrdisplayconnect = "vrdisplayconnect"
	vrdisplaydeactivate = "vrdisplaydeactivate"
	vrdisplaydisconnect = "vrdisplaydisconnect"
	vrdisplayfocus = "vrdisplayfocus"
	vrdisplaypresentchange = "vrdisplaypresentchange"


def window_event_listener(
	event_type: BaseEventType
) -> Callable[[Callable[[DOMEvent], None]], Callable[[DOMEvent], None]]:
	def window_event_listener_decorator(
		callback: Callable[[DOMEvent], None]
	) -> Callable[[DOMEvent], None]:
		window.bind(event_type.value, callback)
		return callback
	
	return window_event_listener_decorator
