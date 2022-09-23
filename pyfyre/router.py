import pathlib
from typing import Dict
from pyfyre.widgets import BaseWidget, Paragraph


class RouteManager:
	routes: Dict[str, BaseWidget] = {}
	
	@staticmethod
	def get_widget(route: str) -> BaseWidget:
		route = str(pathlib.Path(route))
		return RouteManager.routes.get(route) or Paragraph("404: Page Not Found :(")
