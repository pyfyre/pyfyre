## PyNani
PyNani is a Python web user interface framework for building reactive static websites and for those Python devs who hates HTML. Pynani is free and open source project.

## Documentation
Documentation for PyNani is still in development.

## Examples
We have examples in ```/examples``` folder. But here is the super simple example:

```py
# Import PyNani
from pynani.PyNani.core import PyNani, utils

# Creates an instance for PyNaniDOM
pyNaniDOM = PyNani.PyNaniDOM()
# Also here.
utils = utils.Utils()

## Creates a function returning a header1, it is equal to
## <h1> in HTML, utils.header1 is finding arguments:
## (text[String], onClick[Javascript function], styles[List of CSS styles])
def HelloMessage(message):
    return utils.header1(
        text="Hello, %s!" % message,
    )

## Here where all UI began to render in the screen.
## render is finding argument called props:
## (props[list of elements to render])
pyNaniDOM.render(
    props=[
        HelloMessage("Jabez"),
    ]
)
```
Rendered PyNani:
![image](https://user-images.githubusercontent.com/64759159/111185923-76b13380-85ed-11eb-98a4-7e707a7d8ba8.png)


## Installation
Install Python3 on your local machine/PC.

Create a folder called 'PyNani' on your C:\ folder.
```
C:\pynani\
```
Get the source code from PyNani repo on GitHub.
```
C:\pynani>git clone https://github.com/jabezborja/pynani.git -b stable
```
### Update your path
If you wish to run PyNani commands in the regular Windows console, take these steps to add PyNani to the PATH environment variable:

* From the Start search bar, enter ‘env’ and select Edit environment variables for your account and click Environment Variables in the bottom right.
* Under User variables check if there is an entry called Path:
-   If there is path, double click into it, and click ```new``` then type ```C:\pynani\PyNani\bin```.
-   If there is none, click ```new``` and type ```Path``` as the Variable name and ```C:\pynani\PyNani\bin``` as value.

And now, you have the PyNani on your local machine!

### Create an App
To create a Web App, go to the folder where you want PyNani to install in then go to CMD or command line and type:
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

It should take few seconds or minutes. Once it's done, go to the ```C:\pynani\``` and clone the PyNani folder to ```env\lib\site-packages```.

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

Once you have the VS Code go to extensions, you can see it on your left then click the 4 blocks logo. Then type:
```
Live Server
```

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
