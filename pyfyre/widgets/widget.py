from browser import document

class Widget:
    
    def __init__ (self, tagName: str, *, children: list = [], attrs: dict=None):
        self.tagName = tagName
        self.children = children
        self.attrs = attrs if attrs is not None else {}
    
    def dom(self):

        children = self.patchChildren()

        return {
            "tagName": self.tagName,
            "children": children,
            "attrs": self.attrs
        }

    def patchChildren(self):

        if isinstance(self.children, str):
            return self.children

        children = []

        for child in self.children:
            children.append(child.dom())

        return children