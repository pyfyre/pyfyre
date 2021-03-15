## PyNani
PyNani is a Python web user interface framework for building reactive static websites and for those Python devs who hates HTML. Pynani is free and open source project.

## Documentation
Documentation for PyNani is still in development.

## Examples
We have examples in ```/examples``` folder. But here is the easy to access examples and explaination:

```py
# Importing pynani and utils from the core folder
from pynani.PyNani.core import pynani, utils

# Create a new variable with PyNaniDOM() instance from class
pyNaniDOM = pynani.PyNaniDOM()

# Same here
utils = utils.Utils()

# Here where all element rendered to the screen.
pyNaniDOM.render(
    # Props is a list of elements to render in the screen
    props=[
        # From HelloMessage function
        HelloMessage("User"),
        CustomHTML()
    ]
)

def HelloMessage(text):
    # Returns an Header1 which is equal to h1 in HTML
    # Header1 is getting an argument (text(string), onclick(function), styles(list of CSS Styles))
    return utils.header1(
        text=text,
        styles=[
            "background-color: black"
        ]
    )

def CustomHTML():
    # PyNani also support custom HTML like ReactJS
    return "<div>Hello, Frank!</div>
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
