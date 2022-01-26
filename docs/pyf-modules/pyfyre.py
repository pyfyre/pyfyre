from browser import document, window

def runApp(app, mount="app-mount"):
    body = document.getElementById(mount)
    body.innerHTML = ""
    body.appendChild(app.build().dom())
