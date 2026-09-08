file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Camera - use 2-space indentation
old_cam = "  const camera = new THREE.PerspectiveCamera(42, window.innerWidth / window.innerHeight, 0.1, 100);\n  window.camera = camera;\n  camera.position.set(-0.3, 12, 3);\n  camera.lookAt(0, 0, 0);"

new_cam = """  const _isMobileScene = window.innerWidth <= 768;
  const camera = new THREE.PerspectiveCamera(_isMobileScene ? 56 : 42, window.innerWidth / window.innerHeight, 0.1, 100);
  window.camera = camera;
  camera.position.set(_isMobileScene ? 0 : -0.3, _isMobileScene ? 15 : 12, _isMobileScene ? 0 : 3);
  camera.lookAt(0, 0, 0);"""

if old_cam in content:
    content = content.replace(old_cam, new_cam)
    print("Camera patched OK")
else:
    idx = content.find('const camera = new THREE.PerspectiveCamera(42')
    print("FAIL camera at idx:", idx)
    print(repr(content[idx:idx+300]))

# CAM_BASE - use 2-space indentation  
old_base = "  const CAM_BASE = { x: -0.3, y: 12, z: 3 };"
new_base = "  const CAM_BASE = _isMobileScene ? { x: 0, y: 15, z: 0 } : { x: -0.3, y: 12, z: 3 };"
if old_base in content:
    content = content.replace(old_base, new_base)
    print("CAM_BASE patched OK")
else:
    idx = content.find('CAM_BASE = {')
    print("FAIL CAM_BASE")
    print(repr(content[idx-5:idx+80]))

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done.")
