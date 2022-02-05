from pyfyre.widgets.widget import Widget

class ListBuilder(Widget):
    """Creates a ListBuilder widget.

    This is like for loops in programming languages,
    you provide a range (count for instance)
    and the content of the loop (builder for instance).

    The widget returned on the [builder] will be appended
    to the DOM for [count] times.

    Attributes
    ----------
    count : int
        How many times will the ListBuilder [build] method
        will run?
    builder : method -> Widget
        The widget that will append in [count] times.
    """
    
    def __init__(self, count=1, builder=None, className="", props: dict=None):
        super().__init__("div", className=className, props=props)
        self.count = count
        self.builder = builder
    
    def dom(self):
        element = super().dom()
        
        for i in range(self.count):
            element.appendChild(self.builder(i).dom())
        
        return element
