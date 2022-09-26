__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1644540212122, "pyfyre.pyfyre": [".py", "from browser import document\nfrom pyfyre.globals import Globals\nfrom pyfyre import settings\n\ndef runApp(app,mount=\"app-mount\"):\n ''\n\n\n\n\n\n\n\n\n\n \n \n body=document.getElementById(mount)\n body.innerHTML=\"\"\n body.appendChild(app.dom())\n \n Globals.__PARENT__=app\n Globals.DEBUG=settings.DEBUG\n", ["browser", "pyfyre", "pyfyre.globals"]], "pyfyre": [".py", "", [], 1], "pyfyre.ajax": [".py", "from browser import ajax\n\nclass Ajax:\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n @staticmethod\n def get(url,mode=\"json\",then=None ):\n  ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n  \n  ajax.get(url,mode=mode,oncomplete=then)\n", ["browser"], 1], "pyfyre.core.exceptions": [".py", "from pyfyre.widgets.widget import Widget\n\nclass UIBaseException:\n def __init__(self,msg,e):\n  self.msg=msg\n  self.e=e\n  \n def dom(self):\n  print(f\"Uncaught exception: {self.e}\")\n  \n  return self.TextException(self.msg).dom()\n  \n class TextException(Widget):\n  def __init__(self,msg:str,className=\"\",props:dict=None ):\n   super().__init__(\"h1\",className=className,props=props)\n   self.msg=msg\n   \n  def dom(self):\n   element=super().dom()\n   element.textContent=self.msg\n   \n   element.attrs[\"style\"]=\"background-color: #efa3a3; width: fit-content; padding: 10px;\"\n   \n   return element\n   \nclass RenderError(UIBaseException):...\nclass InvalidController(BaseException):...\n", ["pyfyre.widgets.widget"]], "pyfyre.core": [".py", "", [], 1], "pyfyre.globals.events": [".py", "from pyfyre.globals import Globals\n\nclass Events:\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n @staticmethod\n def add(event):\n  ''\n\n\n\n\n\n  \n  Globals.__EVENTS__[event]=[]\n  \n @staticmethod\n def addListener(event,listener):\n  ''\n\n\n\n\n\n\n\n\n  \n  Globals.__EVENTS__[event].append(listener)\n  \n @staticmethod\n def broadcast(event):\n  ''\n\n\n\n\n\n  \n  for func in Globals.__EVENTS__[event]:\n   func()\n", ["pyfyre.globals"]], "pyfyre.globals": [".py", "\nclass Globals:\n\n DEBUG=False\n \n \n \n __PARENT__=None\n \n \n \n __LOC__=None\n \n \n DYNAMIC_ROUTES=[]\n \n \n PATH_INITIALIZED=False\n \n \n \n __EVENTS__={}\n \n \n \n __ASSETS__=\"\"\n", [], 1], "pyfyre.management.python_minifier": [".py", "''\nimport token\nimport tokenize\nimport re\nimport io\nfrom keyword import kwlist\n\nfor kw in [\"async\",\"await\"]:\n if kw not in kwlist:\n  kwlist.append(kw)\n  \nasync_types=[]\nif hasattr(tokenize,\"ASYNC\"):\n async_types.append(tokenize.ASYNC)\nif hasattr(tokenize,\"AWAIT\"):\n async_types.append(tokenize.AWAIT)\n \ndef minify(src,preserve_lines=False ):\n\n file_obj=io.BytesIO(src.encode('utf-8'))\n token_generator=tokenize.tokenize(file_obj.readline)\n \n out=''\n line=0\n last_item=None\n last_type=None\n indent=0\n brackets=[]\n \n \n encoding=next(token_generator).string\n \n file_obj=io.BytesIO(src.encode(encoding))\n token_generator=tokenize.tokenize(file_obj.readline)\n \n for item in token_generator:\n \n  if token.tok_name[item.type]=='OP':\n   if item.string in '([{':\n    brackets.append(item.string)\n   elif item.string in '}])':\n    brackets.pop()\n    \n  sline=item.start[0]\n  if sline ==0:\n   continue\n   \n   \n  if item.type ==tokenize.INDENT:\n   indent +=1\n  elif item.type ==tokenize.DEDENT:\n   indent -=1\n   continue\n   \n  if sline >line:\n  \n   while out.count(\"\\n\")<sline -1:\n    if last_item.line.rstrip().endswith(\"\\\\\"):\n     out +=\"\\\\\"\n    out +=\"\\n\"\n    \n   if not brackets and item.type ==tokenize.STRING:\n    if last_type in [tokenize.NEWLINE,tokenize.INDENT,None ]:\n    \n    \n    \n    \n     out +=' '*indent+\"''\"\n     if preserve_lines:\n      out +='\\n'*item.string.count('\\n')\n     continue\n   out +=' '*indent\n   if item.type not in [tokenize.INDENT,tokenize.COMMENT]:\n    out +=item.string\n   elif (item.type ==tokenize.COMMENT and\n   line <=2 and item.line.startswith('#!')):\n   \n   \n    out +=item.string\n  else :\n   if item.type ==tokenize.COMMENT:\n    continue\n   if (not brackets and item.type ==tokenize.STRING and\n   last_type in [tokenize.NEWLINE,tokenize.INDENT]):\n   \n   \n    out +=\"''\"\n    if preserve_lines:\n     out +='\\n'*item.string.count('\\n')\n    continue\n   previous_types=[tokenize.NAME,tokenize.NUMBER]+async_types\n   if item.type in [tokenize.NAME,tokenize.NUMBER,tokenize.OP]and\\\n   last_type in previous_types:\n   \n    if (item.type !=tokenize.OP\\\n    or item.string not in ',()[].=:{}+&'\\\n    or (last_type ==tokenize.NAME and\n    last_item.string in kwlist)):\n     out +=' '\n   elif (item.type ==tokenize.STRING and\n   last_type in [tokenize.NAME,tokenize.NUMBER]):\n   \n    out +=' '\n   elif (item.type ==tokenize.NAME and\n   item.string ==\"import\"and\n   last_item.type ==tokenize.OP and\n   last_item.string =='.'):\n   \n    out +=' '\n   elif (item.type in async_types and\n   last_item.type in previous_types):\n    out +=' '\n   out +=item.string\n   \n  line=item.end[0]\n  last_item=item\n  if item.type ==tokenize.NL and last_type ==tokenize.COMMENT:\n  \n   last_type=tokenize.NEWLINE\n  else :\n   last_type=item.type\n   \n   \n out=re.sub(r'^\\s+$','',out,re.M)\n \n if not preserve_lines:\n \n  out=re.sub(\"^''\\n\",'',out)\n  \n  \n  out=re.sub('\\n( *\\n)+','\\n',out)\n  \n  \n  \n  def repl(mo):\n   if mo.groups()[0]==mo.groups()[1]:\n    return '\\n'+mo.groups()[1]\n   return mo.string[mo.start():mo.end()]\n  out=re.sub(\"\\n( *)''\\n( *)\",repl,out)\n  \n return out\n", ["io", "keyword", "re", "token", "tokenize"]], "pyfyre.management": [".py", "#!/usr/bin/env python3\n\nimport os,sys,random,string,time\nfrom shutil import copytree,rmtree\nfrom distutils.dir_util import copy_tree\n\nfrom .python_minifier import minify\n\ndef execute_from_command_line(argv=None ):\n utility=ManagementUtility()\n \n \"\"\"Entry Point\"\"\"\n try :\n  if sys.argv[1]==\"create-app\":\n   try :\n    name=sys.argv[2]\n   except IndexError:\n    name=\"MyApp\"\n    \n   try :\n    description=sys.argv[3]\n   except IndexError:\n    description=\"PyFyre web application.\"\n    \n   utility.create_app(name,description)\n  elif sys.argv[1]==\"runapp\":\n   try :\n    port=sys.argv[2]\n   except IndexError:\n    port=None\n    \n   try :\n    directory=sys.argv[3]\n   except IndexError:\n    directory=None\n    \n   utility.run_app(directory,port)\n  elif sys.argv[1]==\"build\":\n   try :\n    directory=sys.argv[2]\n   except IndexError:\n    directory=None\n    \n   utility.build_app(directory)\n  elif sys.argv[1]==\"help\":\n   utility.pyfyre_help()\n  else :\n   utility.pyfyre_help()\n except IndexError as e:\n  utility.pyfyre_help()\n  \nclass ManagementUtility:\n def pyfyre_help(self):\n  PYFYRE_HELP=\"\"\"Manage your PyFyre projects.\n\n        Common Commands:\n\n            pyfyre.py create-app [name] [description]\n                Create a new PyFyre project in your current directory.\n\n            pyfyre.py runserver [port=8080]\n                Run a live server in your current directory.\n\n            pyfyre.py help\n                Show this message.\n        \"\"\"\n  print(PYFYRE_HELP)\n  \n def create_app(self,app_name:str,app_description:str):\n  ''\n  \n  print(\"Creating your PyFyre project...\")\n  \n  path=os.path.join(os.getcwd(),app_name)\n  \n  try :\n   os.makedirs(path)\n  except FileExistsError:\n   prompt=input(f\"Project already exists. Want to overwrite the project '{app_name}'? (y or n): \")\n   \n   if prompt ==\"y\":\n    rmtree(path)\n    os.makedirs(path)\n   else :\n    print(\"Aborting...\")\n    return\n    \n    \n  core_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),\"..\"))\n  copy_tree(core_dir,os.path.join(path,\"pyfyre\"))\n  \n  \n  user_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),\"..\",\"user\"))\n  copy_tree(user_dir,path)\n  \n  \n  with open(os.path.join(user_dir,\"index.html\"))as file:\n   content=file.read().format(app_name=app_name,app_description=app_description,main_key=\"{main_key}\")\n  with open(os.path.join(user_dir,\"index.html\"),\"w\")as file:\n   file.write(content)\n   \n   \n  with open(os.path.join(user_dir,\"README.md\"))as file:\n   content=file.read().format(app_name=app_name,app_description=app_description)\n  with open(os.path.join(path,\"README.md\"),\"w\")as file:\n   file.write(content)\n   \n   \n  with open(os.path.join(user_dir,\"settings.py\"))as file:\n   content=file.read().format(app_name=app_name,app_description=app_description)\n  with open(os.path.join(path,\"settings.py\"),\"w\")as file:\n   file.write(content)\n   \n   \n  with open(os.path.join(path,\".gitignore\"),\"w\")as file:\n   file.write(__GITIGNORE__)\n   \n  os.chdir(os.path.join(path,\"pyfyre\"))\n  \n  os.system(\"brython-cli --install\")\n  \n  \n  os.remove(\"demo.html\")\n  os.remove(\"unicode.txt\")\n  os.remove(\"README.txt\")\n  os.remove(\"brython.js\")\n  os.remove(\"index.html\")\n  \n  rmtree(os.path.join(path,\"pyfyre\",\"management\"))\n  rmtree(os.path.join(path,\"pyfyre\",\"user\"))\n  \n  self.minify_dir(os.path.join(path,\"pyfyre\"))\n  \n  os.system(\"brython-cli --make_package pyfyre\")\n  os.remove(\"pyfyre.py\")\n  os.system(\"brython-cli --modules\")\n  \n  os.chdir(os.path.join(\"..\"))\n  os.mkdir(\"pyf_modules\")\n  \n  with open(os.path.join(path,\"pyfyre\",\"brython_modules.js\"))as file:\n   content=file.read()\n  with open(os.path.join(\"pyf_modules\",\"builtins.js\"),\"w\")as file:\n   file.write(content)\n  with open(os.path.join(path,\"pyfyre\",\"pyfyre.brython.js\"))as file:\n   content=file.read()\n  with open(os.path.join(\"pyf_modules\",\"modules.js\"),\"w\")as file:\n   file.write(content)\n   \n  rmtree(\"pyfyre\")\n  os.system(\"cls\"if os.name ==\"nt\"else \"clear\")\n  \n  print(\"Project created successfully.\")\n  \n def produce(self,directory_path,build_path,reload=False ):\n \n \n \n  if not reload:\n   copytree(directory_path,build_path)\n   \n   for _,__,filenames in os.walk(os.path.join(build_path,\"pyf_modules\")):\n    for filename in filenames:\n    \n     _,ext=os.path.splitext(filename)\n     \n     if ext ==\".js\":\n      with open(os.path.join(directory_path,\"pyf_modules\",filename))as file:\n       content=file.read()\n      with open(os.path.join(build_path,filename),\"w\")as file:\n       file.write(content)\n       \n       \n   css_path=os.path.join(directory_path,\"src\",\"css\")\n   src_css_path=os.path.join(build_path,\"css\")\n   \n   copytree(css_path,src_css_path)\n   \n  with open(os.path.join(build_path,\"index.html\"))as file:\n   index_content=file.read()\n   \n   \n  os.chdir(os.path.join(directory_path,\"src\"))\n  os.system(\"brython-cli --make_package src\")\n  \n  \n  with open(os.path.join(\"src.brython.js\"))as file:\n   content=file.read()\n  with open(os.path.join(build_path,\"src.brython.js\"),\"w\")as file:\n   file.write(content)\n  with open(os.path.join(build_path,\"index.html\"),\"w\")as file:\n   file.write(index_content)\n  with open(os.path.join(directory_path,\"src\",\"__init__.py\"))as file:\n   content=file.read()\n  with open(os.path.join(build_path,\"__init__.py\"),\"w\")as file:\n   file.flush()\n   file.write(content)\n   \n  os.remove(\"src.brython.js\")\n  \n  os.chdir(build_path)\n  \n  \n  if reload:\n  \n   _ignores=set([\"__serve__\",\"__dev__\"])\n   \n   \n   for _,dirs,filenames in os.walk(build_path):\n    [dirs.remove(tmp)for tmp in list(dirs)if tmp in _ignores]\n    \n    for filename in filenames:\n     name,ext=os.path.splitext(filename)\n     \n     if ext ==\".js\":\n      if \"main\"in name:\n       with open(os.path.join(build_path,\"src.brython.js\"))as file:\n        content=file.read()\n       with open(filename,\"w\")as file:\n        file.write(content)\n        \n        \n   css_path=os.path.join(directory_path,\"src\",\"css\")\n   src_css_path=os.path.join(build_path,\"css\")\n   \n   rmtree(src_css_path)\n   \n   src_css_path=os.path.join(build_path,\"css\")\n   \n   copytree(css_path,src_css_path)\n   \n   \n  if not reload:\n   try :rmtree(\"__serve__\")\n   except Exception:...\n   \n   try :rmtree(\"__pycache__\")\n   except Exception:...\n   \n   try :os.remove(\"requirements.txt\")\n   except Exception:...\n   \n   try :os.remove(\"runtime.txt\")\n   except Exception:...\n   \n   try :os.remove(\".gitignore\")\n   except Exception:...\n   \n   rmtree(\"pyf_modules\")\n   os.remove(\"README.md\")\n   \n   rmtree(\"src\")\n   \n def run_app(self,directory,port):\n  print(\"Running your app in a development server...\")\n  \n  try :\n   from livereload import Server\n  except ImportError:\n   raise ImportError(\"Cannot find the liveserver module. Is it installed?\")\n   \n  server=Server()\n  \n  _directory=os.path.abspath(directory)if directory else os.getcwd()\n  \n  if os.path.exists(os.path.join(_directory,\"__serve__\")):\n   rmtree(os.path.join(_directory,\"__serve__\"))\n   \n  _build=os.path.join(_directory,\"__serve__\")\n  \n  def reload():\n   print(\"Detected file changes, performing hot reload...\")\n   self.produce(_directory,_build,reload=True )\n   self.produceJsBundle(_build,_directory,reload=True )\n   print(\"Hot reload successful!\")\n   \n  self.produce(_directory,_build)\n  self.produceJsBundle(_build)\n  \n  os.system(\"cls\"if os.name ==\"nt\"else \"clear\")\n  \n  print(\"Happy Hacking!\")\n  \n  server.watch(f\"{_directory}/src/\",reload)\n  server.serve(port=port if port else 8000,host=\"localhost\",root=os.path.join(_directory,\"__serve__\"))\n  \n def build_app(self,directory):\n  print(\"Producing optimized build for your project...\")\n  \n  directory_path=os.path.abspath(directory)if directory else os.getcwd()\n  \n  if os.path.exists(os.path.join(directory_path,\"build\")):\n   rmtree(os.path.join(directory_path,\"build\"))\n   \n  build_path=os.path.join(directory_path,\"build\")\n  \n  self.produce(directory_path,build_path)\n  self.produceJsBundle(build_path)\n  \n  print(\"Build succeeded!\")\n  \n def produceJsBundle(self,build_path,directory_path=None ,reload=False ):\n \n  try :\n   import js2py\n  except ImportError:\n   raise ImportError(\"Cannot find js2py. Is it installed?\")\n   \n  os.chdir(build_path)\n  \n  vfs={}\n  \n  ctx_main=js2py.EvalJs()\n  ctx_std=js2py.EvalJs()\n  ctx_pyf=js2py.EvalJs()\n  \n  with open(os.path.join(build_path,\"src.brython.js\"))as file:\n   content=file.readlines()\n   content.pop(0)\n   content.pop(1)\n   main_js=''.join(content)\n  with open(os.path.join(build_path,\"builtins.js\")if not reload else os.path.join(directory_path,\"pyf_modules\",\"builtins.js\"))as file:\n   content=file.readlines()\n   content.pop(0)\n   content.pop(0)\n   content.pop(1)\n   std_js=''.join(content)\n  with open(os.path.join(build_path,\"modules.js\")if not reload else os.path.join(directory_path,\"pyf_modules\",\"modules.js\"))as file:\n   content=file.readlines()\n   content.pop(0)\n   content.pop(1)\n   pyf_js=''.join(content)\n  with open(os.path.join(build_path,\"settings.py\"))as file:\n   settings=file.read()\n   \n  ctx_main.execute(main_js)\n  ctx_std.execute(std_js)\n  ctx_pyf.execute(pyf_js)\n  \n  main_scripts=ctx_main.scripts.to_dict()\n  std_scripts=ctx_std.scripts.to_dict()\n  pyf_scripts=ctx_pyf.scripts.to_dict()\n  \n  def appendVfs(sc,py_script=False ,name=None ,requires=None ):\n   if py_script:\n    vfs[f\"{name}\"]=[\".py\",sc,requires]\n    return\n    \n   for k,v in list(sc.items()):\n    if k ==\"$timestamp\":\n     sc.pop(k)\n     \n    vfs[k]=v\n    \n  appendVfs(main_scripts)\n  appendVfs(std_scripts)\n  appendVfs(pyf_scripts)\n  appendVfs(settings,py_script=True ,name=\"pyfyre.settings\",requires=[\"pyfyre.globals\"])\n  \n  main_key=''.join(random.choice(string.ascii_lowercase)for i in range(15))\n  \n  if reload:\n   for _,_,files in os.walk(build_path):\n    for file in files:\n     name,ext=os.path.splitext(file)\n     \n     if ext ==\".js\":\n      if \"main\"in name:\n       name=name.split('.')\n       main_key=name[-1]\n       \n  with open(os.path.join(build_path,f\"main.{main_key}.js\"),\"w\")as file:\n   vfs[\"$timestamp\"]=int(1000 *time.time())\n   \n   brython=[\n   \"__BRYTHON__.use_VFS = true;\\n\",\n   f\"var scripts = {str(vfs)}\",\n   \"\\n__BRYTHON__.update_VFS(scripts)\"\n   ]\n   \n   file.writelines(brython)\n   \n  with open(os.path.join(build_path,\"index.html\"))as file:\n   content=file.read().format(main_key=main_key)\n  with open(os.path.join(build_path,\"index.html\"),\"w\")as file:\n   file.write(content)\n   \n  with open(os.path.join(build_path,\"__init__.py\"))as file:\n   minified=minify(file.read())\n  with open(os.path.join(build_path,\"__init__.py\"),\"w\")as file:\n   file.write(minified)\n   \n  os.remove(f\"src.brython.js\")\n  \n  if not reload:\n   os.remove(f\"modules.js\")\n   os.remove(f\"builtins.js\")\n   \n def minify_dir(self,path):\n  for dirpath,_,filenames in os.walk(path):\n   for filename in filenames:\n    _,ext=os.path.splitext(filename)\n    \n    if ext ==\".py\":\n     with open(os.path.join(dirpath,filename))as file:\n      minified=minify(file.read())\n     with open(os.path.join(dirpath,filename),\"w\")as file:\n      file.write(minified)\n      \n__GITIGNORE__=\"\"\"# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# PyFyre\nbuild/\n__serve__/\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\"\"\"\n\nif __name__ ==\"__main__\":\n execute_from_command_line()\n", ["distutils.dir_util", "js2py", "livereload", "os", "pyfyre.management.python_minifier", "random", "shutil", "string", "sys", "time"], 1], "pyfyre.router": [".py", "from pyfyre.globals import Globals\nfrom pyfyre.globals.events import Events\nfrom pyfyre.pyfyre import runApp\n\nfrom browser import window,bind\n\nclass Router:\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self,routes):\n  self.routes:dict=routes\n  \n  if not Globals.PATH_INITIALIZED:\n   Globals.__LOC__=window.location.pathname\n   Globals.PATH_INITIALIZED=True\n   \n  if not \"change_route\"in Globals.__EVENTS__:\n   Events.add(\"change_route\")\n   \n   self.listenRoute()\n   \n  for routeName,view in self.routes.items():\n   pathname=routeName.split('/')\n   \n   try :\n    query=pathname[-1]\n    pathurl=pathname[-2]\n    \n    if query[0]==\":\":\n     queryName=query.replace(\":\",\"\")\n     Globals.DYNAMIC_ROUTES.append([pathurl,queryName,view])\n   except IndexError:...\n   \n def dom(self):\n \n  try :\n   dom=self.routes[Globals.__LOC__].dom()\n  except KeyError:\n   try :\n    _,pathurl=self.get_params()\n    \n    for route in Globals.DYNAMIC_ROUTES:\n     if route[0]==pathurl:\n      dom=route[2].dom()\n   except Exception as e:\n   \n   \n   \n    raise Exception(\"Path 404: Cannot find the path.\")\n    \n  return dom\n  \n def listenRoute(self):\n  def changeRoute():\n   runApp(Globals.__PARENT__)\n   \n  Events.addListener(\"change_route\",changeRoute)\n  \n @staticmethod\n def query():\n  query,pathurl=Router.get_params(Router)\n  \n  queryNames={}\n  \n  for route in Globals.DYNAMIC_ROUTES:\n   if route[0]==pathurl:\n    queryNames[route[1]]=query\n    \n  return queryNames\n  \n @staticmethod\n def push(location):\n  Globals.__LOC__=location\n  \n  Events.broadcast(\"change_route\")\n  window.history.pushState(None ,None ,location)\n  \n  @bind(window,'popstate')\n  def popState(e):\n   Globals.__LOC__=window.location.pathname\n   Events.broadcast(\"change_route\")\n   e.preventDefault()\n   \n def get_params(self):\n  path=f\"{Globals.__LOC__}\"\n  pathname=path.split('/')\n  \n  query=pathname[-1]\n  pathurl=pathname[-2]\n  \n  return query,pathurl\n", ["browser", "pyfyre.globals", "pyfyre.globals.events", "pyfyre.pyfyre"], 1], "pyfyre.user.settings": [".py", "from pyfyre.globals import Globals\n\nAPP_NAME=\"{app_name}\"\nDESCRIPTION=\"{app_description}\"\n\n\nDEBUG=True\n", ["pyfyre.globals"]], "pyfyre.user": [".py", "", [], 1], "pyfyre.user.src.main": [".py", "from src.components.counterapp import CounterApp\nfrom pyfyre.widgets import *\nfrom src.components.experiment import Experiment\n\n\n\nclass MyWebpage(UsesState):\n def __init__(self,greet):\n  self.greet=greet\n  \n def build(self):\n  return Container(\n  className=\"container\",\n  children=[\n  Text(\n  f\"{self.greet} to PyFyre!\",\n  className=\"title\"\n  ),\n  Experiment(),\n  CounterApp()\n  ]\n  )\n", ["pyfyre.widgets", "src.components.counterapp", "src.components.experiment"]], "pyfyre.user.src": [".py", "from pyfyre.widgets import *\nfrom pyfyre.pyfyre import runApp\nfrom src.main import MyWebpage\n\n\n\n\n\nclass App(UsesState):\n def __init__(self):\n \n \n  self.greet=\"Welcome\"\n  \n def build(self):\n \n \n \n \n  return MyWebpage(self.greet)\n  \n  \n  \n  \n  \n  \n  \n  \nrunApp(\nApp(),\nmount=\"app-mount\"\n)\n", ["pyfyre.pyfyre", "pyfyre.widgets", "src.main"], 1], "pyfyre.user.src.components.counterapp": [".py", "from pyfyre.widgets import *\n\nclass CounterApp(UsesState):\n def __init__(self):\n  self.count=0\n  \n def increment(self,e):\n  self.count=self.count+1\n  self.update()\n  \n def decrement(self,e):\n  self.count=self.count -1\n  self.update()\n  \n def build(self):\n  return Container(\n  className=\"counter-app\",\n  children=[\n  Text(\"Counter app example:\"),\n  Container(\n  className=\"counters\",\n  children=[\n  Button(\n  \"-\",\n  onClick=self.decrement,\n  className=\"btn-counter\"\n  ),\n  Text(self.count),\n  Button(\n  \"+\",\n  onClick=self.increment,\n  className=\"btn-counter\"\n  )\n  ]\n  )\n  ]\n  )\n", ["pyfyre.widgets"]], "pyfyre.user.src.components.experiment": [".py", "from pyfyre.widgets import *\n\nclass Experiment(Container):\n def __init__(self):\n  super().__init__(\n  className=\"test\",\n  children=[\n  Text(\n  \"Try to experiment, edit the `src/main.py` and wait for it to reload automatically on a liveserver. Anyways, I'm a component!\",\n  className=\"desc\"\n  )\n  ]\n  )\n", ["pyfyre.widgets"]], "pyfyre.user.src.components": [".py", "", [], 1], "pyfyre.user.src.css": [".py", "", [], 1], "pyfyre.widgets.button": [".py", "from pyfyre.widgets.widget import Widget\n\nclass Button(Widget):\n ''\n\n\n\n\n\n\n\n\n \n \n def __init__(self,textContent,onClick=lambda :print(\"\"),className=\"\",props:dict=None ):\n  super().__init__(\"button\",className=className,props=props)\n  self.textContent=textContent\n  self.onClick=onClick\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  \n  element.bind(\"click\",self.onClick)\n  \n  return element\n", ["pyfyre.widgets.widget"]], "pyfyre.widgets.clickable": [".py", "from pyfyre.widgets.widget import Widget\n\nclass Clickable(Widget):\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self,bind,onClick,className=\"\",props:dict=None ):\n  super().__init__(\"div\",className=className,props=props)\n  self.bind=bind\n  self.onclick=onClick\n  \n def dom(self):\n  element=super().dom()\n  \n  element.appendChild(self.bind.dom())\n  \n  element.bind(\"click\",self.onclick)\n  \n  return element\n", ["pyfyre.widgets.widget"]], "pyfyre.widgets.container": [".py", "from pyfyre.widgets.widget import Widget\n\nclass Container(Widget):\n ''\n\n\n\n\n\n\n\n \n \n def __init__(self,children=[],className=\"\",props:dict=None ):\n  super().__init__(\"div\",className=className,props=props)\n  self.children=children\n  \n def dom(self):\n  element=super().dom()\n  \n  for child in self.children:\n   element.appendChild(child.dom())\n   \n  return element\n", ["pyfyre.widgets.widget"]], "pyfyre.widgets.image": [".py", "from pyfyre.widgets.widget import Widget\n\nclass Image(Widget):\n ''\n\n\n\n\n\n \n \n def __init__(self,src,className=\"\",props:dict=None ):\n  super().__init__(\"img\",className=className,props=props)\n  self.src=src\n  \n def dom(self):\n  element=super().dom()\n  element.src=self.src\n  \n  return element\n", ["pyfyre.widgets.widget"]], "pyfyre.widgets.link": [".py", "from pyfyre.widgets.widget import Widget\n\nfrom pyfyre.router import Router\n\nclass Link(Widget):\n ''\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self,textContent:str,to='/',external=False ,className=\"\",props:dict=None ):\n  super().__init__(\"a\",className=className,props=props)\n  self.textContent=textContent\n  self.to=to\n  self.external=external\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  element.href=\"#\"if not self.external else self.to\n  \n  if not self.external:\n   element.bind(\"click\",self.navigate)\n   \n  return element\n  \n def navigate(self,e):\n  e.preventDefault()\n  Router.push(self.to)\n", ["pyfyre.router", "pyfyre.widgets.widget"]], "pyfyre.widgets.listbuilder": [".py", "from pyfyre.widgets.widget import Widget\n\nclass ListBuilder(Widget):\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self,count=1,builder=None ,className=\"\",props:dict=None ):\n  super().__init__(\"div\",className=className,props=props)\n  self.count=count\n  self.builder=builder\n  \n def dom(self):\n  element=super().dom()\n  \n  for i in range(self.count):\n   element.appendChild(self.builder(i).dom())\n   \n  return element\n", ["pyfyre.widgets.widget"]], "pyfyre.widgets.states": [".py", "''\n\nfrom pyfyre.globals import Globals\nfrom pyfyre.widgets.widget import Widget\nfrom pyfyre.core.exceptions import RenderError\n\nclass UsesState:\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self):\n  self.domElement=None\n  \n def build(self):\n  pass\n  \n def dom(self):\n  try :\n   self.domElement=self.build().dom()\n   return self.domElement\n  except Exception as e:\n   if Globals.DEBUG:raise e\n   \n   self.domElement=self.onerror(e).dom()\n   return self.domElement\n   \n def onerror(self,e):\n  ''\n\n\n\n\n\n\n\n\n\n  \n  \n  return RenderError(\"Oh no! Something went wrong. We're working on fixing it.\",e)\n  \n def update(self):\n  ''\n\n\n  \n  \n  parentNode=self.domElement.parentNode\n  self.domElement.remove()\n  self.domElement=self.dom()\n  parentNode.appendChild(self.domElement)\n", ["pyfyre.core.exceptions", "pyfyre.globals", "pyfyre.widgets.widget"]], "pyfyre.widgets.text": [".py", "from pyfyre.widgets.widget import Widget\n\nclass Text(Widget):\n ''\n\n\n\n\n\n\n\n \n \n def __init__(self,textContent:str,className=\"\",props:dict=None ):\n  super().__init__(\"p\",className=className,props=props)\n  self.textContent=textContent\n  \n def dom(self):\n  element=super().dom()\n  element.textContent=self.textContent\n  \n  return element\n", ["pyfyre.widgets.widget"]], "pyfyre.widgets.textinput": [".py", "from pyfyre.core.exceptions import InvalidController\nfrom pyfyre.widgets.widget import Widget\n\nclass TextInput(Widget):\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self,controller=None ,onInput=None ,defaultValue=\"\",className=\"\",props:dict=None ):\n  super().__init__(\"input\",className=className,props=props)\n  self.controller=controller\n  self.onInput=onInput\n  self.defaultValue=defaultValue\n  \n def dom(self):\n  element=super().dom()\n  \n  element.value=self.defaultValue\n  \n  if self.controller:\n   self.controller.callback(self)\n   \n   def bindController(event):\n    self.controller.state=element.value\n    \n   element.bind('input',bindController)\n   \n   if self.controller.state:\n    element.value=self.controller.state\n    \n  if self.onInput:\n  \n   def wrapper(event):\n    self.onInput(element.value)\n    \n   element.bind('input',wrapper)\n   \n  return element\n  \nclass TextInputController:\n ''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n \n def __init__(self):\n  self.this=None\n  self.state=None\n  \n  \n  self.readOnly=False\n  self.disabled=False\n  \n def changeAttribute(self,readOnly=False ,disabled=False ):\n  if not self.this or not isinstance(self.this,TextInput):\n   raise InvalidController(\"Looks like you haven't called this controller as a parameter controller of TextInput or you provided an invalid controller.\")\n   \n  self.readOnly=readOnly\n  self.disabled=disabled\n  \n  if self.readOnly:\n   self.this.element.attrs['readonly']=None\n  else :\n   if 'readonly'in self.this.element.attrs:\n    del self.this.element.attrs['readonly']\n    \n  if self.disabled:\n   self.this.element.attrs['disabled']=None\n  else :\n   if 'disabled'in self.this.element.attrs:\n    del self.this.element.attrs['disabled']\n    \n def callback(self,this:TextInput):\n  ''\n\n\n  \n  self.this=this\n  \n @property\n def value(self):\n  return self.this.element.value\n  \n def setValue(self,newValue):\n  self.state=newValue\n", ["pyfyre.core.exceptions", "pyfyre.widgets.widget"]], "pyfyre.widgets.widget": [".py", "from browser import document\n\nclass Widget:\n\n def __init__(self,tagname:str,*,className,props:dict=None ):\n  self.tagname=tagname\n  self.className=className\n  self.element=None\n  self.props=props if props is not None else {}\n  \n def dom(self):\n  element=document.createElement(self.tagname)\n  element.className=self.className\n  \n  self.element=element\n  \n  for key,value in self.props.items():\n   element.attrs[key]=value\n   \n  return element\n", ["browser"]], "pyfyre.widgets": [".py", "from pyfyre.widgets.button import Button\nfrom pyfyre.widgets.container import Container\nfrom pyfyre.widgets.image import Image\nfrom pyfyre.widgets.link import Link\nfrom pyfyre.widgets.listbuilder import ListBuilder\nfrom pyfyre.widgets.states import UsesState\nfrom pyfyre.widgets.text import Text\nfrom pyfyre.widgets.textinput import TextInput,TextInputController\n\n__all__=[\n'Button','Container','Image',\n'Link','ListBuilder','UsesState',\n'Text','TextInput','TextInputController'\n]\n", ["pyfyre.widgets.button", "pyfyre.widgets.container", "pyfyre.widgets.image", "pyfyre.widgets.link", "pyfyre.widgets.listbuilder", "pyfyre.widgets.states", "pyfyre.widgets.text", "pyfyre.widgets.textinput"], 1]}
__BRYTHON__.update_VFS(scripts)
