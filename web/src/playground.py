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

            # Introduction
            [
                "Introduction",
                [

                  ## Hello, World
                  ["Hello, World!",
                      """class App(UsesState):
    def build(self):
      return Text("Hello, World")
    
runApp(App())"""
                  ],

                  ## Nested components
                  [
                    "Nested components",
                    """class App(UsesState):
  def build(self):
    return Container(
    	children=[
        Text("Hi mom..."),
        NestedComponent()
      ]
  )
  
class NestedComponent(UsesState):
  def build(self):
    return Text("I'm an isolated nested component")
                  
runApp(App())"""
                  ],
                ],
            ],

            # Props & Params
            [
              "Props & Params",
              [
                [
                  "Passing params",
                  """class App(UsesState):
  def build(self):
    return Container(
    	children=[
      	Nested(42),
        	Nested()
      ]
    )
  
class Nested(UsesState):
  def __init__(self, answer="a mystery"):
    self.answer = answer
    
  def build(self):
    return Text(f"The answer is {self.answer}")
  
runApp(App())"""
                ],
                [
                  "Widget HTML props",
                  """class App(UsesState):
  def build(self):
    return Button(
    	"I am a disabled button",
      props={
      	"style": "background-color: #f2f2f2; padding: 5px;",
        	"id": "btn-id",
        	"disabled": True
      }
    )
  
runApp(App())"""
                ]
              ]
            ],

            [
              "Inputs",
              [
                [
                  "Text input",
                  """class App(UsesState):
  def __init__(self):
    
    # TextInputController allows you to control TextInputs,
    # control events, and get and set its property.
    self.controller = TextInputController()
    
    self.name = ""
  
  def build(self):
    
    def enter(ev):
      self.name = self.controller.value
      self.update()
    
    return Container(
    	children=[
      	Text(f"Hello, {self.name}"),
        	Container(
            	children=[
                  	TextInput(controller=self.controller, props={"style": "width: 7rem; border: 0.3px solid gray; margin-right: 7px; padding: 5px;"}),
                  	Button("Enter", onClick=enter, props={"style": "background-color: #f2f2f2; padding: 3px;"})
                  ],
              	props={"style": "margin-top: 10px;"}
            )
      ]
    )
    
runApp(App())"""
                ],
                [
                  "Numeric input",
                  """class App(UsesState):
  def __init__(self):
    self.aController = TextInputController()
    self.bController = TextInputController()
    
    self.a = 1
    self.b = 2
  
  def build(self):
    
    def enter(ev):
      self.a = int(self.aController.value)
      self.b = int(self.bController.value)
      self.update()
    
    return Container(
    	children=[
        	Input(self.a, self.aController, enter),
        	Input(self.b, self.bController, enter),
        	Text(f"{self.a} + {self.b} = {self.a + self.b}", props={"style": "margin-top: 10px;"})
      ]
    )
    
class Input(UsesState):
  def __init__(self, val, controller, enter):
    self.val = val
    self.controller = controller
    self.enter = enter
  
  def build(self):
    return Container(
      children=[
        TextInput(
          controller=self.controller,
          props={
            "type": "number",
            "style": "width: 7rem; border: 0.3px solid gray; margin-right: 7px; padding: 5px;"
          },
          defaultValue=self.val
        ),
        TextInput(controller=self.controller, props={"type": "range"}, defaultValue=self.val),
        Button("Enter", onClick=self.enter, props={"style": "background-color: #f2f2f2; padding: 3px;"})
      ],
      props={"style": "margin-top: 10px;"}
    )
    
runApp(App())"""
                ]
              ]
            ],

            # Reactivity
            [
                "Reactivity",
                [
                  
                  ## Reactive assignments
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

                    ## State management
                    [
                    "State management",
                    """
state = State({ "count": 0 }) # I could be a global variable shared across files.

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
                ]
            ],
        ]

    # Structure
    # [
    #   [
    #       "section",
    #       [
    #           [
    #               "content_title",
    #               "code"
    #           ],...
    #       ]
    #   ],...
    # ]
    # i 1 0

    def build(self):

        def section_builder(i):

            def content_builder(j):

                def change_index(ev):
                    state.setValue('currentCode', self.tabs[i][1][j][1])
                    window.CodeMirrorAPI.codeMirror.setValue(state.currentCode)

                return Container(
                    children=[
                        Button(self.tabs[i][1][j][0], onClick=change_index, className="font-thin"),
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

