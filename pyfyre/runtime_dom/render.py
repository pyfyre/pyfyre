from browser import document

class Render:

    @staticmethod
    def checkEvents(vNode, _el):
        if "onclick" in vNode:
            _el.bind("click", vNode["onclick"])

        if "oninput" in vNode:
            _el.bind("input", vNode["oninput"])

    @staticmethod
    def renderElem(vNode):
        _el = document.createElement(vNode["tagName"])

        for k, v in vNode["attrs"].items():
            _el.setAttribute(k, v)

        for child in vNode["children"]:
            _child = Render.render(child)
            _el.appendChild(_child)

        Render.checkEvents(vNode, _el)

        return _el

    @staticmethod
    def render(vNode):
        if isinstance(vNode, str):
            return document.createTextNode(vNode)

        return Render.renderElem(vNode)
