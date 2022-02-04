from browser import ajax

class Ajax:
    """
    Access Brython builtin Ajax.
    """

    def get(url, mode="json", then=None):
        req = ajax.get(url, mode=mode, oncomplete=then)