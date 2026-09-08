import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Adjust placeTableSet calls
content = content.replace(
    "placeTableSet(gltf, -7.0, 0, -Math.PI / 2);",
    "placeTableSet(gltf, _isMobileScene ? -7.0 * 0.7 : -7.0, 0, -Math.PI / 2);"
)
content = content.replace(
    "placeTableSet(gltf,  7.0, 0,  Math.PI / 2);",
    "placeTableSet(gltf, _isMobileScene ? 7.0 * 0.7 : 7.0, 0,  Math.PI / 2);"
)

# Adjust placeWineGlass calls
content = content.replace(
    "placeWineGlass(gltf, -3.0, +2.4);",
    "placeWineGlass(gltf, _isMobileScene ? -3.0 * 0.7 : -3.0, +2.4);"
)
content = content.replace(
    "placeWineGlass(gltf,  3.0, -2.4);",
    "placeWineGlass(gltf, _isMobileScene ? 3.0 * 0.7 : 3.0, -2.4);"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Adjusted spacing between table sets")
