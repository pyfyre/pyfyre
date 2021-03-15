from pynani.PyNani.core import pynani, utils

# Creating an instance from class
pyNaniDOM = pynani.PyNaniDOM()
utils = utils.Utils()

def helloWorld():
    return utils.header1(
        text="Hello, World!",
    )

pyNaniDOM.render(
    props=[
        helloWorld()
    ]
)