from pyfyre.runtime_dom.render import Render
from settings import ROUTES
from typing import Dict, Callable, Optional
from pyfyre.nodes import Node, Element, TextNode
from browser import document, window, DOMEvent, DOMNode
from pyfyre.events import window_event_listener, WindowEventType


class RouteManager:
	_routes_builder: Dict[str, Callable[[], Node]] = {}
	_routes: Dict[str, Optional[Node]] = {}
	_root_node = document.select("body")
	
	@staticmethod
	def initialize(
		root_node: DOMNode, routes: Dict[str, Callable[[], Node]]
	) -> None:
		RouteManager._root_node = root_node
		RouteManager._routes_builder = routes
		
		@window_event_listener(WindowEventType.popstate)
		def onpopstate(event: DOMEvent) -> None:
			RouteManager.change_route(window.location.pathname)
	
	@staticmethod
	def parse_route(route: str) -> str:
		el = document.createElement("a")
		el.href = route
		route = str(el.pathname)
		
		if route == "/":
			return route
		
		return str(el.pathname).rstrip("/")
	
	@staticmethod
	def get_node(route: str, *, parse_route: bool = True) -> Node:
		if parse_route:
			route = RouteManager.parse_route(route)
		
		node = RouteManager._routes.get(route)
		
		if node is None:
			route_builder = RouteManager._routes_builder.get(route)
			node = route_builder() if route_builder else None
			RouteManager._routes[route] = node
					
		return node or Element("p", lambda: [TextNode("404: Page Not Found :(")])
	
	@staticmethod
	def render_route(route: str) -> None:
		node = RouteManager.get_node(route)
		_app = Render.render(node.vdom())
		RouteManager._root_node.innerHTML = ""
		RouteManager._root_node.appendChild(_app)
	
	@staticmethod
	def change_route(route: str) -> None:
		route = RouteManager.parse_route(route)
		route_data = ROUTES.get(route) or {
			"title": "404: Page Not Found :("
		}
		
		document.title = route_data.get("title")
		RouteManager.render_route(route)
