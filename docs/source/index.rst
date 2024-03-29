.. image:: https://user-images.githubusercontent.com/64759159/151080177-2b2ab45a-86e5-4746-b92f-6c4edd1aaa8f.png
   :alt: PyFyre banner

|

Welcome to PyFyre's documentation!
==================================
PyFyre is a fast, declarative, and incrementally adoptable Python web frontend framework for building reactive web user interfaces.

Features
--------
- **Component-based framework**. Developers who have experience in using other frontend frameworks should feel quite at home when using PyFyre.
- **Truly reactive**. PyFyre's virtual DOM allows for simple and efficient state management.
- **Quick navigation**. Navigation between pages is quick with PyFyre's single-page application design.
- **Pythonic code with static typing**. Developing with PyFyre is much easier with its type hinting and Pythonic style of coding.
- **Asynchronous programming**. Run non-blocking functions out of the box.
- **CPython interoperability**. Developers can limitedly use CPython packages on the client-side web.
- **JavaScript interoperability**. Allowing developers to leverage NPM packages and integrate with existing JavaScript applications.
- **Pure Python**. Build web apps without ever touching other languages like HTML and JavaScript.
- **And more!**

Example
-------
See the `examples <https://github.com/pyfyre/pyfyre/tree/main/examples>`_ for more.
If you want to quickly test how PyFyre feels or looks like, try our `playground <https://pyfyre.netlify.app/playground>`_!
But here is a super simple example. See how easy it is to create a simple Hello World web app with PyFyre:

.. code-block:: python

   from pyfyre import render
   from pyfyre.nodes import Node, Widget, Element, Text


   class HelloWorld(Widget):
       def build(self) -> list[Node]:
           return [Element("p", lambda: [Text("Hello, World!")])]


   render({"/": lambda: HelloWorld()})

.. image:: https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png
   :alt: output

Want to jump right in?
----------------------
Feeling like an eager beaver? Jump in to the quick start docs:

.. button-ref:: quickstart
   :color: primary
   :outline:
   :align: left
   :expand:

Implementation
--------------
PyFyre is built on top of `Brython <https://brython.info/>`_ (Browser Python), a Python 3 implementation for client-side web programming. Brython allows Python code to be executed on the client-side browser. Anything you can do with JavaScript, you can also do with Python using Brython. Brython's speed of execution is similar to CPython for most operations. If you want to deep dive into how Brython works under the hood, check `this <https://github.com/brython-dev/brython/wiki/How-Brython-works>`_ out.

Stay Updated
------------
Stay updated about the PyFyre framework by following our `Facebook page <https://www.facebook.com/pyfyreframework>`_.

Contents
--------

.. toctree::
   :maxdepth: 1
   
   Introduction <self>
   quickstart
   help

.. toctree::
   :maxdepth: 1
   :caption: References
   
   modules
   genindex
   modindex
   search

.. toctree::
   :maxdepth: 1
   :caption: Links
   
   PyPI <https://pypi.org/project/pyfyre>
   Repository <https://github.com/pyfyre/pyfyre>
   Homepage <https://pyfyre.netlify.app>
   Facebook Page <https://www.facebook.com/pyfyreframework>
   Discord Server <https://discord.gg/YzEDuqhgZJ>
