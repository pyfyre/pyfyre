from typing import Any


class EmptyObject:
	def __getattr__(self, attr: str) -> Any:
		return EmptyObject()
	
	def __call__(self, *args: Any, **kwargs: Any) -> Any:
		return EmptyObject()
	
	def __getitem__(self, key: str) -> Any:
		return EmptyObject()


ROUTES = EmptyObject()
PYTHON_DEPENDENCIES = EmptyObject()
