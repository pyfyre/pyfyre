from browser import document

class Widget:
    
    def __init__ (self, tagname: str, *, className, props: dict=None):
        self.tagname = tagname
        self.className = className
        self.element = None
        self.props = props if props is not None else {}
    
    def dom(self):
        element = document.createElement(self.tagname)
        element.className = self.className

        self.element = element
        
        for key, value in self.props.items():
            element.attrs[key] = value
        
        return element