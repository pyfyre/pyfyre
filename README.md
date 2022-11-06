![image](https://user-images.githubusercontent.com/64759159/151080177-2b2ab45a-86e5-4746-b92f-6c4edd1aaa8f.png)

# PyFyre - The Python Web Frontend Framework
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![GitHub Version](https://img.shields.io/github/release/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/releases)
[![Github Star](https://img.shields.io/github/stars/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/stargazers) 
[![License](https://img.shields.io/github/license/pyfyre/pyfyre.svg?style=for-the-badge)](https://github.com/pyfyre/pyfyre/blob/main/LICENSE)

A fast, declarative, and incrementally adoptable Python web frontend framework for building reactive web user interfaces.  
PyFyre offers the following:
- **Component-based framework**. Developers who have experience in using other frontend frameworks should feel quite at home when using PyFyre.
- **Truly reactive**. PyFyre's virtual DOM allows for simple and efficient state management.
- **Quick navigation**. Navigation between pages is quick with PyFyre's single-page application design.
- **Pythonic code with static typing**. Developing with PyFyre is much easier with its type hinting and Pythonic style of coding.
- **Asynchronous programming**. Run non-blocking functions out of the box.
- **CPython interoperability**. Developers can limitedly use CPython packages on the client-side web.
- **JavaScript interoperability**. Allowing developers to leverage NPM packages and integrate with existing JavaScript applications.
- **Pure Python**. Build web apps without ever touching other languages like HTML and JavaScript.
- **And more!**

## Documentation
Learn PyFyre by reading the [documentation](https://pyfyre.netlify.app/).
It is also advisable to learn [Brython](https://www.brython.info/) alongside PyFyre as it is built on top of Brython.

## Examples
See the [examples](examples) directory for more. But here is a super simple example.  
See how easy it is to create a simple Hello World web app with PyFyre:
```py
from pyfyre import render
from pyfyre.nodes import *


class HelloWorld(Widget):
	def build(self) -> list[Node]:
		return [Element("p", lambda: [Text("Hello, World!")])]


render({"/": lambda: HelloWorld()})
```
![image](https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png)

## Installation
```bash
pip install pyfyre
```

## Create and Run a PyFyre Project
```bash
pyfyre create [name]
cd <project_directory>
pyfyre run
```

## Contributing
Please read the [contributing guide](CONTRIBUTING.md).

## Stay Updated
Stay updated about the PyFyre framework by following our [Facebook page](https://www.facebook.com/pyfyreframework/).

## Links
- [PyPI](https://pypi.org/project/pyfyre/)
- [Repository](https://github.com/pyfyre/pyfyre)
- [Documentation](https://pyfyre.netlify.app/)
- [Facebook Page](https://www.facebook.com/pyfyreframework/)
