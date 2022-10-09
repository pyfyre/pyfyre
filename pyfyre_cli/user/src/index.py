from pyfyre import render
from pyfyre.nodes import *


class App(Element):
	def __init__(self) -> None:
		super().__init__("main", lambda: [
			Element("h1", lambda: [TextNode("Welcome to PyFyre 🐍🔥")]),
			Element("p", lambda: [
				TextNode("Learn PyFyre by reading the "),
				Anchor(
					"https://pyfyre.netlify.app/",
					lambda: [TextNode("documentation")]
				),
				TextNode(". It is also advisable to learn "),
				Anchor("https://www.brython.info/", lambda: [TextNode("Brython")]),
				TextNode(" alongside PyFyre as it is built on top of Brython.")
			])
		])


render("body", {"/": lambda: App()})
