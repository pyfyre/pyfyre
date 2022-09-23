import sys
from uuid import uuid4
from typing import Type
from types import TracebackType
from abc import ABC, abstractmethod
from typing import Optional, Dict, List
from pyfyre.widgets.texts import Paragraph
from pyfyre.widgets.base import Widget, BaseWidget


class Container(Widget):
	def __init__(
		self, *,
		props: Optional[Dict[str, str]] = None,
		children: Optional[List[BaseWidget]] = None
	):
		super().__init__("div", props=props, children=children)


class StatefulContainer(Container, ABC):
	def __init__(self, *, props: Optional[Dict[str, str]] = None):
		super().__init__(props=props, children=self._secure_build())
		self.identifier = str(uuid4())
		self.props["pyfyre-identifier"] = self.identifier
	
	@abstractmethod
	def build(self) -> List[BaseWidget]:
		raise NotImplementedError
	
	def on_build_error(
		self, exc_type: Type[BaseException],
		exc_value: BaseException, exc_traceback: TracebackType
	) -> List[BaseWidget]:
		return [
			Paragraph(exc_type),
			Paragraph(exc_value),
			Paragraph(exc_traceback)
		]
	
	def _secure_build(self) -> List[BaseWidget]:
		try:
			return self.build()
		except BaseException:
			return self.on_build_error(*sys.exc_info())
	
	def update(self) -> None:
		self.children = self._secure_build()
		
		# Importing inside this method due to circular import problem
		from pyfyre.virtual_dom import VirtualDOM
		VirtualDOM.update(self)
