from pyfyre.core.exceptions import InvalidController
from pyfyre.widgets.widget import Widget

class TextInput(Widget):
    """Creates a Text input widget.

    Parameters
    ----------
    controller : TextInputController
        TextInputController method allows you to leverage `input` HTML built-ins.

    onInput : method
        Method passed on this parameter will be called automatically
        when the user puts input to this widget.

    defaultValue : str
        Default value of the TextInput
    """
    
    def __init__(self, controller=None, onInput=None, defaultValue="", className="", multiline=False, props: dict=None):
        super().__init__("input" if not multiline else "textarea", className=className, props=props)
        self.controller = controller
        self.onInput = onInput
        self.defaultValue = defaultValue
    
    def dom(self):
        element = super().dom()

        element.value = self.defaultValue
        
        if self.controller:
            self.controller.callback(self)

            def bindController(event):
                self.controller.state = element.value

            element.bind('input', bindController)

            if self.controller.state:
                element.value = self.controller.state
        
        if self.onInput:
            
            def wrapper(event):
                self.onInput(element.value)
                
            element.bind('input', wrapper)
        
        return element

class TextInputController:
    """
    TextInputController, used to leverage HTML `input` built-ins.
    
    To use this, you must initialize this on the `__init__` method of
    your component and pass the variable on the TextInput as a controller.

    Methods
    -------
    changeAttribute(readOnly=False, disabled=False)
        Change an attribute of TextInput.

    Properties
    ----------
    value -> str
        returns a string of the current value of the TextInput
    """

    def __init__(self):
        self.this = None
        self.state = None
        
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
        
    @property
    def value(self):
        return self.this.element.value

    def setValue(self, newValue):
        self.state = newValue