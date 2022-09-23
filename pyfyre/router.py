import pathlib
from typing import Dict
from pyfyre.virtual_dom import VirtualDOM
from pyfyre.widgets import BaseWidget, Paragraph


class RouteManager:
	routes: Dict[str, BaseWidget] = {}
	
	@staticmethod
	def get_widget(route: str) -> BaseWidget:
		route = "/" + str(pathlib.Path(route)).lstrip("/")
		return RouteManager.routes.get(route) or Paragraph("404: Page Not Found :(")
	
	@staticmethod
	def change_route(route: str) -> None:
		VirtualDOM.render(RouteManager.get_widget(route).dom())
