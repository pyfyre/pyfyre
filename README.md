![image](https://user-images.githubusercontent.com/64759159/151080177-2b2ab45a-86e5-4746-b92f-6c4edd1aaa8f.png)

# PyFyre - The Python Web Frontend Framework
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![GitHub Version](https://img.shields.io/github/release/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/releases)
[![Github Star](https://img.shields.io/github/stars/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/stargazers) 
[![License](https://img.shields.io/github/license/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/blob/main/LICENSE)

PyFyre is a web frontend framework for building reactive static user interfaces on the web using Python. It allows you to create UI more effectively and efficiently without leaving any language, just Python. PyFyre works like a charm, it transpiles your Python code into native Javascript with the help of Brython (Browser Python) Just-In-Time.

## Documentation
Documentation for PyFyre is still in development.

## Examples
We have examples in the [examples](examples) folder. But here is the super simple example.
See how easy it is to create a simple Hello World web app that shows Hello, World text:

```py
from pyfyre.widgets import *
from pyfyre.pyfyre import runApp

class MyWebpage(PyFyreApp):
    def build(self):
        return Container(
            className = "container",
            children = [
                Text(
                    className = "title",
                    textContent = "Hello, World!"
                ),
            ]
        )

runApp(MyWebpage())
```

Rendered PyFyre:
![image](https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png)

## Installation

### Prerequisites
* python3.x

### Create An App
Install PyFyre via PIP:
```
py -m pip install PyFyre
```
It will automatically be installed.

Now you have PyFyre to your local machine, you can now create an app by:
```
pyfyre create-app <app_name>
```

### Run The App (With HOT RELOAD)
Running PyFyre is actually pretty simple, just run:
```
pyfyre runapp
```
and you now have a PyFyre app running on your local machine with HOT RELOAD.

You can now edit your PyFyre app through `src/__init__.py`, and see the magic.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for contributing.

## Stay Updated
If you would like to get updates about the PyFyre framework, we created a [Facebook Page](https://www.facebook.com/PyFyreframework) where we are going to post all the updates like newly created widgets, adjustments, core updates, and more!
