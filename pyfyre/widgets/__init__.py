# standard imports
from pyfyre.pyfyre import runApp

# third-party imports #
from browser import document

class PyFyreApp:
    
    def build(self):
        pass
    
    def update(self):
        runApp(self)
        
class Widget:
    
    def __init__ (self, tagname: str, *, className, props=None):
        self.tagname = tagname
        self.className = className
        self.props = props if props is not None else {}
    
    def dom(self):
        element = document.createElement(self.tagname)
        element.className = self.className
        
        for key, value in self.props.items():
            element.attrs[key] = value
        
        return element

class Container(Widget):
    
    def __init__(self, *, children, onClick=lambda: print("Click!"), className, props=None):
        super().__init__("div", className=className, props=props)
        self.children = children
        self.onClick = onClick
    
    def dom(self):
        element = super().dom()
        
        if self.onClick is not None:
            element.bind("click", self.onClick)
        
        for child in self.children:
            element.appendChild(child.dom())
        
        return element

class Button(Widget):
    
    def __init__(self, *, textContent: str="Button", onClick=lambda: print("Click!"), className, props):
        super().__init__("button", className=className, props=props)
        self.textContent = textContent
        self.onClick = onClick
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        
        if self.onClick is not None:
            element.bind("click", self.onClick)
        
        return element

class Anchor(Widget):
    
    def __init__(self, *, textContent: str="Anchor", onClick=lambda: print("Click!"), link: str="#", className, props=None):
        super().__init__("a", className=className, props=props)
        self.textContent = textContent
        self.onClick = onClick
        self.link = link
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        element.href = self.link
        
        if self.onClick is not None:
            element.bind("click", self.onClick)
        
        return element

class Text(Widget):
    
    def __init__(self, *, textContent: str="Anchor", onClick=lambda: print("Click!"), className, props=None):
        super().__init__("p", className=className, props=props)
        self.textContent = textContent
        self.onClick = onClick
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        
        if self.onClick is not None:
            element.bind("click", self.onClick)
        
        return element


class Image(Widget):
    
    def __init__(self, *, src, onClick=lambda: print("Click!"), className, props=None):
        super().__init__("img", className=className, props=props)
        self.src = src
        self.onClick = onClick
    
    def dom(self):
        element = super().dom()
        element.src = self.src
        
        if self.onClick is not None:
            element.bind("click", self.onClick)
        
        return element

class Link(Widget):
    
    def __init__(self, *, textContent: str="Anchor", page: Widget, className, props=None):
        super().__init__("a", className=className, props=props)
        self.textContent = textContent
        self.page = page
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        element.href = "#"
        
        element.bind("click", self.navigate)
        
        return element

    def navigate(self, e):
        runApp(self.page())