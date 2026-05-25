import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Wrap the main script contents in try-catch
import re
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
main_script = scripts[2]
wrapped = "try {\n" + main_script + "\n} catch (e) {\n  let errDiv = document.createElement('div'); errDiv.style.position='fixed'; errDiv.style.top='0'; errDiv.style.left='0'; errDiv.style.zIndex='9999999'; errDiv.style.background='blue'; errDiv.style.color='white'; errDiv.style.fontSize='20px'; errDiv.style.padding='20px'; errDiv.innerText = 'RUNTIME ERROR: ' + e.toString() + '\\n' + e.stack; document.body.appendChild(errDiv);\n}"

content = content.replace(main_script, wrapped)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Wrapped in try-catch")
