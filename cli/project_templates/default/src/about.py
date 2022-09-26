from pyfyre.nodes import *
from text_generator import generate


class AboutPage(Division):
	def __init__(self) -> None:
		super().__init__(children=[
			Paragraph(children=[TextNode("About Page")]),
			Paragraph(children=[TextNode(f"Random string: {generate()}")]),
			Anchor("/", children=[TextNode("Go back")])
		])
