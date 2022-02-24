from pyfyre.widgets import *

from browser import document, window

state = State({ "tabIndex": 0, "currentCode": "" })

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
                Sidebar(self),
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

class Sidebar(UsesState):
    def __init__(self, this):
        self.this = this
        self.tabs = [
            [
                "Introduction",
                [
                    "Hello, World!",
                    """class App(UsesState):
  def build(self):
    return Text("Hello, World")
  
runApp(App())"""
                ],
                [
                    "Nested components",
                    """class App(UsesState):
  def build(self):
    return Container(
    	children=[
        	Text("Hi mom!"),
      	NestedComponent()
      ]
    )
    
class NestedComponent(UsesState):
  def build(self):
    return Text("I'm nested!")
  
runApp(App())"""
                ],
            ],
            [
                "Reactivity",
                [
                    "Reactive assignments",
                    """class App(UsesState):
  def __init__(self):
    self.count = 0
  
  def build(self):
    
    def increment(ev):
      self.count += 1
      self.update()
    
    return Button(f"Clicked for {self.count} {'time' if self.count == 1 else 'times'}", onClick=increment)
  
runApp(App())"""
                ],
                [
                    "State management",
                    """state = State({ "count": 0 })

class App(UsesState):
  def build(self):
    
    def increment(ev):
      state.count += 1
      self.update()
    
    return Container(
    	children=[
        	FirstUI(),
        	SecondUI(),
      	Button(f"Click me", onClick=increment),
      ]
    )
  
class FirstUI(UsesState):
  def build(self):
    return Text(state.count)
  
class SecondUI(UsesState):
  def build(self):
    return Text(state.count)
  
runApp(App())"""
                ]
            ],
            [
                "Inputs",
                [
                    "TextInput",
                    """class App(UsesState):
  def __init__(self):
    # TextInputController allows you to control the TextInput widget where this controller passed
    # such as setting the TextInput value, getting the value, etc.
    self.controller = TextInputController()
    
    self.name = ""
  
  def build(self):
    
    def enter(ev):
      self.name = self.controller.value
      self.update()
    
    return Container(
    	children=[
      	Container(
            	children=[
                  	TextInput(controller=self.controller, props={"style": "width: 9rem; border: 0.2px solid gray;"}),
        			Button("Enter", onClick=enter, props={"style": "margin-left: 10px; background-color: #f2f2f2; padding-left: 7px; padding-right: 7px; border-radius: 2px;"})
                  ]
            ),
        	Text(f"Kumusta, {self.name or 'stranger'}!", props={"style": "margin-top: 5px;"})
      ]
    )
    
runApp(App())"""
                ]
            ]
        ]

    # Structure
    # [
    #   [
    #       "section",
    #       [
    #           "content_title",
    #           "code"
    #       ],...
    #   ],...
    # ]
    # i 1 0

    def build(self):

        def section_builder(i):

            def content_builder(j):

                def change_index(ev):
                    state.setValue('currentCode', self.tabs[i][j+1][1])
                    window.CodeMirrorAPI.codeMirror.setValue(state.currentCode)

                return Container(
                    children=[
                        Button(self.tabs[i][j+1][0], onClick=change_index, className="font-thin"),
                    ]
                )
            
            return Container(
                className="mt-5 ml-3",
                children=[
                    Text(self.tabs[i][0], className="text-xl mb-2 font-bold font-mono"),
                    ListBuilder(
                        count=len(self.tabs[i][1]),
                        builder=content_builder
                    )
                ]
            )

        return Container(
            className="w-2/12 border border-r-3 overflow-auto",
            children=[
                ListBuilder(
                    count=len(self.tabs),
                    builder=section_builder
                ) # Section
            ]
        )

