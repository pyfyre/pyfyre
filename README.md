# PyFyre
👌 PyFyre is a web frontend framework for building static UI on the web using Python. It allows you to create UI more effectively and efficiently without leaving any language, just Python. PyFyre works like a charm, it compiles your Python code into Raw HTML, CSS, and Javascript and render it on the web. It use Brython for Javascript communication.

Note: Master Branch is not stable, if you want to use PyFyre please use Stable branch.

## Stay Updated
If you would like to get updates about the PyFyre framework, we created a [Facebook Page](https://www.facebook.com/pynaniframework) where we are going to post all the updates like newly created widgets, adjustments, core updates, and more. Please consider liking it also. Thank you so much!

## Documentation
Documentation for PyFyre is still in development.

## Examples
We have examples in the [examples](examples) folder. But here is the super simple example.
See how easy it is to create a simple Hello World web app that shows Hello, World text:

```py
# Import PyNani
from pynani.core.pynani import Component, RunApp
from pynani.core.widgets import Widgets

widgets = Widgets()

class MyApp(Component):
    def build(self):
        return widgets.header1(text="Hello, World!", styles=["margin-top: 10px"])

RunApp(MyApp())
```


Rendered PyNani:
![image](https://user-images.githubusercontent.com/64759159/111881940-d80e4380-89ed-11eb-9ffc-d607d80896fb.png)


## Installation

### Prerequisites
* python3.x

### Windows
Create a folder called `pyfyre` on your `C:\` folder.
```
C:\pyfyre\
```
Get the source code from PyNani repo on GitHub.
```
C:\pynani> git clone https://github.com/jabezborja/pynani.git -b stable
```
#### Update Your Path
If you wish to run PyFyre commands in the regular Windows console, take these steps to add Pyfyre to the PATH environment variable:

* From the Start search bar, enter ‘env’ and select Edit environment variables for your account and click Environment Variables in the bottom right.
* Under User variables check if there is an entry called Path:
-   If there is path, double click into it, and click ```new``` then type ```C:\pyfyre\pyfyre\bin```.
-   If there is none, click ```new``` and type ```Path``` as the Variable name and ```C:\pyfyre\pyfyre\bin``` as value.

### Linux
Get the source code from PyNani repo on GitHub.
```bash
git clone https://github.com/pyfyre/pyfyre.git -b stable
```

Make the [pynani.py](bin/pynani.py) an executable file.
```bash
chmod +x pyfyre/bin/pynani.py
```

#### Update Your Path
If you wish to run PyFyre on any directory, take these steps to add PyFyre to the PATH environment variable:

* Go to your home directory by typing the `cd` command.
* Then find the `.bashrc` file and insert the following:
```bash
export PATH=$PATH:<path_to_PyNani>/bin
```
* Restart your terminal or you could do the following:
```bash
source ~/.bashrc
```

### Create an App
To create a Web App, go to the folder where you want PyFyre to install in then go to CMD or command line and type:
```
pynani.py create-app <App_Name>
```

in real world example, it should be:
```
pynani.py create-app my_cool_app
```

Then it will create a boilerplate code for you.

Now, locate to your created folder called the app name you entered. Then type in the Command Line or CMD:
```
py -m venv env
```
This command creates a environment for your app. 

It should take few seconds or minutes. Once it's done, go to the ```C:\pyfyre\``` and clone the PyNani folder to ```env\lib\site-packages```.

And type:
```
env\scripts\activate
```
To activate your virtual environment.

For Hot Reload, you need to install a package called ```Watchdog``` for file changes watcher. To install that type 
```
pip install watchdog
```
It will install and wait for few seconds.

Now, locate to the main workspace navigate to ```src``` folder and type:
```
pynani.py runserver
```
It will run the watchdog and now the HOT RELOAD is now HOT!!!

To make your website live on your local machine, you can use XAMPP or Live Server in VSCode

#### Live Server
Install VSCode or Visual Studio Code on your PC.

Once you have the VS Code go to extensions, you can see it on your left then click the 4 blocks logo. Then type: ```Live Server```

and it will install.

Now, open your PyNani App folder on VSCode by typing on CMD located on your PyNani Folder:
```
C:\users\<your_username>\desktop\pynani>code .
```
it will load for few seconds and click ```Go Live``` on bottom right.

#### XAMPP
See https://www.apachefriends.org/index.html

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for this.
