# Welcome to PyFyre Contributing Guide
As an open-source project, PyFyre welcomes contributions of any form.  
When contributing to this repository, please first discuss the change you wish to make via [issue](https://github.com/pyfyre/pyfyre/issues), [discussion](https://github.com/pyfyre/pyfyre/discussions), or any other method with the owners of this repository before making a change.

Thank you for investing your time in contributing to our project!

## Before Starting
- Install the required packages for development.
```bash
pip install -r requirements.txt
pip install -r dev_requirements.txt
```
- This codebase uses [Black](https://github.com/psf/black) Python code formatter.
  You may install Black on your code editor or IDE.
- This codebase uses [Mypy](http://mypy-lang.org/) Python static type checker.
  Make sure to apply type hinting and annotations in your code.
  You may install Mypy on your code editor or IDE.
- Read the module docstring of [dev.py](dev.py).

## Python Code Style
The following items apply to all Python modules inside this project.
- The code is formatted using [Black](https://github.com/psf/black).
- Docstrings use [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

## Pull Request
Make sure to do the following items before making a pull request.
- Format your code using [Black](https://github.com/psf/black).
  You may run `black .` on your command line in the directory of this project.
- Run `mypy .` on your command line in the directory of this project to type check your code.

## Project Directory
- [**pyfyre**](pyfyre)  
Core files of PyFyre.
- [**pyfyre_cli**](pyfyre_cli)  
Command-line interface for using PyFyre.

## Code of Conduct
Please note that we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project to keep our community approachable and respectable.
