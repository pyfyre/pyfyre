# PyNani
PyNani is a Python web framework for building UI on the web with just one language, Python. Pynani is free and open source project.

Note: `master` branch is not stable, if you want to use PyNani please use the `stable` branch, thank you!

## Stay Updated
If you would like to get updates about PyNani framework, we created a [Facebook Page](https://www.facebook.com/pynaniframework) where we are going to post all the updates like newly created widgets, adjustments, core updates, and more. Please consider liking it also. Thank you so much!

## Documentation
Documentation for PyNani is still in development.

## Examples
We have examples in the [examples](examples) folder. But here is the super simple example.

```py
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
```

Rendered PyNani:
![image](https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png)

## Installation
```bash
git clone https://github.com/jabezborja/pynani.git -b stable
```

## Running the App
You could serve the [index.html](index.html) by using the built-in PyNani live server.

Install the [livereload](https://livereload.readthedocs.io/en/latest/) Python module.
```bash
pip install livereload
```

Serve the [index.html](index.html) file.
```bash
python liveserver.py
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for this.
