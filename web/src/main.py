from pyfyre.widgets import *
from src.components.cta import CallToAction

from browser import document

# You can make components by inherting a Widget class
# and initialize it on the `super().__init__()`.
class HomePage(Container):
    def __init__(self):

        document.body.classList.add("overflow-auto")
        document.body.classList.remove("overflow-hidden")
        
        _features = [
            [
                "Developer friendly",
                "python-logo.png",
                "The language you already know.",
                "PyFyre allows you to develop apps with the language you already know, Python. Create reactive websites fast with ease. Build your apps in minutes, not days.",
                "Show me"
            ],
            [
                "Fast",
                "transpiled.png",
                "Fast transpilation time on the fly.",
                "PyFyre transpiles your code into small, vanilla JS that works for every browser with the power of Brython that stays fast, and always will be.",
                "Show me"
            ],
            [
                "Productive",
                "pypi-logo.jpg",
                "Use Python Packages on the web.",
                "Use CPython's existing packages on PyPi.org/, develop sites quickly and efficiently with a large selection of packages.",
                "Visit pypi.org/"
            ],
        ]

        layouts = []

        for i in range(len(_features)):
            layout_1 = "md:flex-row-reverse" if i % 2 == 0 else "md:flex-row"
            layout_2 = "items-start" if i % 2 == 0 else "items-end"

            _layouts = []
            _layouts.append(layout_1)
            _layouts.append(layout_2)
            
            layouts.append(_layouts)

        def feature(i):
            return Container(
                className="",
                children=[
                    Container(
                        className=f"flex flex-col items-center px-5 py-16 mx-auto {layouts[i][0]} lg:px-28",
                        children=[
                            Container(
                                className="w-full mb-10 lg:w-1/3 lg:w-3/12 md:w-1/2",
                                children=[
                                    Image(
                                        className="object-cover object-center rounded-lg w-52 mx-auto md:w-auto",
                                        props={
                                            "loading": "lazy",
                                            "width": 500,
                                            "height": 500
                                        },
                                        src=_features[i][1]
                                    )
                                ]
                            ),
                            Container(
                                className=f"flex flex-col {layouts[i][1]} mb-16 text-left lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 md:mb-0",
                                children=[
                                    Text(
                                        className="mb-8 text-lg font-semibold tracking-widest text-black uppercase title-font text-[#333333]",
                                        textContent=_features[i][0]
                                    ),
                                    Text(
                                        className="mb-8 text-2xl font-black tracking-tighter text-black md:text-5xl title-font text-[#333333]",
                                        textContent=_features[i][2]
                                    ),
                                    Text(
                                        className="mb-8 text-base leading-relaxed text-left text-blueGray-600 text-[#333333]",
                                        textContent=_features[i][3]
                                    )
                                ]
                            )
                        ]
                    ),
                ]
            )

        super().__init__(
            className = "flex flex-col h-screen w-full",
            children = [
                Container(
                    className="flex flex-col w-full h-5/6",
                    children=[
                        Container(
                            className="flex flex-col w-full mt-28",
                            children=[
                                Container(
                                    className="flex flex-col",
                                    children=[
                                        Text(
                                            className = "text-5xl mx-auto font-bold bg-clip-text h-20 text-[#222222] xl:text-7xl",
                                            textContent = "Build reactive"
                                        ),
                                        Text(
                                            className = "text-5xl mx-auto font-bold bg-clip-text h-20 text-transparent bg-gradient-to-r from-cyan-500 to-blue-500 xl:text-7xl",
                                            textContent = "UI using Python."
                                        ),
                                    ]
                                ),
                                Text(
                                    className = "text-lg px-10 xl:text-xl mx-auto mt-5 xl:px-52 text-center text-[#3c3c3c]",
                                    textContent = "A fast, declarative, and incrementally adoptable Python web frontend framework for building reactive web user interfaces."
                                )
                            ]
                        ),
                        Container(
                            className="flex space-x-3 mx-auto mt-20 mb-44",
                            children=[
                                Link(
                                    className="bg-[#fab327] w-fit px-5 py-2 text-base rounded-3xl text-white cursor-pointer",
                                    textContent="Get started",
                                    to="https://pyfyre.gitbook.io/docs/",
                                    external=True
                                ),
                                Link(
                                    className="bg-[#f1f1f1] w-fit px-5 py-2 text-base rounded-xl text-[#474747] hover:text-[#333333] cursor-pointer",
                                    textContent="Learn",
                                    to="/playground"
                                )
                            ]
                        )
                    ]
                ),
                ListBuilder(
                    count=len(_features),
                    builder=feature
                ),
                CallToAction("Brython", "PyFyre is powered by Brython, a Python 3 implementation for client-side web programming.", "https://brython.info"),
            ]
        )