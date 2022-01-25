import json

class MyWebpage(PyFyreApp):
    def build(self):
        return Container(
            className = "container",
            children = [
                Text(
                    className="text",
                    textContent="Go to another page"
                ),
                Link(
                    className="link",
                    textContent="About",
                    page=AboutPage
                ),
            ]
        )

class AboutPage(PyFyreApp):
    def build(self):
        return Container(
            className="container-2",
            children=[
                Text(
                    className="text-2",
                    textContent="ABOUT PAGE"
                ),
                Link(
                    className="link",
                    textContent="Home",
                    page=MyWebpage
                )
            ]
        )

runApp(
    MyWebpage(),
    mount="app-mount"    
)
