![image](https://user-images.githubusercontent.com/64759159/151080177-2b2ab45a-86e5-4746-b92f-6c4edd1aaa8f.png)

# PyFyre - The Python Web Frontend Framework
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![GitHub Version](https://img.shields.io/github/release/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/releases)
[![Github Star](https://img.shields.io/github/stars/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/stargazers) 
[![License](https://img.shields.io/github/license/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/blob/main/LICENSE)

PyFyre is a web frontend framework for building reactive static user interfaces on the web using Python.
- Component-based framework. Developers who have experience of using other frontend frameworks should feel quite at home when using PyFyre, especially Flutter developers.
- Supports JavaScript interoperability, allowing developers to leverage NPM packages and integrate with existing JavaScript applications.
- Supports CPython interoperability, allowing developers to use existing PyPi packages on the client-side web.

PyFyre is at the top of Brython (Browser Python), a Python 3 implementation for client-side web programming.

**Note: PyFyre is not 1.0 yet. Be prepared to do major refactoring due to breaking API changes.**

## Documentation
The documentation can be found in PyFyre website:
https://pyfyre.netlify.app/

## Examples
We have examples in the [examples](examples) folder. But here is the super simple example.
See how easy it is to create a simple Hello World web app that shows Hello, World text:

```py
from pyfyre.widgets import *
from pyfyre.pyfyre import runApp

class MyWebpage(UsesState):
    def build(self):
        return Container(
            children=[
                Text("Hello, World!")
            ]
        )

runApp(MyWebpage())
```

Rendered PyFyre:
![image](https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png)

## Installation
See how easy it is to setup a working environment with PyFyre.

### Prerequisites
* python3.x

### Setting Up a Project
Install the PyFyre CLI:
```
py -m pip install PyFyre
```
Create a new application:
```
pyfyre create-app <app_name>
```
Run the application:
```
cd <project-name>
pyfyre runapp
```
PyFyre has a built-in hot reload to enhance your productivity tremendously. Try it out by editing the `src/__init__.py` and see the magic works.

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for contributing.

## Stay Updated
If you would like to get updates about the PyFyre framework, we created a [Facebook Page](https://www.facebook.com/PyFyreframework) where we are going to post all the updates like newly created widgets, adjustments, core updates, and more!
