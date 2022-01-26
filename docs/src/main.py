
class HomePage(PyFyreApp):
    def build(self):

        return Container(
            className = "flex flex-col h-screen w-full",
            children = [
                Text(
                    className="text-6xl mx-auto mt-20 font-bold px-20",
                    textContent="Build reactive static UI using Python."
                ),
                Text(
                    className="text-base mx-auto mt-5 px-52 text-center",
                    textContent="PyFyre is a web frontend framework for building reactive static user interfaces on the web using Python. PyFyre works like a charm, it transpiles your Python code into native Javascript with the help of Brython (Browser Python) Just-In-Time."
                ),
                Container(
                    className="flex flex-row mx-auto space-x-3 mt-20",
                    children = [
                        Button(
                            className="text-white font-bold bg-[#fab327] focus:ring-4 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                            textContent="Get started"
                        ),
                        Link(
                            className="text-black font-bold bg-[#f2f2f2] focus:ring-4 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                            textContent="Documentation",
                            page=DocsPage,
                            linkName="about"
                        )
                    ]
                )
            ]
        )

class DocsPage(PyFyreApp):
    def build(self):
        return Text(
            className = "hello",
            textContent = "Hello, World!"
        )

runApp(
    HomePage(),
    mount="app-mount"    
)