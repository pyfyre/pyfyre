from settings import ROUTES
from browser import document
from typing import Dict, Callable, Optional
from pyfyre.nodes import Node, Element, TextNode


class RouteManager:
	_routes_builder: Dict[str, Callable[[], Node]] = {}
	_routes: Dict[str, Optional[Node]] = {}
	root_node = document.select("body")
	
	@staticmethod
	def set_routes(routes: Dict[str, Callable[[], Node]]) -> None:
		RouteManager._routes_builder = routes
	
	@staticmethod
	def parse_route(route: str) -> str:
		el = document.createElement("a")
		el.href = route
		route = str(el.pathname)
		
		if route == "/":
			return route
		
		return str(el.pathname).rstrip("/")
	
	@staticmethod
	def get_node(route: str) -> Node:
		route = RouteManager.parse_route(route)
		node = RouteManager._routes.get(route)
		
		if node is None:
			route_builder = RouteManager._routes_builder.get(route)
			node = route_builder() if route_builder else None
			RouteManager._routes[route] = node
		
		return node or Element("p", children=[TextNode("404: Page Not Found :(")])
	
	@staticmethod
	def render_route(route: str) -> None:
		node = RouteManager.get_node(route)
		RouteManager.root_node.innerHTML = ""
		RouteManager.root_node.appendChild(node.dom)
	
	@staticmethod
	def change_route(route: str) -> None:
		route = RouteManager.parse_route(route)
		route_data = ROUTES.get(route) or {
			"title": "404: Page Not Found :("
		}
		
		document.title = route_data.get("title")
		RouteManager.render_route(route)
