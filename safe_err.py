import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

safe_error = """<script>
window.onerror = function(msg, url, line, col, err) {
  let d = document.createElement('div');
  d.style.cssText = 'position:fixed;top:0;left:0;z-index:9999999;background:red;color:white;padding:20px;font-size:24px;width:100%;';
  d.innerHTML = '<b>JS ERROR:</b> ' + msg + ' <br>Line: ' + line;
  document.body.appendChild(d);
};
</script>"""

if "<b>JS ERROR:</b>" not in content:
    content = content.replace("<head>", "<head>\n" + safe_error)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Safe error handler injected.")
