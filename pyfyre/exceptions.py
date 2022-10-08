class PyFyreException(Exception):
	pass


class NodeNotFound(PyFyreException):
	pass


class FutureElementException(PyFyreException):
	pass


class FutureNoResult(FutureElementException):
	pass


class FutureCancelled(FutureElementException):
	pass


class FutureAlreadyDone(FutureElementException):
	pass
