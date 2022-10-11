from pyfyre.events import EventType
from pyfyre.nodes import Element


class ListBuilder(Element):
	def __init__(
		self, children_builder, *,
		max_height: str = "300px",
		render_batch: int = 10,
		render_interval: float = 0,
		attrs = None
	) -> None:
		self.children_builder = children_builder
		self.render_batch = render_batch
		self.render_interval = render_interval
		
		self.index = 0
		self.rendered_children = []
		
		super().__init__("div", lambda: self.rendered_children, attrs=attrs)
		self.dom.style.overflowY = "scroll"
		self.dom.style.overflowWrap = "break-word"
		self.dom.style.maxHeight = max_height
		
		def render_nodes(event) -> None:
			el = event.target
			if el.scrollHeight - el.scrollTop - el.clientHeight < 1:
				self.render_next_children()
		
		self.add_event_listener(EventType.Scroll, render_nodes)
	
	def render_next_children(self) -> None:
		for _ in range(self.render_batch):
			child = self.children_builder(self.index)
			
			if child is None:
				break
			
			self.rendered_children.append(child)
			self.index += 1
		
		self.update_dom()
	
	def build_children(self) -> None:
		if self.dom.scrollHeight == self.dom.clientHeight:
			self.render_next_children()
			self.build_children()
