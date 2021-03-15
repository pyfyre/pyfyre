from shutil import copyfile
import sys
import os

print("Creating your PyNani App")

# Get the Path
PATH = os.getcwd() + "\\%s" % sys.argv[1]

# Create the Folder
os.makedirs(PATH)

# Create the SRC PATH
src_path = os.makedirs(PATH + "\\src")

# Create the Files
main = open("%s\\src\\main.py" % (PATH), "w+")
indexHTML = open("%s\\index.html" % (PATH), "w+")

# Create README.md
readme = open("%s\\README.md" % (PATH), "w+")

# Write to readme
readme.writelines("""# PyNani
Python web UI framework for building nice websites.

## THANK YOU!
Thank you for using PyNani! Your journey using PyNani begins here.

I am the creator of PyNani, Jabez Borja, I am assuming that you saw this framework in Programming Philippines group.
I, the creator of this Framework, thanks you for using or trying this Framework that I created. I appreciate it, sooo much!

If you have any questions, suggestions or bug reports about this Framework, please make an issue on Github repo, or email me at jabez.natsu@gmail.com.

Again, thank you and enjoy!

""")

# Write as the starter of Main.py
main.writelines(
"""from PyNani import PyNani, utils

pyNaniDOM = PyNani.PyNaniDOM()
utils = utils.Utils()

def HelloMessage(message):
    return utils.header1(
        text="Hello, %s!" % message,
    )

pyNaniDOM.render(
    props=[
        HelloMessage("Hello, World!"),
    ]
)
"""
)

print("App created successfully!")
