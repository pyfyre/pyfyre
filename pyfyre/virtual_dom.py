from typing import Dict, Any, List
from browser import document, DOMNode
from pyfyre.widgets import WidgetType, StatefulContainer


class VirtualDOM:
	root: DOMNode = document.select("body")
	
	@staticmethod
	def create_element(dom: Dict[str, Any]) -> DOMNode:
		el = document.createElement(dom["tag_name"])
		
		for attr_name, attr_value in dom["props"].items():
			el.setAttribute(attr_name, attr_value)
		
		for event_type, listeners in dom["event_listeners"].items():
			for callback in listeners:
				el.bind(event_type.value, callback)
		
		VirtualDOM.append_children(el, dom["children"])
		return el
	
	@staticmethod
	def append_children(parent: DOMNode, children: List[Dict[str, Any]]) -> None:
		for child in children:
			if child["_type"] == WidgetType.TextNode:
				parent.textContent += child["content"]
			elif child["_type"] == WidgetType.Element:
				el = VirtualDOM.create_element(child)
				parent.appendChild(el)
	
	@staticmethod
	def update(widget: StatefulContainer) -> None:
		el = document.select(f"[pyfyre-identifier='{widget.identifier}']")[0]
		el.replaceWith(VirtualDOM.create_element(widget.dom()))
	
	@staticmethod
	def render(dom: Dict[str, Any]) -> None:
		if dom["_type"] == WidgetType.TextNode:
			VirtualDOM.root.textContent = dom["content"]
		elif dom["_type"] == WidgetType.Element:
			el = VirtualDOM.create_element(dom)
			VirtualDOM.root.innerHTML = ""
			VirtualDOM.root.appendChild(el)
