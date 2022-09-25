from pyfyre.widgets import *
from text_generator import generate


class AboutPage(Container):
	def __init__(self) -> None:
		super().__init__(children=[
			Paragraph("About Page"),
			Paragraph(f"Random string: {generate()}"),
			LineBreak(),
			Link("", children=[TextWidget("Go back")])
		])
