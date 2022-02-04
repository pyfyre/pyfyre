"""PyFyre States"""

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