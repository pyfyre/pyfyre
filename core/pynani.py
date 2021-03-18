import pathlib

class RunApp:
    def __init__(self, main_widget):
        print("Rendering...")
        self.main_widget = str(main_widget)
        self.head_count = 1
        self.body_count = 1
        self.footer_count = 1
        self.file = "..\index.html"
        self.index = open(self.file, "r")
        STARTER_HTML = ""

        # Open the Starter.html and get all the lines from it.
        with open("%s\\starter.html" % pathlib.Path(__file__).parent.absolute(), "r") as file:
            html_data = file.readlines()

            for line in html_data:
                if "title" in line:
                    line = "        <title>%s</title>\n" % "App Name"
                STARTER_HTML += line

        # And it will add it on index.html
        with open(self.file, "w") as file:
            file.write(STARTER_HTML)
            
        # This will count the index from the body
        with open(self.file, "r") as lines:
            for line in lines:
                if "body" in line:
                    break

                self.body_count += 1

        self.render()

    def render(self):
        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count, self.main_widget)

            file.writelines(filedata)

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

    
