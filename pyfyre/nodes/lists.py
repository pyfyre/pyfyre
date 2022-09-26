from browser import DOMEvent, aio
from pyfyre.events import EventType
from pyfyre.nodes import Node, Division
from typing import Optional, Dict, List


class ListBuilder(Division):
	def __init__(
		self, *,
		max_height: str = "300px",
		render_batch: int = 10,
		render_interval: float = 0.1,
		attrs: Optional[Dict[str, str]] = None,
		children: Optional[List[Node]] = None
	) -> None:
		self.unrendered_children = children or []
		self.rendered_children: List[Node] = []
		
		super().__init__(attrs=attrs, children=lambda: self.rendered_children)
		self.dom.style.overflow = "scroll"
		self.dom.style.maxHeight = max_height
		
		def render_child() -> None:
			for _ in range(render_batch):
				try:
					child = self.unrendered_children.pop(0)
				except IndexError:
					return
				
				self.rendered_children.append(child)
			
			self.update_dom()
		
		async def render_children() -> None:
			if self.dom.scrollHeight == self.dom.clientHeight:
				render_child()
				await aio.sleep(render_interval)
				await render_children()
		
		def render_nodes(event: DOMEvent) -> None:
			el = event.target
			if el.scrollHeight - el.scrollTop - el.clientHeight < 1:
				render_child()
		
		aio.run(render_children())
		self.add_event_listener(EventType.Scroll, render_nodes)
