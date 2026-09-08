import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace scale: 1.2 with scale: IS_MOB ? 1.45 : 1.2
# Let's define the ternary just as text
new_scale = "scale: window.matchMedia('(max-width: 768px)').matches ? 1.45 : 1.2"

content = content.replace(
    "scale: 1.2, rotation: 0, opacity: 0, zIndex: 5",
    f"{new_scale}, rotation: 0, opacity: 0, zIndex: 5"
)

content = content.replace(
    "scale: 1.2, rotation: -2.5, opacity: 1, zIndex: 10",
    f"{new_scale}, rotation: -2.5, opacity: 1, zIndex: 10"
)

content = content.replace(
    "scale: 1.2, rotation: -2.5, rotationY: 180, rotationX: 0, z: 1",
    f"{new_scale}, rotation: -2.5, rotationY: 180, rotationX: 0, z: 1"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done patching sCards scale for mobile.")
