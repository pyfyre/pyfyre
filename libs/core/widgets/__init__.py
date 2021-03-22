# standard imports
from abc import ABC, abstractmethod
from typing import Optional, Callable

# third-party imports
from browser import document

class App(ABC):
    
    @abstractmethod
    def build(self):
        pass
    
    def update(self):
        runApp(self)

class Widget(ABC):
    
    def __init__ (self, tagname: str, *, props: Optional[dict]=None):
        self.tagname = tagname
        self.props = props if props is not None else {}
    
    def dom(self):
        element = document.createElement(self.tagname)
        
        for key, value in self.props.items():
            element.attrs[key] = value
        
        return element

class Button(Widget):
    
    def __init__(self, *, textContent: str="Button", onClick: Optional[Callable]=None, props: Optional[dict]=None):
        super().__init__("button", props=props)
        self.textContent = textContent
        self.onClick = onClick
    
    def dom(self):
        element = super().dom()
        element.textContent = self.textContent
        
        if self.onClick is not None:
            element.bind("click", self.onClick)
        
        return element
