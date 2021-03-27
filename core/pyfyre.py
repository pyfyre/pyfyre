import pathlib
import time
import os

class RunApp:
    def __init__(self, main_widget):
        print("Rendering...")
        self.main_widget = str(main_widget)
        self.head_count = 1
        self.body_count = 1
        self.footer_count = 1
        self.index = "..\index.html"
        self.render_file = os.path.join(pathlib.Path(__file__).parent.absolute(), "public", "index.html")
        self.file = open(self.index, "r")
        self.html_data = ""
        STARTER_HTML = ""

        # Open the Starter.html and get all the lines from it.
        with open(self.index, "r") as file:
            self.html_data = file.readlines()

            for line in self.html_data:
                if "title" in line:
                    line = "        <title>%s</title>\n" % "App Name"
                STARTER_HTML += line
            
        # This will count the index from the body
        with open(self.index, "r") as lines:
            for line in lines:
                if "body" in line:
                    break

                self.body_count += 1

        self.render()

    def render(self):
        with open(self.render_file, "w") as file:
            self.html_data.insert(self.body_count, self.main_widget)

            file.writelines(self.html_data)

            print("Rendered successfully!")


class Component:
    def __init__(self):
        # self.build() is returning a String of HTML
        self.data = self.build()

    def build(self):
        return None

    def setState(self, func):
        # TODO: Create setState()
        return None

    def __repr__(self):
        return self.data

    
