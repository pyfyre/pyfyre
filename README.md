# PyFyre - The First Python Web Frontend Framework
👌 PyFyre is a web frontend framework for building static UI on the web using Python. It allows you to create UI more effectively and efficiently without leaving any language, just Python. PyFyre works like a charm, it transpiles your Python code into native Javascript with the help of Brython (Browser Python) Just-In-Time.

**NOTE**: MASTER BRANCH IS NOW ABSOLUTELY STABLE AFTER 1 YEAR OF DEVELOPMENT!!

## Stay Updated
If you would like to get updates about the PyFyre framework, we created a [Facebook Page](https://www.facebook.com/pynaniframework) where we are going to post all the updates like newly created widgets, adjustments, core updates, and more. Please consider liking it also. Thank you so much!

## Documentation
Documentation for PyFyre is still in development.

## Examples
We have examples in the [examples](examples) folder. But here is the super simple example.
See how easy it is to create a simple Hello World web app that shows Hello, World text:

```py
# Import PyFyre
class MyWebpage(PyFyreApp):
    def build(self):
        return Container(
            className = "container",
            children = [
                Text(
                    className = "title",
                    textContent = "Hello, World!"
                ),
            ]
        )

runApp(MyWebpage())
```

Rendered PyFyre:
![image](https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png)

## Installation

### Prerequisites
* python3.x

### Run The App
Running PyFyre is actually pretty simple, just run the `index.html` with a VSCode Extension Liveserver or by running it through 
```
py -m http.server
```
and here you go, you now have a PyFyre running on your web! Super simple, right? That's it.

You can now edit your PyFyre app through `src/main.py`, and see the magic.

**Note**: PyFyre may take up a seconds long to load in development because it transpile your code into native Javascript Just-In-Time!
**Important Note**: The Python Linter might react wild a little bit about PyFyre's importing mechanism, it would be fix soon. **If it works, don't touch it.**

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for contributing.
