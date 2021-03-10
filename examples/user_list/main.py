from pynani.pyNani.core import PyNani
import time

pn = PyNani.PyNani(
    file="lib/templates/index.html",
    title="User List"
)

users = ["Jabez", "Valerie", "Jeremy", "Arah", "Jacob", "Jhonna"]

for user in users:
    pn.header1(
        text=user,
        styles=[
            "text-alignment: center"
        ]
    )

    time.sleep(1)