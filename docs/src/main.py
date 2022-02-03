from pyfyre.widgets import *
from src.components.cta import CallToAction
from src.components.description import Descriptions

# You can make components by inherting a Widget class
# and initialize it on the `super().__init__()`.
class HomePage(Container):
    def __init__(self):
        
        _features = [
            [
                "Developer friendly",
                "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
                "The language you already know.",
                "PyFyre allows you to develop apps with the language you already know, Python. Create reactive websites fast with ease. Build your apps in minutes, not days.",
                "Show me"
            ],
            [
                "Fast",
                "https://i.imgur.com/yI8tUab.png",
                "Fast transpilation time on the fly.",
                "PyFyre transpiles your code into small, vanilla JS that works for every browser with the power of Brython that stays fast, and always will be.",
                "Show me"
            ],
            [
                "Productive",
                "https://pbs.twimg.com/profile_images/909757546063323137/-RIWgodF_400x400.jpg",
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
                                className="w-full lg:w-1/3 lg:w-3/12 md:w-1/2",
                                children=[
                                    Image(
                                        className="object-cover object-center rounded-lg",
                                        src=_features[i][1]
                                    )
                                ]
                            ),
                            Container(
                                className=f"flex flex-col {layouts[i][1]} mb-16 text-left lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 md:mb-0",
                                children=[
                                    Text(
                                        className="mb-8 text-lg font-semibold tracking-widest text-black uppercase title-font",
                                        textContent=_features[i][0]
                                    ),
                                    Text(
                                        className="mb-8 text-2xl font-black tracking-tighter text-black md:text-5xl title-font",
                                        textContent=_features[i][2]
                                    ),
                                    Text(
                                        className="mb-8 text-base leading-relaxed text-left text-blueGray-600",
                                        textContent=_features[i][3]
                                    ),
                                    Container(
                                        className="flex flex-col justify-center lg:flex-row",
                                        children=[
                                            Text(
                                                className="flex items-center px-6 py-2 mt-auto font-semibold text-white transition duration-500 ease-in-out transform bg-blue-600 rounded-lg hover:bg-blue-700 focus:shadow-outline focus:outline-none focus:ring-2 ring-offset-current ring-offset-2",
                                                textContent=_features[i][4]
                                            ),
                                        ]
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
                    className="flex flex-col w-full h-5/6 bg-[#222222]",
                    children=[
                        Container(
                            className="flex flex-col w-full mt-28",
                            children=[
                                Text(
                                    className = "text-3xl mx-auto font-bold bg-clip-text h-20 text-transparent bg-gradient-to-r from-cyan-500 to-blue-500 xl:text-6xl",
                                    textContent = "Build reactive static UI using Python."
                                ),
                                Text(
                                    className = "px-28 text-xl mx-auto mt-5 xl:px-52 text-center text-white",
                                    textContent = "PyFyre is a fast, declarative, and incrementally adoptable Python web frontend framework for building reactive static single-page web applications easily and efficiently."
                                )
                            ]
                        ),
                        Container(
                            className="flex space-x-3 mx-auto mt-20 mb-44",
                            children=[
                                Link(
                                    className="bg-[#444444] w-fit px-5 py-2 text-base rounded-3xl text-white cursor-pointer",
                                    textContent="Documentation",
                                    to="/docs"
                                ),
                                Link(
                                    className="bg-[#fab327] w-fit px-5 py-2 text-base rounded-3xl text-white cursor-pointer",
                                    textContent="Get started",
                                    to="/docs/introduction"
                                )
                            ]
                        )
                    ]
                ),
                ListBuilder(
                    className="",
                    count=len(_features),
                    builder=feature
                ),
                CallToAction("Brython", "PyFyre is powered by Brython, a Python 3 implementation for client-side web programming.", "brython.info"),
            ]
        )