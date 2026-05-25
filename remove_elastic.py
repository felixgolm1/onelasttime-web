import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Add .box-3d-volume to the list of elements getting their transition disabled
content = re.sub(
    r"mainDeck\.querySelectorAll\('\.box-flap, \.tuck-lip, \.dust-flap, \.interior-cards \.interior-card'\)",
    "mainDeck.querySelectorAll('.box-3d-volume, .box-flap, .tuck-lip, .dust-flap, .interior-cards .interior-card')",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
