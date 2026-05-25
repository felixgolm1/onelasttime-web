import os
import re
import subprocess

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

scripts = re.findall(r"<script>([\s\S]*?)</script>", content)

for i, js_code in enumerate(scripts):
    with open(f"test_script_{i}.js", "w", encoding="utf-8") as temp_js:
        temp_js.write(js_code)
    
    result = subprocess.run(['node', '-c', f"test_script_{i}.js"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error in script {i}:")
        print(result.stderr)
    else:
        print(f"Script {i} is syntactically valid!")
