import os
import re

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the math in smoothScrollLoop
content = re.sub(
    r"let swapProg = glowTSwap / 4\.80; // \(10\.57 / 2\.2 = 4\.80\)",
    "let swapProg = glowTSwap / (scrollTl.duration() / 2.2);",
    content
)

# And in the initialization block
content = re.sub(
    r"let swapProg = glowTSwap / 4\.80; // \(10\.57 / 2\.2 = 4\.80\)",
    "let swapProg = glowTSwap / (scrollTl.duration() / 2.2);",
    content
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
