from browser import document

def runApp(app):
    body = document.select("body")[0]
    body.innerHTML = ""
    body.appendChild(app.build().dom())
