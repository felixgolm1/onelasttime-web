import re

file_path = "3d-test.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = r"#magazine-scene \{ width: 98vw; height: 141vw; \}"
replacement = r"#magazine-scene { width: 108vw; height: 155vw; }"
content = re.sub(target, replacement, content)

target = r"#camera-flash-container \{ width: 98vw; height: 141vw; \}"
replacement = r"#camera-flash-container { width: 108vw; height: 155vw; }"
content = re.sub(target, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
