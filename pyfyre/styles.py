from typing import List, Optional, Callable


class Style:
	@classmethod
	def from_styles(
		cls, styles: List["Style"], *, dynamic: bool = True
	) -> "Style":
		"""
			If [dynamic] is `True`, if one of the [styles] is updated,
			this [Style] will also update.
		"""
		
		s = Style()
		props = {}
		
		def update_style() -> None:
			s.props = Style.from_styles(styles, dynamic=False).props.copy()
			s.call_listeners()
		
		for style in styles:
			for prop, value in style.props.items():
				props[prop] = value
			
			if dynamic:
				style.add_listener(update_style)
		
		s.props = props
		return s
	
	def __init__(self, **props: str) -> None:
		self.props = props
		self._listeners: List[Callable[[], None]] = []
	
	def __getitem__(self, prop: str) -> Optional[str]:
		return self.props.get(prop)
	
	def __setitem__(self, prop: str, value: str) -> None:
		self.props[prop] = value
		self.call_listeners()
	
	def __delitem__(self, prop: str) -> None:
		del self.props[prop]
		self.call_listeners()
	
	def call_listeners(self) -> None:
		for listener in self._listeners:
			listener()
	
	def css(self) -> str:
		return "; ".join([
			f"{prop.replace('_', '-')}: {value}"
			for prop, value in self.props.items()
		])
	
	def add_listener(self, listener: Callable[[], None]) -> None:
		self._listeners.append(listener)
	
	def remove_listener(self, listener: Callable[[], None]) -> int:
		remaining_listeners = []
		removed = 0
		
		for c in self._listeners:
			if c == listener:
				removed += 1
			else:
				remaining_listeners.append(c)
		
		self._listeners = remaining_listeners
		return removed
