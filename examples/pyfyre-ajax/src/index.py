from browser import ajax
from pyfyre.nodes import *
from typing import Dict, Any
from pyfyre import render, State


class App(FutureWidget):
	# FutureWidget allows you to make the `build` method to
	# be asyncronous in order to run other asyncronous functions.

	def __init__(self) -> None:
		# A State object with a dictionary and empty dictionary default value.
		self.user = State[Dict[Any, Any]]({})
		super().__init__()

	async def fetch_user(self) -> None:
		await ajax.get(
			"https://randomuser.me/api/",
			mode="json",
			# Once fetching is complete, get the json response from the
			# request object and set the value of the `self.user` State object.
			# All of the Element objects
			# that depends on the State object will be rerendered automatically.
			oncomplete=lambda req: self.user.set_value(req.json)
			# If you are not familiar with `lambda` Python but familiar with
			# javascript, this Python code equivalents to:
			# oncomplete: (req) => this.user.set_value(req.json)
		)

	async def build(self) -> Element:
		await self.fetch_user()  # Fetch the data asyncronously

		return Element(
			"main",
			lambda: [
				Element(
					"img",
					attrs={
						"src": self.user.value["results"][0]["picture"]["large"]
						if self.user.value else ""
					}
				),
				Element("p", lambda: [Text(
					f"{self.user.value['results'][0]['name']['first']} "
					f"{self.user.value['results'][0]['name']['last']}"
					if self.user.value else "Loading"
				)])
			],
			# Element("main") will be automatically rerendered once its
			# dependency state has been updated.
			states=[self.user]
		)


render({"/": lambda: App()})
