from pyfyre.widgets import *

from browser import document, window

codeListen = False

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

        return Container(
            className="flex flex-row w-full h-screen",
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
                            className="m-2",
                            props={"id": "output-id"},
                            children=[]
                        )
                    ]
                )
            ]
        )