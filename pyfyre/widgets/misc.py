from pyfyre.widgets.base import Widget


class LineBreak(Widget):
	def __init__(self) -> None:
		super().__init__("br")


class HorizontalLine(Widget):
	def __init__(self) -> None:
		super().__init__("hr")
