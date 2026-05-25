import os
import re
import subprocess

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the main script block
match = re.search(r"<script>\s*(const SC = 512;[\s\S]*?)</script>", content)
if match:
    js_code = match.group(1)
    with open("test_script.js", "w", encoding="utf-8") as temp_js:
        temp_js.write(js_code)
    
    result = subprocess.run(['node', '-c', "test_script.js"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error in script:")
        print(result.stderr)
    else:
        print("Script is syntactically valid!")
else:
    print("Main script block not found.")
