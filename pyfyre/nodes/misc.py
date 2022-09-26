from pyfyre.nodes.base import Element


class LineBreak(Element):
	def __init__(self) -> None:
		super().__init__("br")


class HorizontalRule(Element):
	def __init__(self) -> None:
		super().__init__("hr")
