import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add the HTML element before </body>
content = content.replace(
    "</body>",
    "  <!-- Debug: Mostrar scroll prog -->\n  <div id=\"debug-scroll-prog\" style=\"position: fixed; bottom: 20px; left: 20px; color: #00ff00; font-family: monospace; font-size: 24px; font-weight: bold; z-index: 999999; pointer-events: none; background: rgba(0,0,0,0.5); padding: 5px 10px; border-radius: 5px;\">0.00</div>\n</body>"
)

# 2. Add the update logic inside smoothScrollLoop
content = re.sub(
    r"(updateGlobalScenes\(\);)",
    r"\1\n\n          const debugProg = document.getElementById('debug-scroll-prog');\n          if (debugProg) debugProg.innerText = prog.toFixed(2);",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
