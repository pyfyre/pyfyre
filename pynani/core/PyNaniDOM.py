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

class PyNaniDOM:
    def __init__(self):
        self.head_count = 1
        self.body_count = 1
        self.footer_count = 1
        self.counter_from_body = 0
        self.file = "..\index.html"
        
        self.index = open(self.file, "r")

        with open(self.file, "w") as file:
            file.write(STARTER_HTML % "My PyNani App")
            
        with open(self.file, "r") as lines:
            for line in lines:
                if "body" in line:
                    break

                self.body_count += 1
    
    def render(self, props=[]):
        data = ""

        for prop in props:
            data += "       " + prop + "\n"

        with open(self.file, "r") as file:
            filedata = file.readlines()

        with open(self.file, "w") as file:
            filedata.insert(self.body_count + self.counter_from_body, data)

            file.writelines(filedata)

        self.counter_from_body += 1