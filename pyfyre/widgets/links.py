from typing import Optional, Dict, List
from pyfyre.widgets.base import Widget, BaseWidget


class Link(Widget):
	def __init__(
		self, href: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		props = props or {}
		props["href"] = href
		super().__init__("a", props=props, children=children)
