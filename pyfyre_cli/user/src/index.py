from typing import List
from pyfyre import render, Style
from pyfyre import on_mount, create_effect, State
from pyfyre.nodes import Node, Widget, Element, Text, Link, Button

def my_app(instance):

    count = State[int](0)
    computed_count = State[int](0)

    @create_effect([count])
    def effect():
        # An effect where count will be multiplied
        computed_count.set_value(count.value * 2)

    return Button(lambda e: count.set_value(count.value + 1), lambda: [
        Text('Counts: ', count),
        Element('br'),
        Text('Multiplied by 2: ', computed_count)
    ])


render({"/": lambda: my_app})
