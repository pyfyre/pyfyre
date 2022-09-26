from typing import List
from pyfyre import render
from pyfyre.nodes import *
from about import AboutPage
from browser import DOMEvent


class HomePage(Division):
	def __init__(self) -> None:
		self.counter = 0
		
		def pc() -> List[Node]:
			if self.counter == 3:
				raise Exception("Intentional raise condition when count is 3")
			return [TextNode(self.counter)]
		
		self.count = Paragraph(children=pc)
		
		super().__init__(children=[
			Element("h1", children=[TextNode("Welcome to PyFyre ✨")]),
			Span(children=[TextNode("This is an example counter app.")]),
			self.count,
			Button(self.increment, children=[TextNode("Count")]),
			HorizontalRule(),
			Anchor("about", children=[TextNode("About this website")])
		])
	
	def increment(self, event: DOMEvent) -> None:
		self.counter += 1
		self.count.update_dom()


render("body", {
	"/": HomePage(),
	"/about": AboutPage()
})
