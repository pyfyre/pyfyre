import sys
from pyfyre.styles import Style
from browser import DOMEvent, aio
from pyfyre.nodes import Node, Element
from typing import Optional, Dict, List, Callable


class ListBuilder(Element):
	def __init__(
		self, children_builder: Callable[[int], Optional[Node]], *,
		count: Optional[int] = None,
		max_height: str = "300px",
		render_batch: int = 10,
		render_interval: float = 0,
		styles: Optional[List[Style]] = None,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		styles = styles or []
		self.children_builder = children_builder
		self.count = count
		self.render_batch = render_batch
		self.render_interval = render_interval
		
		self.index = 0
		self.rendered_children: List[Node] = []
		
		super().__init__(
			"div", lambda: self.rendered_children, attrs=attrs,
			styles=[Style(
				overflow_y="scroll",
				overflow_wrap="break-word",
				max_height=max_height
			)] + styles
		)
		
		def render_nodes(event: DOMEvent) -> None:
			el = event.target
			if el.scrollHeight - el.scrollTop - el.clientHeight < 1:
				prev_index = self.index
				self.render_next_children()
				
				if self.index > prev_index:
					render_nodes(event)
		
		self.add_event_listener("scroll", render_nodes)
	
	def render_next_children(self) -> None:
		for _ in range(self.render_batch):
			if self.count:
				if self.index >= self.count:
					break
			
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
