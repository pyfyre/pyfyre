__all__ = [
	"PyFyreException",
	"NodeNotFound"
]


class PyFyreException(Exception):
	pass


class NodeNotFound(PyFyreException):
	pass
