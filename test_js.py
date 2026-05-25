import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract script blocks
scripts = re.findall(r"<script>([\s\S]*?)</script>", content)
if scripts:
    with open("test.js", "w", encoding="utf-8") as f:
        # We only care about the main script that has smoothScrollLoop
        for s in scripts:
            if "smoothScrollLoop" in s:
                f.write(s)
                break
print("Wrote test.js")
