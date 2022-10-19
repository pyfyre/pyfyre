from pyfyre import render
from pyfyre.nodes import *


class App(Element):
	def __init__(self) -> None:
		super().__init__("main", lambda: [
			Element("h1", lambda: [Text("Welcome to PyFyre 🐍🔥")]),
			Element("p", lambda: [
				Text("Learn PyFyre by reading the "),
				Link(
					"https://pyfyre.netlify.app/",
					lambda: [Text("documentation")]
				),
				Text(". It is also advisable to learn "),
				Link("https://www.brython.info/", lambda: [Text("Brython")]),
				Text(" alongside PyFyre as it is built on top of Brython.")
			])
		])


render("body", {"/": lambda: App()})
