import pathlib
from typing import Dict
from settings import ROUTES
from browser import document
from pyfyre.virtual_dom import VirtualDOM
from pyfyre.widgets import BaseWidget, Paragraph


class RouteManager:
	routes: Dict[str, BaseWidget] = {}
	
	@staticmethod
	def parse_route(route: str) -> str:
		return "/" + str(pathlib.Path(route)).lstrip("/")
	
	@staticmethod
	def get_widget(route: str) -> BaseWidget:
		route = RouteManager.parse_route(route)
		return RouteManager.routes.get(route) or Paragraph("404: Page Not Found :(")
	
	@staticmethod
	def change_route(route: str) -> None:
		route = RouteManager.parse_route(route)
		route_data = ROUTES.get(route) or {
			"title": "404: Page Not Found :("
		}
		
		document.title = route_data.get("title")
		VirtualDOM.render(RouteManager.get_widget(route).dom())
