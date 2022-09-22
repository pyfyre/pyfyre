from typing import Optional, Dict, List
from pyfyre.widgets.base import Widget, BaseWidget


class Container(Widget):
	def __init__(
		self, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		super().__init__("div", props=props, children=children)
