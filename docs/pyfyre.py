import os
import time

process_time_ms = time.time() * 1000

# import PyFyre's core modules
pyfyre_path = os.path.join("pyf-modules")
with open(os.path.join(pyfyre_path, "pyfyre.py")) as file:
	exec(file.read())
with open(os.path.join(pyfyre_path, "widgets", "__init__.py")) as file:
	exec(file.read())
with open(os.path.join(pyfyre_path, "ajax", "__init__.py")) as file:
	exec(file.read())

# import user's `src/main.py` file
with open(os.path.join("src", "main.py")) as file:
	exec(file.read())

print(f"PYTHON PROCESS TIME: {time.time() * 1000 - process_time_ms}ms")
