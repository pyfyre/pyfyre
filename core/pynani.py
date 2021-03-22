# standard imports
import pathlib
import os

# third-party imports
from browser import document, window, alert

def RunApp(app_widget):
    body = document.select("body")[0]
    # body.innerHTML = ""
    body.appendChild(app_widget.render())
