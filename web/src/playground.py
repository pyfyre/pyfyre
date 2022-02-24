from pyfyre.widgets import *

from browser import document, window

def runApp(app):
    try:
        out = document.getElementById("output-id")
        out.innerHTML = ""
        out.appendChild(app.dom())
    except Exception as e:
        out.innerHTML = ""
        out.innerHTML = "Error"

class PlaygroundPage(UsesState):
    def __init__(self):
        self.output = None
        self.controller = TextInputController()

        window.CodeListen.listen(self.compile)

    def compile(self):
        textArea = window.CodeMirrorAPI.codeMirror.getValue()

        exec(textArea)

    def build(self):

        document.body.classList.add("overflow-hidden")
        document.body.classList.remove("overflow-auto")

        return Container(
            className="flex flex-row w-full h-screen overflow-hidden",
            children=[
                Container(
                    className="flex flex-col w-6/12",
                    children=[
                        TextInput(
                            className="",
                            controller=self.controller,
                            props={
                                "id": "code-editor",
                                "cols": 40,
                                "rows": 5 
                            },
                            multiline=True
                        ),
                    ]
                ),
                Container(
                    className="border-l-4",
                    children=[
                        Text("Result:", className="m-2 font-black"),
                        Container(
                            children=[],
                            props={"id": "output-id"},
                            className="p-2 h-full w-full overflow-auto"
                        )
                    ]
                )
            ]
        )