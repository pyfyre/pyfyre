from typing import Optional, Dict, List
from pyfyre.widgets.base import Widget, BaseWidget, TextWidget


class Span(Widget):
	def __init__(
		self, content: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		children = children or []
		children.insert(0, TextWidget(content))
		super().__init__("span", props=props, children=children)


class Paragraph(Widget):
	def __init__(
		self, content: str, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		children = children or []
		children.insert(0, TextWidget(content))
		super().__init__("p", props=props, children=children)
