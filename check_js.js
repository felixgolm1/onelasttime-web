var fso = new ActiveXObject("Scripting.FileSystemObject");
var f = fso.OpenTextFile("c:\\Users\\Félix Gol\\.gemini\\antigravity\\scratch\\sensibles-web\\3d-test.html", 1);
var html = f.ReadAll();
f.Close();

// Extract scripts
var scripts = html.match(/<script\b[^>]*>([\s\S]*?)<\/script>/gi);
if (scripts) {
    for (var i=0; i<scripts.length; i++) {
        var code = scripts[i].replace(/<script\b[^>]*>/i, "").replace(/<\/script>/i, "");
        try {
            var fn = new Function(code);
        } catch(e) {
            WScript.Echo("Error in script " + i + ": " + e.message);
        }
    }
}
WScript.Echo("Done parsing JS.");
