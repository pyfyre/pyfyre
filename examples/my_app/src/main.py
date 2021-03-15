from pynani.PyNani.core import pynani, utils

# Creating an instance from class
pyNaniDOM = pynani.PyNaniDOM()
utils = utils.Utils()

def HelloMessage(text):
    return utils.header1(
        text="Hello, " + text,
        styles=[
            "background-color: black",
            "color: white",
            "padding: 30px",
            "margin: 30px",
        ]
    )

def CustomHTML():
    return "<div style=\"margin-left: 30px\">Welcome to my Website</div>"

pyNaniDOM.render(
    props=[
        HelloMessage("Max"),
        CustomHTML()
    ]
)