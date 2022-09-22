from uuid import uuid4
from abc import ABC, abstractmethod
from typing import Optional, Dict, List
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
		super().__init__(props=props, children=self.build())
		self.identifier = str(uuid4())
		self.props["pyfyre-identifier"] = self.identifier
	
	@abstractmethod
	def build(self) -> List[BaseWidget]:
		raise NotImplementedError
	
	def update(self) -> None:
		self.children = self.build()
		
		# Importing inside this method due to circular import problem
		from pyfyre.virtual_dom import VirtualDOM
		VirtualDOM.update(self)
