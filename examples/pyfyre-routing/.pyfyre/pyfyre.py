from browser import document

def runApp(app, mount="app-mount"):
    body = document.getElementById(mount)
    body.innerHTML = ""
    body.appendChild(app.build().dom())
