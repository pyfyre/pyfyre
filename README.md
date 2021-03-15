## PyNani
PyNani is a Python web user interface framework for building reactive static websites and for those Python devs who hates HTML. Pynani is free and open source project.

## Documentation
Documentation for PyNani is still in development.

## Examples
We have examples in ```/examples``` folder. But here is the easy to access examples:

```py
from pynani.PyNani.core import pynani, utils

# Creating an instance from class
pyNaniDOM = pynani.PyNaniDOM()
utils = utils.Utils()

pyNaniDOM.render(
    props=[
        HelloMessage("User"),
        CustomHTML()
    ]
)

def HelloMessage(text):
    return utils.header1(
        text=text,
        styles=[
            "background-color: black"
        ]
    )

def CustomHTML():
    return "<div>Hello, Frank!</div>"
```

## Installation
We haven't added some code for installing the PyNani automatically but
here's the installation guide to install PyNani and create a PyNani
App manually.

To create a PyNani App, for now, clone or download this repo to your 
own local machine.

Create a virtual environment by typing to cmd:
```
py -m venv env
```

And place all the files to ```env/lib/site-packages/```

And, you're now cool, you just added the PyNani to your local machine.

Now, get some examples from ```/examples``` folder and paste it to your file.
And that's it! PyNani!

If you have any questions about this installation guide and it is not clear
for you, please open a issue.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for this.
