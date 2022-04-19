from browser import document

class Widget:
    
    def __init__ (self, tagName: str, *, className: str, children=None, props: dict={}):
        self.tagName = tagName
        self.className = className
        self.children = children
        self.props = props
    
    def dom(self):

        children = self.patch()

        return {
            "tagName": self.tagName,
            "children": children,
            "props": self.props
        }

    def patch(self):
        
        oldProps = self.props
        self.props = {"class": self.className}

        for k, v in oldProps.items():
            self.props[k] = v

        if isinstance(self.children, str):
            return self.children

        if isinstance(self.children, list):

            children = []

            for child in self.children:
                children.append(child.dom())
                
            return children

        return str(self.children)

class PropObj:
    def __init__(self, props):
        self.props = props