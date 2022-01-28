import os

# Import user's `src/main.py` file
with open(os.path.join("src", "__init__.py")) as file:
	exec(file.read())
