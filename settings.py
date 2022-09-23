"""
	Settings for building the development environment `__dev__`
	when `dev.py` is run
"""

from typing import Dict

# This is used for building the application.
# PyFyre creates HTML files based on these routes.
# So that when a user navigates to a certain route,
# the corresponding page is returned.
ROUTES: Dict[str, Dict[str, str]] = {
	"/": {
		"title": "A PyFyre App"
	},
	"/about": {
		"title": "About Page"
	}
}
