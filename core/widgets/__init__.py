class Widgets:
    def __init__(self): pass
    def container(self, child="", onClick="", styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        onclick = " onclick=\"%s\"" % onClick if not onClick == "" else ""
        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        child = child if not child == "" else ""
        
        data = """<div%s%s>
        %s
        </div>""" % (onclick, html_style, child)

        return data

    def column(self, children=[], styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        childrens = ""
        
        for child in children:
            childrens += child + "\n"

        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        childrens = childrens if not childrens == [] else ""

        data = """<div %s>
            %s
        </div>
        """ % (html_style, childrens)
        
        return data

    def header1(self, text="", onClick="", styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        onclick = " onclick=\"%s\"" % onClick if not onClick == "" else ""
        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        
        data = "<h1%s%s>%s</h1>" % (onclick, html_style, text)

        return data

    def button(self, text="", onClick="", styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        onClick = " onclick=\"%s\"" % onClick if not onClick == "" else ""
        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        
        data = "<button type=\"Button\"%s>%s</button>" % (html_style, text)

        return data

    def paragraph(self, text="", onClick="", styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        onclick = " onclick=\"%s\"" % onClick if not onClick == "" else ""
        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        
        data = "<p%s%s>%s</p>\n" % (onclick, html_style, text)

        return data

    def link(self, link="#", text="", onClick="", styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        link = " href=\"%s\"" % link if not link == "" else ""
        onclick = " onclick=\"%s\"" % onClick if not onClick == "" else ""
        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        
        data = "<a%s%s%s>%s</a>\n" % (link, onclick, html_style, text)

        return data

    def span(self, text="", onClick="", styles=[]):
        gathered_style = ""

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        onclick = " onclick=\"%s\"" % onClick if not onClick == "" else ""
        html_style = " style=\"%s\"" % gathered_style if not gathered_style == "" else ""
        
        data = "<span%s%s>%s</span>\n" % (onclick, html_style, text)

        return data

    def listViewBuilder(self, count=0, builder=[], styles=[]):
        build_data = ""
        gathered_style = ""
        build = [] 

        for i in range(count):
            build.append(builder[0](i))

        # Get every styles
        for style in styles:
            gathered_style += "%s; " % style

        html_style = " style=\"%s\"" % gathered_style

        for built in build:
            build_data += built + "\n"
        
        data = "<div%s>%s</div>" % (html_style, build_data)

        return data