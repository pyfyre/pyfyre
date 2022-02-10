from pyfyre.core.exceptions import InvalidController
from pyfyre.widgets.widget import Widget

class TextInput(Widget):
    """Creates a Text input widget.

    Parameters
    ----------
    onInput : method
        Method passed on this parameter will be fired automatically
        when the user puts input to this widget.
    """
    
    def __init__(self, controller=None, onInput=None, className="", props: dict=None):
        super().__init__("input", className=className, props=props)
        self.controller = controller
        self.onInput = onInput
    
    def dom(self):
        element = super().dom()

        if self.controller:
            self.controller.callback(self)
        
        if self.onInput:
            
            def wrapper(event):
                self.onInput(element.value)
                
            element.bind('input', wrapper)
        
        return element

class TextInputController:
    def __init__(self):
        self.this = None
        
        # TextInput attributes
        self.readOnly = False
        self.disabled = False

    def changeAttribute(self, readOnly=False, disabled=False):
        if not self.this or not isinstance(self.this, TextInput):
            raise InvalidController("Looks like you haven't called this controller as a parameter controller of TextInput or you provided an invalid controller.")

        self.readOnly = readOnly
        self.disabled = disabled

        if self.readOnly:
            self.this.element.attrs['readonly'] = None
        else:
            if 'readonly' in self.this.element.attrs:
                del self.this.element.attrs['readonly']

        if self.disabled:
            self.this.element.attrs['disabled'] = None
        else:
            if 'disabled' in self.this.element.attrs:
                del self.this.element.attrs['disabled']

    def callback(self, this: TextInput):
        """
        This is called when this TextInputController object
        is passed as a parameter Controller of TextInput widget.
        """
        self.this = this
        