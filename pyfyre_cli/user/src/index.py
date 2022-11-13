from typing import List
from pyfyre import render, Style
from pyfyre.nodes import *


class App(Widget):
    def build(self) -> List[Node]:
        return [
            Element(
                "h1",
                lambda: [Text("Welcome to PyFyre 🐍🔥")],
                styles=[Style(font_family="Sans")],
            ),
            Element(
                "p",
                lambda: [
                    Text("Get started by modifying the "),
                    Element("code", lambda: [Text("src/index.py")]),
                    Text("."),
                ],
            ),
            Element(
                "p",
                lambda: [
                    Text("Learn PyFyre by reading the "),
                    Link(
                        "https://pyfyre-docs.netlify.app/",
                        lambda: [Text("documentation")],
                    ),
                    Text(". It is also advisable to learn "),
                    Link("https://www.brython.info/", lambda: [Text("Brython")]),
                    Text(" alongside PyFyre as it is built on top of Brython."),
                ],
            ),
            Element("h2", lambda: [Text("Deployment")]),
            Element(
                "p",
                lambda: [
                    Text("Run "),
                    Element("code", lambda: [Text("pyfyre build")]),
                    Text(". The build files are saved in the "),
                    Element("code", lambda: [Text("build")]),
                    Text(
                        " directory so you can just serve or deploy that directory to the web."
                    ),
                ],
            ),
            Element("h2", lambda: [Text("Links")]),
            Element(
                "ul",
                lambda: [
                    Element(
                        "li",
                        lambda: [
                            Link(
                                "https://pypi.org/project/pyfyre",
                                lambda: [Text("PyPI")],
                            )
                        ],
                    ),
                    Element(
                        "li",
                        lambda: [
                            Link(
                                "https://github.com/pyfyre/pyfyre",
                                lambda: [Text("Repository")],
                            )
                        ],
                    ),
                    Element(
                        "li",
                        lambda: [
                            Link(
                                "https://pyfyre-docs.netlify.app",
                                lambda: [Text("Documentation")],
                            )
                        ],
                    ),
                    Element(
                        "li",
                        lambda: [
                            Link(
                                "https://www.facebook.com/pyfyreframework",
                                lambda: [Text("Facebook Page")],
                            )
                        ],
                    ),
                    Element(
                        "li",
                        lambda: [
                            Link(
                                "https://discord.gg/YzEDuqhgZJ",
                                lambda: [Text("Discord Server")],
                            )
                        ],
                    ),
                ],
            ),
        ]


render({"/": lambda: App()})
