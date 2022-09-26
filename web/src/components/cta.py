from pyfyre.widgets import *

class CallToAction(Container):
    def __init__(self, title, desc, link):
        super().__init__(
            className="flex flex-col w-full h-3/6 justify-center mx-auto bg-gradient-to-r from-[#4568dc] to-[#b06ab3] text-white p-10",
            children=[
                Text(
                    className="text-md font-bold",
                    textContent=title
                ),
                Text(
                    className="text-3xl w-4/6 font-normal",
                    textContent=desc
                ),
                Container(
                    className="mt-5",
                    children=[
                        Link(
                            className="bg-transparent border border-white w-fit px-5 py-2 text-base rounded-3xl cursor-pointer hover:bg-white hover:text-[#222222]",
                            textContent=f"Visit {link}",
                            to=link,
                            external=True
                        )
                    ]
                )
            ]
        )