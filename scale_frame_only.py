import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r"#magazine-border-svg, \.carousel-viewport \{ transform: translateY\(-4\.5vh\) !important; \}"
replacement = r"#magazine-border-svg, .carousel-viewport { transform: translateY(-4.5vh) scale(1.10) !important; }"

content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
