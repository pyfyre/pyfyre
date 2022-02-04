from pyfyre.widgets import *
from pyfyre.pyfyre import runApp
from pyfyre.ajax import Ajax

class App(UsesState):
    def __init__(self):
        self.image = self.fetch(0)

    def fetch(self, e):
        Ajax.get("https://randomuser.me/api", then=self.display)

    def display(self, request):
        self.image = request.json["results"][0]["picture"]["large"]

        self.update() # Rerender the app
    
    def build(self):
        return Container(
            props={"style": "height: 100vh; width: 100vw; display: flex; flex-direction: column; justify-content: center;"},
            children = [
                Image(
                    props={"style": "width: 300px; height: 300px; margin-left: auto; margin-right: auto;"},
                    src=self.image
                ),
                Button(
                    props={"style": "width: 300px; margin-top: 30px; margin-left: auto; margin-right: auto;"},
                    textContent="Fetch Random User",
                    onClick=self.fetch
                )
            ]
        )

runApp(
    App(),
    mount="app-mount"
)