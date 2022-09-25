from typing import Dict, List

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
# 		"title": "A PyFyre App"
# 	}
# }
ROUTES: Dict[str, Dict[str, str]] = {
	"/": {
		"title": "A PyFyre App"
	},
	"/about": {
		"title": "About Page"
	}
}

# When building your app, PyFyre makes your CPython packages installed by pip
# usable for the web. Just add the name of the pip package in the list.
#
# Example:
# ["requests", "selenium"]
DEPENDENCIES: List[str] = [
	"overrides"
]
