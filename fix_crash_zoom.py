import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. placeTableSet
content = re.sub(
    r"const isMobile = window\.matchMedia\('\(max-width: 768px\)'\)\.matches;\s*const targetWidth = isMobile \? 9\.0 \* 1\.3 : 9\.0;",
    "const targetWidth = 9.0;",
    content
)

# 2. placeWineGlass
content = re.sub(
    r"const isMobile = window\.matchMedia\('\(max-width: 768px\)'\)\.matches;\s*const targetH = isMobile \? 4\.16 \* 1\.3 : 4\.16;",
    "const targetH = 4.16;",
    content
)

# 3. polaroidMesh
content = re.sub(
    r"const polS = window\.matchMedia\('\(max-width: 768px\)'\)\.matches \? 0\.83 \* 1\.3 : 0\.83;\s*window\.polaroidMesh\.scale\.set\(polS, polS, polS\);",
    "window.polaroidMesh.scale.set(0.83, 0.83, 0.83);",
    content
)

# 4. Change camera Y from 26 to 20 for mobile
content = content.replace(
    "camera.position.set(_isMobileScene ? 0 : -0.3, _isMobileScene ? 26 : 12, _isMobileScene ? 0 : 3);",
    "camera.position.set(_isMobileScene ? 0 : -0.3, _isMobileScene ? 20 : 12, _isMobileScene ? 0 : 3);"
)

content = content.replace(
    "const CAM_BASE = _isMobileScene ? { x: 0, y: 26, z: 0 } : { x: -0.3, y: 12, z: 3 };",
    "const CAM_BASE = _isMobileScene ? { x: 0, y: 20, z: 0 } : { x: -0.3, y: 12, z: 3 };"
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted scale and adjusted camera Y")
