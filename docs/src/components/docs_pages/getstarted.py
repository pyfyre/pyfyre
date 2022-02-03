from pyfyre.widgets import *
from src.components.docs_pages import DocsPage
from src.components.docs_pages.section import Section

class Introduction(DocsPage):
    def __init__(self):

        def whatIsPyFyre():
            return Container(
                className="",
                children=[
                    Text(
                        className="mt-5",
                        textContent = "PyFyre is a fast, declarative, and incrementally adoptable Python web frontend framework for building reactive static web applications easily and efficiently. It allows you to create frontend applications with the programming language you already know, Python. Thanks to Brython's powerful tooling, PyFyre also allows you to use existing Python Packages on the client-side web. PyFyre also fits to create Single-Page applications with powerful built-in tools like PyFyre Router, and more."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "PyFyre has a quite of mix with the existing largest framework, React and Flutter. PyFyre is inspired by Flutter's beautiful development experience and React's speed and efficiency. Together, PyFyre is a developer and user friendly framework in Python."
                    ),
                ]
            )

        def pythonOnClientSideWeb():
            return Container(
                className="",
                children=[
                    Text(
                        className="mt-5",
                        textContent = "You're probably new with Python on the client-side web as the current frontend frameworks used today are made with Node.js Javascript. PyFyre's mission is not to *really* reinvent the wheel, its mission is to allow the frontend web to access existing Python Packages."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "How? PyFyre compiles your Python code in Javascript itself instead of CPython with the help of Brython (Browser Python). It's still the same, just not Javascript but it's Python. Thanks to Brython, you can also access vanilla Javascript."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "PyFyre is in the top of Brython, most of its operations are on Brython. PyFyre just helps developers to create apps easily just like React, Vue, and Flutter."
                    ),
                ]
            )
        
        def content():
            return Container(
                className="text-base",
                children=[
                    Section(
                        "What and why PyFyre",
                        content=whatIsPyFyre
                    ),
                    Container(className="mt-20", children=[]),
                    Section(
                        "Python on the client-side web",
                        content=pythonOnClientSideWeb
                    ),
                ]
            )

        super().__init__(content=content)


class Installation(DocsPage):
    def __init__(self):

        def install():
            return Container(
                className="",
                children=[
                    Text(
                        className="mt-5",
                        textContent = "PyFyre installation is really straightforward, you only need to be familiar of Python and CSS, and a working environment."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "To install PyFyre, you need to install Python 3.x, and a working `pip` command. To make sure you installed it correctly, go to your terminal (cmd on Windows) and type `py --version` if Python version shows, you already have Python. To check `pip`, type `pip --version` and it should show as well."
                    ),

                    # Install PyFyre CLI
                    Text(
                        className="mt-7 text-xl font-medium",
                        textContent = "Install PyFyre CLI"
                    ),
                    Text(
                        className="mt-4",
                        textContent = "You need PyFyre CLI to create projects, generate application and perform commands."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "To install the PyFyre CLI, open a terminal window (cmd on Windows) and run the following command:"
                    ),
                    Text(
                        className="mt-2 bg-[#f2f2f2] px-4 py-4 rounded-md",
                        textContent = "pip install pyfyre"
                    ),

                    # Create an App
                    Text(
                        className="mt-7 text-xl font-medium",
                        textContent = "Create an App"
                    ),
                    Text(
                        className="mt-4",
                        textContent = "Start your app and create a new workspace to develop your apps."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "To create a new app, run the PyFyre CLI command:"
                    ),
                    Text(
                        className="mt-2 bg-[#f2f2f2] px-4 py-4 rounded-md",
                        textContent = "pyfyre create-app my-cool-app"
                    ),
                    Text(
                        className="mt-4",
                        textContent = "You can replace `my-cool-app` with the name of the app you desired."
                    ),

                    # Run the App
                    Text(
                        className="mt-7 text-xl font-medium",
                        textContent = "Run the App"
                    ),
                    Text(
                        className="mt-4",
                        textContent = "PyFyre has a development server that has hot reload that detects changes in your code and reload the application automatically."
                    ),
                    Text(
                        className="mt-4 ml-2",
                        textContent = "1. Navigate to the app folder, in our case, it's `my-cool-app`"
                    ),
                    Text(
                        className="mt-4 ml-2",
                        textContent = "2. Run PyFyre CLI command:"
                    ),
                    Text(
                        className="mt-2 bg-[#f2f2f2] px-4 py-4 rounded-md",
                        textContent = "pyfyre runapp"
                    ),
                    Text(
                        className="mt-4",
                        textContent = "And voila! You now have a running PyFyre app on your local machine."
                    ),
                    Text(
                        className="mt-4",
                        textContent = "Note: Once you have run the app, PyFyre will generate a folder called `__serve__`, the folder contains all the files the running server need. You can delete it once `runapp` has finished or you can ignore it on .gitignore file."
                    ),
                ]
            )
        
        def content():
            return Container(
                className="text-base",
                children=[
                    Section(
                        "Install",
                        content=install
                    ),
                ]
            )

        super().__init__(content=content)