from typing import Optional, Dict, List
from pyfyre.widgets.base import Widget, BaseWidget


class Image(Widget):
	def __init__(
		self, src: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		props = props or {}
		props["src"] = src
		super().__init__("img", props=props, children=children)
