from browser import ajax

#
class Ajax:
    def get(url, then):
        req = ajax.ajax()
        req.open('GET', url, True)
        req.bind('complete', then)
        req.set_header('content-type','application/x-www-form-urlencoded')
        req.send()