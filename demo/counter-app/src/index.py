from pyfyre import render
from pyfyre.nodes import *


class App(Element):
	def __init__(self) -> None:
		super().__init__("main", children=[
			Element("h1", children=[TextNode("Welcome to PyFyre 🐍🔥")]),
			Element("p", children=[
				TextNode("Learn PyFyre by reading the "),
				Anchor(
					"https://pyfyre.netlify.app/",
					children=[TextNode("documentation")]
				),
				TextNode(". It is also advisable to learn "),
				Anchor("https://www.brython.info/", children=[TextNode("Brython")]),
				TextNode(" alongside PyFyre as it is built on top of Brython."),
			])
		])


render("body", {"/": App()})
