import json

class MyWebpage(PyFyreApp):
    
    def __init__(self):
        self.image = "None"
    
    def build(self):
        
        def fetch(event):
            Ajax.get("https://randomuser.me/api", then=display)

        def display(request):
            data = json.loads(request.text)
            self.image = data["results"][0]["picture"]["large"]

            self.update() # Rerender the app

        return Container(
            className = "container",
            children = [
                Image(
                    className="image",
                    src=self.image
                ),
                Button(
                    className="btn",
                    textContent="Fetch Random User",
                    onClick=fetch
                )
            ]
        )

runApp(
    MyWebpage(),
    mount="app-mount"    
)