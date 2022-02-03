# standard imports
from pyfyre.pyfyre import runApp
from pyfyre.globals import Globals

# third-party imports #
from browser import document, window
from pyfyre.router import Router

class UsesState:

    def __init__(self):
        self.domElement = None
    
    def build(self):
        pass

    def dom(self):
        self.domElement = self.build().dom()
        return self.domElement

    def update(self):
        """
        Updates the DOM element. Instead of painting the app again
        for state change, only update the DOM where the change happens.
        """
        
        parentNode = self.domElement.parentNode
        self.domElement.remove()
        self.domElement = self.dom()
        parentNode.appendChild(self.domElement)

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


class Container(Widget):
    
    def __init__(self, children=[], className="", props: dict=None):
        super().__init__("div", className=className, props=props)
        self.children = children
    
    def dom(self):
        element = super().dom()
        
        for child in self.children:
            element.appendChild(child.dom())
        
        return element

class Button(Widget):
    
    def __init__(self, textContent, onClick=lambda: print(""), className="", props: dict=None):
        super().__init__("button", className=className, props=props)
        self.textContent = textContent
        self.onClick = onClick
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent

        element.bind("click", self.onClick)
        
        return element

class Anchor(Widget):
    
    def __init__(self, textContent, link: str="#", className="", props: dict=None):
        super().__init__("a", className=className, props=props)
        self.textContent = textContent
        self.link = link
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        element.href = self.link
        
        return element

class Text(Widget):
    
    def __init__(self, textContent: str, className="", props: dict=None):
        super().__init__("p", className=className, props=props)
        self.textContent = textContent
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        
        return element


class Image(Widget):
    
    def __init__(self, src, className="", props: dict=None):
        super().__init__("img", className=className, props=props)
        self.src = src
    
    def dom(self):
        element = super().dom()
        element.src = self.src
        
        return element

class Link(Widget):
    
    def __init__(self, textContent: str, to='/', className="", props: dict=None):
        super().__init__("a", className=className, props=props)
        self.textContent = textContent
        self.to = to
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        element.href = "#"
        
        element.bind("click", self.navigate)
        
        return element

    def navigate(self, e):
        e.preventDefault()
        Router.push(self.to)

class ListBuilder(Widget):
    
    def __init__(self, count=1, builder=None, className="", props: dict=None):
        super().__init__("div", className=className, props=props)
        self.count = count
        self.builder = builder
    
    def dom(self):
        element = super().dom()
        
        for i in range(self.count):
            element.appendChild(self.builder(i).dom())
        
        return element
