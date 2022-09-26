
from pyfyre.core.runtime_dom.render import Render
import javascript


class Diffing:

    @staticmethod
    def zip(xs, ys):
        zipped = []

        for i in range(javascript.Math.min(len(xs), ys.length)):
            zipped.append([xs[i], ys[i]])

        return zipped

    @staticmethod
    def diffChildren(oldVChildren, newVChildren):
        childPatches = []
        additionalPatches = []

        def wrapper(_parent):
            for z in Diffing.zip(childPatches, _parent.childNodes):
                z[0](z[1])

            for patch in additionalPatches:
                patch(_parent)

            return _parent

        if (isinstance(oldVChildren, str) or isinstance(newVChildren, str)):
            childPatches.append(Diffing.diff(oldVChildren, newVChildren))

            return wrapper

        for i in range(len(oldVChildren)):
            childPatches.append(Diffing.diff(oldVChildren[i], newVChildren[i]))

        for additionalVChild in newVChildren[len(oldVChildren):]:

            def wrapper(_node):
                _node.appendChild(Render.render(additionalVChild))
                return _node

            additionalPatches.append(wrapper)

        return wrapper


    @staticmethod
    def diffprops(oldprops, newprops):
        patches = []

        for k, v in newprops.items():
            
            def wrapper(_node):
                _node.setAttribute(k, v)
                return _node

            patches.append(wrapper)

        for k in oldprops:
            if not k in newprops:
                def wrapper(_node):
                    _node.removeAttribute(k)
                    return _node

                return wrapper

        def wrapper(_node):
            for patch in patches:
                patch(_node)

        return wrapper
    
    @staticmethod
    def diff(vOldNode, vNewNode):
        if (vNewNode == None):
            def wrapper(_node):
                _node.remove()
                return None

            return wrapper

        if (isinstance(vOldNode, str) or isinstance(vNewNode, str)):
            if vOldNode != vNewNode:
                def wrapper(_node):
                    _newNode = Render.render(vNewNode)
                    _node.replaceWith(_newNode)
                    return _newNode

                return wrapper
            else:
                def wrapper(_node): return _node

                return wrapper
            
        if vOldNode["tagName"] != vNewNode["tagName"]:
            def wrapper(_node):
                _newNode = Render.render(vNewNode)
                _node.replaceWith(_newNode)
                return _newNode

            return wrapper

        patchProps = Diffing.diffprops(vOldNode["props"], vNewNode["props"])
        patchChildren = Diffing.diffChildren(vOldNode["children"], vNewNode["children"])

        def wrapper(_node):
            patchProps(_node)
            patchChildren(_node)
            return _node

        return wrapper