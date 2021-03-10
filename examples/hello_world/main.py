from pynani.pyNani.core import PyNani as pyNani

pn = pyNani.PyNani(
    file="lib/templates/index.html",
    title="Hello World"
)

pn.header1(
    text="Hello, World!",
    styles=[
        "text-alignment: center"
    ]
)