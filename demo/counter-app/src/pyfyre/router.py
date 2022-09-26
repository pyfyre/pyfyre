from typing import Dict
from settings import ROUTES
from browser import document
from pyfyre.nodes import Node, Element, TextNode


class RouteManager:
	routes: Dict[str, Node] = {}
	root_node = document.select("body")
	
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
		return RouteManager.routes.get(route) or Element(
			"p", children=[TextNode("404: Page Not Found :(")]
		)
	
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
