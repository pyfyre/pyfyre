from typing import List
from pyfyre import render, Style
from pyfyre import on_mount, create_effect, State, CreateRef
from pyfyre.nodes import Node, Widget, Element, Text, Link, Button, TextInput, ListBuilder

def my_app(context):

    todos = State[list](['hello'])
    inputRef = CreateRef(None)

    @on_mount(context)
    def mount():
        print("Just mounted")

    def add_todo(e):
        todos.set_value([*todos.value, inputRef.node.value])

    def todo(i):
        return Text(todos.value[i])

    return Element('p', lambda: [
        ListBuilder(count=len(todos.value), item_builder=todo, states=[todos]),
        TextInput(ref=inputRef),
        Element('br'),
        Button(add_todo, lambda: [
            Text("Add Todo")
        ])
    ], states=[todos])


render({"/": lambda: my_app})
