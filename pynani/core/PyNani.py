
STARTER_HTML = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>%s</title>
    </head>
    <body>
        
    </body>
    <footer>
    </footer>
    <style>
        body {
            padding: 0;
            margin: 0;
        }
    </style>
</html>
"""

class PyNani:
    def __init__(self, file="", title="My First Nani App"):
        self.title = title
        self.head_count = 1
        self.body_count = 1
        self.footer_count = 1
        self.counter_from_body = 0
        self.file = file
        
        self.index = open(self.file, "r")

        with open(self.file, "w") as file:
            file.write(STARTER_HTML % self.title)
            
        with open(self.file, "r") as lines:
            for line in lines:
                if "body" in line:
                    break

                self.body_count += 1

    def body(self):
        # TODO: Create some styling ability to body
        data = ""

    def container(self, onClick="", styles=[], child=""):
        # TODO: DIV CHILD
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s " % style

        html_style = "style=\"%s\"" % gathered_style
        

        data = "        <div %s %s >\n          %s\n        </div>\n" % (onclick, html_style, child)

        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count + self.counter_from_body, data)

            file.writelines(filedata)

        self.counter_from_body += 1

    def header1(self, text="", onClick="", styles=[]):
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s " % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "        <h1 %s %s >%s</h1>\n" % (onclick, html_style, text)

        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count + self.counter_from_body, data)

            file.writelines(filedata)

        self.counter_from_body += 1

    def paragraph(self, text="", onClick="", styles=[]):
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s " % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "        <p %s %s >%s</p>\n" % (onclick, html_style, text)

        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count + self.counter_from_body, data)

            file.writelines(filedata)

        self.counter_from_body += 1

    def link(self, text="", link="", onClick="", styles=[]):
        link = "href=\"%s\"" % link
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s " % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "        <a %s %s %s >%s</a>\n" % (link, onclick, html_style, text)

        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count + self.counter_from_body, data)

            file.writelines(filedata)

        self.counter_from_body += 1

    def span(self, text="", onClick="", styles=[]):
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s " % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "        <span %s %s >%s</span>\n" % (onclick, html_style, text)

        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count + self.counter_from_body, data)

            file.writelines(filedata)

        self.counter_from_body += 1

    