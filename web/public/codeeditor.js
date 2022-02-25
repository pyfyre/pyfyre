var CodeMirrorAPI = { codeMirror: null };
PyFyreDOM.addListener(() => {
    CodeMirrorAPI.codeMirror = CodeMirror.fromTextArea(
        document.getElementById("code-editor"),
        { lineNumbers: !0, mode: "python", tabSize: 6, tabindex: 20 }
    );
    CodeMirrorAPI.codeMirror.setSize(width = "100%", height = "100%");
    CodeMirrorAPI.codeMirror.on("change", () => {
      CodeListen.broadcast();
    });
    CodeMirrorAPI.codeMirror.setValue(`class App(UsesState):
  def build(self):
    return Text("Hello, World")
  
runApp(App())`)
});
var CodeListen = {
  listeners: [],
  listen: (e) => {
    CodeListen.listeners.push(e);
  },
  broadcast: () => {
    for (var e = 0; e < CodeListen.listeners.length; e++)
      CodeListen.listeners[e]();
  },
};
