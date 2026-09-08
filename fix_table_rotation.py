file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert buildScene to original
old_bs = '''function buildScene(gltf) {
      const isMobile = window.innerWidth <= 768;
      if (isMobile) {
        // Mobile: platos arriba y abajo (eje Z)
        placeTableSet(gltf,  0, -7.0, 0);
        placeTableSet(gltf,  0,  7.0, Math.PI);
      } else {
        placeTableSet(gltf, -7.0, 0, -Math.PI / 2);
        placeTableSet(gltf,  7.0, 0,  Math.PI / 2);
      }
      gltfReady = true;
      tryReveal();
    }'''

new_bs = '''function buildScene(gltf) {
    placeTableSet(gltf, -7.0, 0, -Math.PI / 2);
    placeTableSet(gltf,  7.0, 0,  Math.PI / 2);
    gltfReady = true;
    tryReveal();
  }'''

if old_bs in content:
    content = content.replace(old_bs, new_bs)
    print("buildScene reverted OK")
else:
    print("FAIL buildScene revert")

# 2. Revert wine glasses to original
old_glass = """      (gltf) => {
        const isMob = window.innerWidth <= 768;
        if (isMob) {
          placeWineGlass(gltf,  0, -5.0);
          placeWineGlass(gltf,  0,  5.0);
        } else {
          placeWineGlass(gltf, -3.0, +2.4);
          placeWineGlass(gltf,  3.0, -2.4);
        }
      },"""

new_glass = """      (gltf) => {
        placeWineGlass(gltf, -3.0, +2.4);
        placeWineGlass(gltf,  3.0, -2.4);
      },"""

if old_glass in content:
    content = content.replace(old_glass, new_glass)
    print("Wine glass reverted OK")
else:
    print("FAIL wine glass revert")

# 3. Fix camera: rotate 90° using camera.up for mobile
# Straight-down camera (0, 22, 0) with up.set(1,0,0) 
# makes X axis appear as vertical → tables at x:±7 appear top/bottom
old_cam_line = "  camera.position.set(_isMobileScene ? 0 : -0.3, _isMobileScene ? 20 : 12, _isMobileScene ? 0 : 3);\n  camera.lookAt(0, 0, 0);"

new_cam_line = """  camera.position.set(_isMobileScene ? 0 : -0.3, _isMobileScene ? 22 : 12, _isMobileScene ? 0 : 3);
  if (_isMobileScene) camera.up.set(1, 0, 0); // rotate view 90° so x-axis plates appear top/bottom
  camera.lookAt(0, 0, 0);"""

if old_cam_line in content:
    content = content.replace(old_cam_line, new_cam_line)
    print("Camera patched OK")
else:
    print("FAIL camera patch")
    idx = content.find("camera.position.set(_isMobileScene")
    if idx > -1:
        print("Found at:", idx, repr(content[idx:idx+200]))

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")
