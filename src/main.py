class MyWebpage(App):
    
    def __init__(self):
        self.text = "Click me!"
    
    def build(self):
        
        def change_text(event):
            self.text = "How dare you to click me!"
            self.update() # this is necessary in order to update the webpage
        
        return Button(
            textContent=self.text,
            onClick=change_text
        )

runApp(MyWebpage())
