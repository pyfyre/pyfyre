from typing import List, Optional


class Style:
	@classmethod
	def from_styles(cls, styles: List["Style"]) -> "Style":
		props = {}
		
		for style in styles:
			for prop, value in style.props.items():
				props[prop] = value
		
		return Style(**props)
	
	def __init__(self, **props: str) -> None:
		self.props = props
	
	def __getitem__(self, prop: str) -> Optional[str]:
		return self.props.get(prop)
	
	def __setitem__(self, prop: str, value: str) -> None:
		self.props[prop] = value
	
	def __delitem__(self, prop: str) -> None:
		del self.props[prop]
	
	def css(self) -> str:
		return "; ".join([
			f"{prop.replace('_', '-')}: {value}"
			for prop, value in self.props.items()
		])
