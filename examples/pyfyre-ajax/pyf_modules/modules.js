__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1643992369453, "pyfyre.pyfyre": [".py", "from browser import document\nfrom pyfyre.globals import Globals\n\ndef runApp(app,mount=\"app-mount\"):\n body=document.getElementById(mount)\n body.innerHTML=\"\"\n body.appendChild(app.dom())\n \n Globals.__PARENT__=app\n", ["browser", "pyfyre.globals"]], "pyfyre": [".py", "", [], 1], "pyfyre.ajax": [".py", "from browser import ajax\n\nclass Ajax:\n def get(url,then):\n  req=ajax.ajax()\n  req.open('GET',url,True )\n  req.bind('complete',then)\n  req.set_header('content-type','application/x-www-form-urlencoded')\n  req.send()\n", ["browser"], 1], "pyfyre.globals.events": [".py", "from pyfyre.globals import Globals\n\nclass Events:\n ''\n\n\n\n \n \n @staticmethod\n def add(event):\n  Globals.__EVENTS__[event]=[]\n  \n @staticmethod\n def addListener(event,listener):\n  Globals.__EVENTS__[event].append(listener)\n  \n @staticmethod\n def broadcast(event):\n  for func in Globals.__EVENTS__[event]:\n   func()\n", ["pyfyre.globals"]], "pyfyre.globals": [".py", "\nclass Globals:\n __PARENT__=None\n __LOC__=None\n __EVENTS__={}\n \n PATH_INITIALIZED=False\n", [], 1], "pyfyre.router": [".py", "from pyfyre.globals import Globals\nfrom pyfyre.globals.events import Events\nfrom pyfyre.pyfyre import runApp\n\nfrom browser import document,window,bind\n\nclass Router:\n ''\n\n\n\n \n \n def __init__(self,routes):\n  self.routes=routes\n  \n  if not Globals.PATH_INITIALIZED:\n   Globals.__LOC__=window.location.pathname\n   Globals.PATH_INITIALIZED=True\n   \n  if not \"change_route\"in Globals.__EVENTS__:\n   Events.add(\"change_route\")\n   \n   self.listenRoute()\n   \n def dom(self):\n  return self.routes[Globals.__LOC__].dom()\n  \n def listenRoute(self):\n  def changeRoute():\n   runApp(Globals.__PARENT__)\n   \n  Events.addListener(\"change_route\",changeRoute)\n  \n @staticmethod\n def push(location):\n  Globals.__LOC__=location\n  \n  Events.broadcast(\"change_route\")\n  window.history.pushState(None ,None ,location)\n  \n  @bind(window,'popstate')\n  def popState(e):\n   Globals.__LOC__=window.location.pathname\n   Events.broadcast(\"change_route\")\n   e.preventDefault()\n", ["browser", "pyfyre.globals", "pyfyre.globals.events", "pyfyre.pyfyre"], 1], "pyfyre.widgets": [".py", "\nfrom pyfyre.pyfyre import runApp\nfrom pyfyre.globals import Globals\n\n\nfrom browser import document,window\nfrom pyfyre.router import Router\n\nclass UsesState:\n\n def __init__(self):\n  self.domElement=None\n  \n def build(self):\n  pass\n  \n def dom(self):\n  self.domElement=self.build().dom()\n  return self.domElement\n  \n def update(self):\n  ''\n\n\n  \n  \n  parentNode=self.domElement.parentNode\n  self.domElement.remove()\n  self.domElement=self.dom()\n  parentNode.appendChild(self.domElement)\n  \nclass Widget:\n\n def __init__(self,tagname:str,*,className,props:dict=None ):\n  self.tagname=tagname\n  self.className=className\n  self.element=None\n  self.props=props if props is not None else {}\n  \n def dom(self):\n  element=document.createElement(self.tagname)\n  element.className=self.className\n  \n  self.element=element\n  \n  for key,value in self.props.items():\n   element.attrs[key]=value\n   \n  return element\n  \n  \nclass Container(Widget):\n\n def __init__(self,children=[],className=\"\",props:dict=None ):\n  super().__init__(\"div\",className=className,props=props)\n  self.children=children\n  \n def dom(self):\n  element=super().dom()\n  \n  for child in self.children:\n   element.appendChild(child.dom())\n   \n  return element\n  \nclass Button(Widget):\n\n def __init__(self,textContent,onClick=lambda :print(\"\"),className=\"\",props:dict=None ):\n  super().__init__(\"button\",className=className,props=props)\n  self.textContent=textContent\n  self.onClick=onClick\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  \n  element.bind(\"click\",self.onClick)\n  \n  return element\n  \nclass Anchor(Widget):\n\n def __init__(self,textContent,link:str=\"#\",className=\"\",props:dict=None ):\n  super().__init__(\"a\",className=className,props=props)\n  self.textContent=textContent\n  self.link=link\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  element.href=self.link\n  \n  return element\n  \nclass Text(Widget):\n\n def __init__(self,textContent:str,className=\"\",props:dict=None ):\n  super().__init__(\"p\",className=className,props=props)\n  self.textContent=textContent\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  \n  return element\n  \n  \nclass Image(Widget):\n\n def __init__(self,src,className=\"\",props:dict=None ):\n  super().__init__(\"img\",className=className,props=props)\n  self.src=src\n  \n def dom(self):\n  element=super().dom()\n  element.src=self.src\n  \n  return element\n  \nclass Link(Widget):\n\n def __init__(self,textContent:str,to='/',className=\"\",props:dict=None ):\n  super().__init__(\"a\",className=className,props=props)\n  self.textContent=textContent\n  self.to=to\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  element.href=\"#\"\n  \n  element.bind(\"click\",self.navigate)\n  \n  return element\n  \n def navigate(self,e):\n  e.preventDefault()\n  Router.push(self.to)\n  \nclass ListBuilder(Widget):\n\n def __init__(self,count=1,builder=None ,className=\"\",props:dict=None ):\n  super().__init__(\"div\",className=className,props=props)\n  self.count=count\n  self.builder=builder\n  \n def dom(self):\n  element=super().dom()\n  \n  for i in range(self.count):\n   element.appendChild(self.builder(i).dom())\n   \n  return element\n", ["browser", "pyfyre.globals", "pyfyre.pyfyre", "pyfyre.router"], 1]}
__BRYTHON__.update_VFS(scripts)
