# standard imports
from abc import ABC, abstractmethod
from typing import Optional, Callable
from pyf_modules.pyfyre import runApp

# third-party imports #
from browser import document

class UsesState(ABC):
    
    @abstractmethod
    def build(self):
        pass
    
    def update(self):
        runApp(self)
        
class Widget(ABC):
    
    def __init__ (self, tagname: str, *, className: Optional[str], props: Optional[dict]=None):
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
    
    def __init__(self, *, children: Optional[list], onClick: Optional[Callable]=None, className: Optional[str], props: Optional[dict]=None):
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
    
    def __init__(self, *, textContent: str="Button", onClick: Optional[Callable]=None, className: Optional[str], props: Optional[dict]=None):
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
    
    def __init__(self, *, textContent: str="Anchor", onClick: Optional[Callable]=None, link: str="#", className: Optional[str], props: Optional[dict]=None):
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
    
    def __init__(self, *, textContent: str="Anchor", onClick: Optional[Callable]=None, className: Optional[str], props: Optional[dict]=None):
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
    
    def __init__(self, *, src, onClick: Optional[Callable]=None, className: Optional[str], props: Optional[dict]=None):
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
    
    def __init__(self, *, textContent: str="Anchor", page: Widget, className: Optional[str], props: Optional[dict]=None):
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