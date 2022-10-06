from pyfyre import render
from pyfyre.nodes import *


class HomePage(Element):
	def __init__(self) -> None:
		super().__init__(
			"div",
			lambda: [
				Element(
					"p",
					lambda: [TextNode("Welcome to Home page!")],
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					}
				),
				RouterLink(
					"/about",
					lambda: [TextNode("Go to About")],
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					}
				)
			],
			attrs={
				"style": "height: 100vh; width: 100vw; display: flex; "
				"flex-direction: column; justify-content: center;"
			}
		)


class AboutPage(Element):
	def __init__(self) -> None:
		super().__init__(
			"div",
			lambda: [
				Element(
					"p",
					lambda: [TextNode("Welcome to About page!")],
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					}
				),
				RouterLink(
					"/",
					lambda: [TextNode("Go to Home")],
					attrs={
						"style": "margin-left: auto; margin-right: auto; font-size: 50px;"
					}
				)
			],
			attrs={
				"style": "height: 100vh; width: 100vw; display: flex; "
				"flex-direction: column; justify-content: center;"
			}
		)


render("body", {
	"/": lambda: HomePage(),
	"/about": lambda: AboutPage()
})
