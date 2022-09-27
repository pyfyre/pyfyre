from pyfyre import render
from pyfyre.nodes import *


class HomePage(Element):
	def __init__(self) -> None:
		super().__init__(
			"div",
			attrs={
				"style": "height: 100vh; width: 100vw; display: flex; "
				"flex-direction: column; justify-content: center;"
			},
			children=[
				Element(
					"p",
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					},
					children=[TextNode("Welcome to Home page!")]
				),
				Anchor(
					"/about",
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					},
					children=[TextNode("Go to About")]
				)
			]
		)


class AboutPage(Element):
	def __init__(self) -> None:
		super().__init__(
			"div",
			attrs={
				"style": "height: 100vh; width: 100vw; display: flex; "
				"flex-direction: column; justify-content: center;"
			},
			children=[
				Element(
					"p",
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					},
					children=[TextNode("Welcome to About page!")]
				),
				Anchor(
					"/",
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					},
					children=[TextNode("Go to Home")]
				)
			]
		)


render("body", {
	"/": lambda: HomePage(),
	"/about": lambda: AboutPage()
})
