class Utils:
    def __init__(self):
        pass

    def header1(self, text="", onClick="", styles=[]):
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s;" % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "<h1 %s %s >%s</h1>\n" % (onclick, html_style, text)

        return data

    def paragraph(self, text="", onClick="", styles=[]):
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s;" % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "<p %s %s >%s</p>\n" % (onclick, html_style, text)

        return data

    def link(self, link="#", text="", onClick="", styles=[]):
        link = "href=\"%s\"" % link
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s;" % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "<a %s %s %s >%s</a>\n" % (link, onclick, html_style, text)

        return data

    def span(self, text="", onClick="", styles=[]):
        onclick = "onclick=\"%s\"" % onClick
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s;" % style

        html_style = "style=\"%s\"" % gathered_style
        
        data = "<span %s %s >%s</span>\n" % (onclick, html_style, text)

        return data