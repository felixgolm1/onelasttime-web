import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the try-catch wrapper
content = content.replace("<script>try {\n", "<script>\n")
content = re.sub(r'\} catch \(e\) \{\s*let errDiv.*?\}\s*</script>', '\n</script>', content, flags=re.DOTALL)

# 2. Remove the injected window.onerror script
content = re.sub(r'<script>\s*window\.onerror = function.*?</script>', '', content, flags=re.DOTALL)

# 3. Fix the mainDeck reference
content = content.replace(
    "let hiddenFaces = mainDeck.querySelectorAll('.box-flap, .tuck-lip, .dust-flap, .face-back, .face-front, .face-bottom');",
    "let hiddenFaces = document.getElementById('mainDeck').querySelectorAll('.box-flap, .tuck-lip, .dust-flap, .face-back, .face-front, .face-bottom');"
)

# 4. Remove the corrupted "<body>" string inside the JS comment
content = content.replace("<body>\n", "")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("File repaired.")
