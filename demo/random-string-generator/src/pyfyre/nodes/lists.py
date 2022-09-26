from browser import DOMEvent, aio
from pyfyre.events import EventType
from pyfyre.nodes import Node, Element
from typing import Optional, Dict, List, Callable


class ListBuilder(Element):
	def __init__(
		self, children_builder: Callable[[int], Optional[Node]], *,
		max_height: str = "300px",
		render_batch: int = 10,
		render_interval: float = 0.1,
		attrs: Optional[Dict[str, str]] = None
	) -> None:
		self.rendered_children: List[Node] = []
		
		super().__init__("div", attrs=attrs, children=lambda: self.rendered_children)
		self.dom.style.overflowY = "scroll"
		self.dom.style.overflowWrap = "break-word"
		self.dom.style.maxHeight = max_height
		
		self._index = 0
		
		def render_child() -> None:
			for _ in range(render_batch):
				child = children_builder(self._index)
				
				if child is None:
					return
				
				self.rendered_children.append(child)
				self._index += 1
			
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
