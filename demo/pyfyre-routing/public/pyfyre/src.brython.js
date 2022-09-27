__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1664259589329, "settings": [".py", "_A='/favicon.ico'\nROUTES={'/':{'title':'A PyFyre App | Home','icon':_A},'/about':{'title':'A PyFyre App | About','icon':_A}}\nDEPENDENCIES=[]\n", []], "index": [".py", "_D='/about'\n_C='height: 100vh; width: 100vw; display: flex; flex-direction: column; justify-content: center;'\n_B='margin-left: auto; margin-right: auto; font-size: 50px;'\n_A='style'\nfrom pyfyre import render\nfrom pyfyre.nodes import *\nclass HomePage(Element):\n def __init__(self):super().__init__('div',attrs={_A:_C},children=[Element('p',attrs={_A:_B},children=[TextNode('Welcome to Home page!')]),Anchor(_D,attrs={_A:_B},children=[TextNode('Go to About')])])\nclass AboutPage(Element):\n def __init__(self):super().__init__('div',attrs={_A:_C},children=[Element('p',attrs={_A:_B},children=[TextNode('Welcome to About page!')]),Anchor('/',attrs={_A:_B},children=[TextNode('Go to Home')])])\nrender('body',{'/':lambda :HomePage(),_D:lambda :AboutPage()})\n", ["pyfyre", "pyfyre.nodes"]], "pyfyre": [".py", "from browser import document,window\nfrom pyfyre.router import RouteManager\nfrom pyfyre.exceptions import NodeNotFound\n__all__=['render']\ndef render(root_selector,routes):\n A=root_selector ;B=document.select(A)\n if B:RouteManager.set_routes(routes);RouteManager.root_node=B[0];RouteManager.render_route(window.location.pathname)\n else :raise NodeNotFound(A)\n", ["browser", "pyfyre.exceptions", "pyfyre.router"], 1], "pyfyre.events": [".py", "from enum import Enum\nclass BaseEventType(Enum):0\nclass EventType(BaseEventType):Cancel='cancel';Error='error';Scroll='scroll';Select='select';Wheel='wheel'\nclass MouseEventType(BaseEventType):AuxClick='auxclick';Click='click';ContextMenu='contextmenu';DbClick='dblclick';MouseDown='mousedown';MouseEnter='mouseenter';MouseLeave='mouseleave';MouseMove='mousemove';MouseOut='mouseout';MouseOver='mouseover';MouseUp='mouseup'\n", ["enum"]], "pyfyre.exceptions": [".py", "class PyFyreException(Exception):0\nclass NodeNotFound(PyFyreException):0\n", []], "pyfyre.router": [".py", "_A='404: Page Not Found :('\nfrom settings import ROUTES\nfrom browser import document\nfrom pyfyre.nodes import Element,TextNode\nclass RouteManager:\n _routes_builder={};_routes={};root_node=document.select('body')\n @staticmethod\n def set_routes(routes):RouteManager._routes_builder=routes\n @staticmethod\n def parse_route(route):\n  A=route ;B=document.createElement('a');B.href=A ;A=str(B.pathname)\n  if A =='/':return A\n  return str(B.pathname).rstrip('/')\n @staticmethod\n def get_node(route):\n  A=route ;A=RouteManager.parse_route(A);B=RouteManager._routes.get(A)\n  if B is None :C=RouteManager._routes_builder.get(A);B=C()if C else None ;RouteManager._routes[A]=B\n  return B or Element('p',children=[TextNode(_A)])\n @staticmethod\n def render_route(route):A=RouteManager.get_node(route);RouteManager.root_node.innerHTML='';RouteManager.root_node.appendChild(A.dom)\n @staticmethod\n def change_route(route):B='title';A=route ;A=RouteManager.parse_route(A);C=ROUTES.get(A)or {B:_A};document.title=C.get(B);RouteManager.render_route(A)\n", ["browser", "pyfyre.nodes", "settings"]], "pyfyre.nodes.buttons": [".py", "from pyfyre.events import MouseEventType\nfrom pyfyre.nodes.base import Element\nclass Button(Element):\n def __init__(A,onclick,*,attrs=None ,children=None ):super().__init__('button',attrs=attrs,children=children);A.add_event_listener(MouseEventType.Click,onclick)\n", ["pyfyre.events", "pyfyre.nodes.base"]], "pyfyre.nodes.links": [".py", "_A=None\nfrom pyfyre.events import MouseEventType\nfrom pyfyre.nodes.base import Element\nfrom browser import document,window\nclass Anchor(Element):\n def __init__(A,href,*,attrs=_A,children=_A):\n  C=href ;B=attrs ;A.href=C ;B=B or {};B['href']=C ;super().__init__('a',attrs=B,children=children)\n  if A.is_internal():\n   def D(event):from pyfyre.router import RouteManager as B ;window.history.pushState(_A,_A,A.absolute_href);event.preventDefault();B.change_route(C)\n   A.add_event_listener(MouseEventType.Click,D)\n @property\n def absolute_href(self):A=document.createElement('a');A.href=self.href ;return A.href\n def is_internal(B):A=document.createElement('a');A.href=B.href ;return bool(A.host ==window.location.host)\n", ["browser", "pyfyre.events", "pyfyre.nodes.base", "pyfyre.router"]], "pyfyre.nodes.lists": [".py", "from browser import aio\nfrom pyfyre.events import EventType\nfrom pyfyre.nodes import Element\nclass ListBuilder(Element):\n def __init__(A,children_builder,*,max_height='300px',render_batch=10,render_interval=0.1,attrs=None ):\n  A.rendered_children=[];super().__init__('div',attrs=attrs,children=lambda :A.rendered_children);A.dom.style.overflowY='scroll';A.dom.style.overflowWrap='break-word';A.dom.style.maxHeight=max_height ;A._index=0\n  def B():\n   for C in range(render_batch):\n    B=children_builder(A._index)\n    if B is None :return\n    A.rendered_children.append(B);A._index +=1\n   A.update_dom()\n  async def C():\n   if A.dom.scrollHeight ==A.dom.clientHeight:B();await aio.sleep(render_interval);await C()\n  def D(event):\n   A=event.target\n   if A.scrollHeight -A.scrollTop -A.clientHeight <1:B()\n  aio.run(C());A.add_event_listener(EventType.Scroll,D)\n", ["browser", "pyfyre.events", "pyfyre.nodes"]], "pyfyre.nodes.base": [".py", "_A=None\nimport sys\nfrom browser import document\nfrom abc import ABC,abstractmethod\nclass Node(ABC):\n def __init__(A):A.dom=A.create_dom()\n @abstractmethod\n def create_dom(self):raise NotImplementedError\n @abstractmethod\n def update_dom(self):raise NotImplementedError\nclass Element(Node):\n def __init__(A,tag_name,*,attrs=_A,children=_A):B=children ;A.tag_name=tag_name ;A.attrs=attrs or {};A._children_builder=B if callable(B)else _A ;A.children=(A._secure_build()if callable(B)else B)or [];super().__init__()\n def _secure_build(A):\n  if A._children_builder is _A:return A.children\n  try :return A._children_builder()\n  except BaseException:return A.on_build_error(*sys.exc_info())\n def on_build_error(B,exc_type,exc_value,exc_traceback):A='p';return [Element(A,children=[TextNode(exc_type)]),Element(A,children=[TextNode(exc_value)]),Element(A,children=[TextNode(exc_traceback)])]\n def create_dom(A):\n  B=document.createElement(A.tag_name)\n  for (C,D)in A.attrs.items():B.setAttribute(C,D)\n  B.replaceChildren(*([B.dom for B in A.children]));return B\n def update_dom(A):\n  for (B,C)in A.attrs.items():A.dom.setAttribute(B,C)\n  A.children=A._secure_build();A.dom.replaceChildren(*([B.dom for B in A.children]))\n def add_event_listener(A,event_type,callback):A.dom.bind(event_type.value,callback)\nclass TextNode(Node):\n def __init__(A,value):A._value=str(value);super().__init__()\n @property\n def value(self):return self._value\n def set_value(A,value):A._value=str(value)\n def create_dom(A):return document.createTextNode(A.value)\n def update_dom(A):A.dom.nodeValue=A.value\n", ["abc", "browser", "sys"]], "pyfyre.nodes": [".py", "from .base import Node,Element,TextNode\nfrom .buttons import Button\nfrom .links import Anchor\nfrom .lists import ListBuilder\n__all__=['Node','Element','TextNode','Button','Anchor','ListBuilder']\n", ["pyfyre.nodes.base", "pyfyre.nodes.buttons", "pyfyre.nodes.links", "pyfyre.nodes.lists"], 1]}
__BRYTHON__.update_VFS(scripts)
