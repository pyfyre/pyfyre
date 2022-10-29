from typing import Dict, List, Any

# When building your app, PyFyre creates HTML files based on these routes,
# so that when a user visits your website,
# the corresponding page of the route is returned.
# Once the initial page has been loaded,
# PyFyre will take over the routing as a single-page application.
#
# -> A user visits "https://your-pyfyre-app.com/about".
# -> The server returns the `about/index.html`.
# -> PyFyre takes over the page routing
#    by preventing further navigation to internal links.
# -> The user clicks an internal link "https://your-pyfyre-app.com/home".
# -> PyFyre prevents the navigation and modifies the DOM
#    to render the corresponding view of the route "/home".
#
# Example:
# {
# 	"/": {
# 		"title": "A PyFyre App",
# 		"icon": "/favicon.ico",
# 		"head": ['<link rel="stylesheet" href="/style.css" />']
# 	}
# }
ROUTES: Dict[str, Dict[str, Any]] = {
    "/": {
        "title": "A PyFyre App",
        "icon": "/favicon.ico",
        "head": ['<link rel="stylesheet" href="/style.css" />'],
    }
}

# When building your app, PyFyre makes your CPython packages installed by pip
# usable for the web. Just add the name of the pip package in the list.
#
# !!! Note that it is not possible to import every CPython package
# due to Brython limitations. Read the Brython documentation:
# https://www.brython.info/static_doc/en/faq.html#:~:text=Q%20%3A%20can%20I%20import%20all%20the%20modules%20/%20packages%20that%20run%20with%20CPython%20%3F
#
# Example:
# [
# 	"text_generator",
# 	"random_string",
# 	"url64"
# ]
PYTHON_DEPENDENCIES: List[str] = []
