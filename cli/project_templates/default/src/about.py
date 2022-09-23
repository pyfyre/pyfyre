from pyfyre.widgets import *


class AboutPage(Container):
	def __init__(self) -> None:
		super().__init__(children=[
			Paragraph("About Page")
		])
