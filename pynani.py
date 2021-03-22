import os

# import PyNani's core modules
pynani_path = os.path.join("libs", "core")
with open(os.path.join(pynani_path, "pynani.py")) as file:
	exec(file.read())
with open(os.path.join(pynani_path, "widgets", "__init__.py")) as file:
	exec(file.read())

# import user's `main.py` file
with open("src/main.py") as file:
	exec(file.read())
