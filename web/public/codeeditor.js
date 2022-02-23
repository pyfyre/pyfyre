var CodeMirrorAPI = {
    codeMirror: null
}

PyFyreDOM.addListener(() => {
    CodeMirrorAPI.codeMirror = CodeMirror.fromTextArea(
        document.getElementById("code-editor"), {
            lineNumbers: true,
            mode: "python",
            tabSize: 6,
            tabindex: 20,
            value: `class App(UsesState):
            def build(self):
                return Container(
                  children=[
                     Text("Hello, World")
                  ]
                )
                
          runApp(App())`
        }
    )

    CodeMirrorAPI.codeMirror.setSize(width="100%", height="100%")

    CodeMirrorAPI.codeMirror.on("change", () => {
        CodeListen.broadcast();
    })
});

var CodeListen = {
    listeners: [],

    listen: (fun) => {
        CodeListen.listeners.push(fun);
    },

    broadcast: () => {
        for (var i = 0; i < CodeListen.listeners.length; i++) {
            CodeListen.listeners[i]();
        }
    }
}