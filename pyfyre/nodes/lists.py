import sys
from pyfyre.styles import Style
from browser import DOMEvent, aio
from pyfyre.nodes import Node, Element
from pyfyre.events import ElementEventType
from typing import Optional, Dict, List, Callable


class ListBuilder(Element):
	def __init__(
		self, children_builder: Callable[[int], Optional[Node]], *,
		max_height: str = "300px",
		render_batch: int = 10,
		render_interval: float = 0,
		styles: Optional[List[Style]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		self.attrs = attrs or {}
		self.children_builder = children_builder
		self.render_batch = render_batch
		self.render_interval = render_interval
		
		self.index = 0
		self.rendered_children: List[Node] = []
		
		if "style" in self.attrs:
			self.attrs["style"] += "; overflow-y: scroll; " +\
				f"overflow-wrap: break-word; max-height: {max_height};"
		else:
			self.attrs["style"] = "overflow-y: scroll; " +\
				f"overflow-wrap: break-word; max-height: {max_height};"
		
		super().__init__(
			"div", lambda: self.rendered_children, styles=styles, attrs=self.attrs
		)
		
		def render_nodes(event: DOMEvent) -> None:
			el = event.target
			if el.scrollHeight - el.scrollTop - el.clientHeight < 1:
				prev_index = self.index
				self.render_next_children()
				
				if self.index > prev_index:
					render_nodes(event)
		
		self.add_event_listener(ElementEventType.scroll, render_nodes)
	
	def render_next_children(self) -> None:
		for _ in range(self.render_batch):
			try:
				child = self.children_builder(self.index)
			except BaseException:
				error_children = self.on_build_error(*sys.exc_info())
				child = Element("div", lambda: error_children)
			
			if child is None:
				break
			
			self.rendered_children.append(child)
			self.index += 1
		
		self.update_dom()
	
	def build_children(self) -> None:
		async def async_wrapper() -> None:
			while self.dom.scrollHeight == self.dom.clientHeight:
				self.render_next_children()
				await aio.sleep(self.render_interval)
		
		super().build_children()
		aio.run(async_wrapper())
