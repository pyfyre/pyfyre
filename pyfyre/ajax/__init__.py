from browser import ajax

class Ajax:
    """Access Brython builtin Ajax.

    ...

    Methods
    -------
    get(url, mode="json", then=None)
        Request a GET method to the url provided after the
        request, the [then] method will be fired.

    GET Parameters
    --------------
    url : str
        The URL where to request the GET
    mode : str
        Mode of the request
    then : method
        After the request, the [then] method provided
        will be fired passing the request object as the
        argument.
    """

    @staticmethod
    def get(url, mode="json", then=None):
        """Request a GET method to the url provided after the
        request, the [then] method will be fired.

        Parameters
        ----------
        url : str
            The URL where to request the GET
        mode : str
            Mode of the request
        then : method
            After the request, the [then] method provided
            will be fired passing the request object as the
            argument.
        
        """
        ajax.get(url, mode=mode, oncomplete=then)