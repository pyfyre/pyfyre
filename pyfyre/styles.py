from typing import Dict


class Style:
	def __init__(self, class_name: str, **styles: Dict[str, str]) -> None:
		self.class_name = class_name
		self._raw_styles = styles
	
	def css(self) -> str:
		css = f".{self.class_name}" + "{"
		
		for style_name, style_value in self._raw_styles.items():
			style_name = style_name.replace("_", "-")
			css += f"{style_name}: {style_value}; "
		
		return css + "}"
