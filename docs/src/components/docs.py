from pyfyre.widgets import *
from pyfyre.globals import Globals
from src.components.docs_pages.getstarted import *
from src.components.docs_pages import DocsPage

# You can make components by inherting a Widget class
# and initialize it on the `super().__init__()`.
class Docs(Container):
    def __init__(self):

        pages = {
            "/": Introduction,
            "/?": NotFinished,
            "/docs": Introduction,
            "/docs/introduction": Introduction,
            "/docs/introduction": Introduction,
            "/docs/installation": Installation
        }

        currentPage = pages[Globals.__LOC__] if Globals.__LOC__ is not None else pages["/docs/introduction"]

        super().__init__(
            className = "flex flex-row h-full w-full overflow-y-auto",
            children = [
                Sidebar(),
                currentPage()
            ]
        )

class NotFinished(DocsPage):
    def __init__(self):
        
        def content():
            return Text(
                className="",
                textContent="This documentation page is under construction yet. Please come back later."
            )

        super().__init__(content)

class Sidebar(Container):
    def __init__(self):

        docs = {
            "Get started": {
                "Introduction": [
                    ["What and why PyFyre?", "/docs/introduction"],
                    ["Python on the client-side web", "/docs/introduction"],
                ],
                "Installation": [
                    ["Install", "/docs/installation"],
                ],
            },
            "Development": [
                ["Introduction to components", "/?"],
                ["Building components", "/?"],
                ["Component properties", "/?"],
                ["Navigation & Routing", "/?"],
                ["Python Packages on the web", "/?"],
            ],
            "Cookbook": [
                ["Increment-decrement", "/?"],
                ["Display images", "/?"],
                ["Create a list from Python List", "/?"],
                ["Navigation", "/?"]
            ]
        }

        docs_list = list(docs)

        def document(i):

            part_name = docs_list[i]
            contents = docs[docs_list[i]]

            def contentBuilder(contentIndex):
                content = None

                if type(contents) == dict:
                    content_list = list(contents)
                    content_contents = contents[content_list[contentIndex]]

                    title = content_list[contentIndex]
                    
                    content = content_contents

                    def nestedDocument(i):
                        return Link(
                            className="text-base ml-6",
                            textContent=f"{i+1}. {content[i][0]}",
                            to=content[i][1]
                        )

                    return Container(
                        className="mt-4",
                        children=[
                            Text(
                                className="text-base",
                                textContent=title
                            ),
                            ListBuilder(
                                className="flex flex-col",
                                count=len(content),
                                builder=nestedDocument
                            )
                        ]
                    )

                else:
                    content = contents[contentIndex][0]

                    return Link(
                        className="text-base",
                        textContent=content,
                        to=contents[contentIndex][1]
                    )
        
            return Container(
                className="",
                children=[
                    Text(
                        className="font-bold text-lg",
                        textContent=f"{part_name}"
                    ),
                    ListBuilder(
                        className="flex flex-col",
                        count=len(contents),
                        builder=contentBuilder
                    )
                ]
            )

        super().__init__(
            className="bg-[#f2f2f2] h-screen overflow-y-auto w-80 p-10 text-[#222222] fixed border-r",
            children=[
                ListBuilder(
                    className="flex flex-col space-y-6 mb-10",
                    count=len(docs),
                    builder=document
                )
            ]
        )