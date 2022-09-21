from pyfyre.widgets import *
from pyfyre.pyfyre import runApp

class App(UsesState):
    def __init__(self):
        self.todos = []
        self.controller = TextInputController()

    def build(self):

        def todos_list(i):

            def finish_todo(e):
                del self.todos[i]
                self.update()

            return Container(
                props={"style": "display: flex;"},
                children=[
                    Text(self.todos[i]),
                    Button("Finish", onClick=finish_todo)
                ]
            )

        def add_todo(e):
            if len(self.controller.value) == 0: return

            self.todos.append(self.controller.value)
            self.controller.setValue("")
            self.update()

        return Container(
            children=[
                ListBuilder(
                    count=len(self.todos),
                    builder=todos_list
                ),
                TextInput(
                    controller=self.controller
                ),
                Button(
                    "Add Todo",
                    onClick=add_todo
                )
            ]
        )

runApp(
    App(),
    mount="app-mount"
)