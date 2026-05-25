import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace ANY bracket that comes right after updateGlobalScenes();
content = re.sub(
    r"updateGlobalScenes\(\);\s*\}\s*//",
    r"updateGlobalScenes();\n\n          //",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
