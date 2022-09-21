from typing import Dict, Any, List
from browser import document, DOMNode
from pyfyre.exceptions import NodeNotFound
from pyfyre.widgets import BaseWidget, WidgetType, TextWidget

__all__ = [
	"render"
]


class _VirtualDOM:
	dom: Dict[str, Any] = TextWidget("Welcome to PyFyre ✨").dom()
	
	@staticmethod
	def create_element(dom: Dict[str, Any]) -> DOMNode:
		el = document.createElement(dom["tag_name"])
		
		for attr_name, attr_value in dom["props"].items():
			el.setAttribute(attr_name, attr_value)
		
		return el
	
	@staticmethod
	def append_children(parent: DOMNode, children: List[Dict[str, Any]]) -> None:
		for child in children:
			if child["_type"] == WidgetType.TextNode:
				parent.textContent += child["content"]
			elif child["_type"] == WidgetType.Element:
				el = _VirtualDOM.create_element(child)
				_VirtualDOM.append_children(el, child["children"])
				parent.appendChild(el)
	
	@staticmethod
	def render(root_selector: str) -> None:
		nodes = document.select(root_selector)
		
		if nodes:
			root = nodes[0]
		else:
			raise NodeNotFound(root_selector)
		
		dom: Dict[str, Any] = _VirtualDOM.dom
		
		if dom["_type"] == WidgetType.TextNode:
			root.textContent += dom["content"]
		elif dom["_type"] == WidgetType.Element:
			el = _VirtualDOM.create_element(dom)
			_VirtualDOM.append_children(el, dom["children"])
			root.appendChild(el)


def render(root_selector: str, widget: BaseWidget) -> None:
	_VirtualDOM.dom = widget.dom()
	_VirtualDOM.render(root_selector)
