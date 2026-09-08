import re

file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Patch buildScene to be mobile-aware
old_buildScene = """    function buildScene(gltf) {
      placeTableSet(gltf, -7.0, 0, -Math.PI / 2);
      placeTableSet(gltf,  7.0, 0,  Math.PI / 2);
      gltfReady = true;
      tryReveal();
    }"""

new_buildScene = """    function buildScene(gltf) {
      const isMobile = window.innerWidth <= 768;
      if (isMobile) {
        // Mobile: platos arriba y abajo (eje Z), mesa rotada 90° en Y
        placeTableSet(gltf,  0, -7.0, 0);
        placeTableSet(gltf,  0,  7.0, Math.PI);
      } else {
        // Desktop: platos izquierda y derecha (eje X)
        placeTableSet(gltf, -7.0, 0, -Math.PI / 2);
        placeTableSet(gltf,  7.0, 0,  Math.PI / 2);
      }
      gltfReady = true;
      tryReveal();
    }"""

if old_buildScene in content:
    content = content.replace(old_buildScene, new_buildScene)
else:
    print("WARNING: Could not find buildScene function")

# 2. Patch placeWineGlass calls to be mobile-aware
old_glass = """        (gltf) => {
          placeWineGlass(gltf, -3.0, +2.4);
          placeWineGlass(gltf,  3.0, -2.4);
        },"""

new_glass = """        (gltf) => {
          const isMob = window.innerWidth <= 768;
          if (isMob) {
            // Mobile: copas adelante y atrás, centradas en X
            placeWineGlass(gltf,  0, -4.2);
            placeWineGlass(gltf,  0,  4.2);
          } else {
            placeWineGlass(gltf, -3.0, +2.4);
            placeWineGlass(gltf,  3.0, -2.4);
          }
        },"""

if old_glass in content:
    content = content.replace(old_glass, new_glass)
else:
    print("WARNING: Could not find placeWineGlass calls")

# 3. Patch camera FOV / position to be mobile-aware
old_camera_init = """    const camera = new THREE.PerspectiveCamera(42, window.innerWidth / window.innerHeight, 0.1, 100);
    window.camera = camera;
    camera.position.set(-0.3, 12, 3);
    camera.lookAt(0, 0, 0);"""

new_camera_init = """    const _isMobileScene = window.innerWidth <= 768;
    const camera = new THREE.PerspectiveCamera(_isMobileScene ? 55 : 42, window.innerWidth / window.innerHeight, 0.1, 100);
    window.camera = camera;
    camera.position.set(_isMobileScene ? 0 : -0.3, _isMobileScene ? 14 : 12, _isMobileScene ? 0 : 3);
    camera.lookAt(0, 0, 0);"""

if old_camera_init in content:
    content = content.replace(old_camera_init, new_camera_init)
else:
    print("WARNING: Could not find camera init")

# 4. Patch CAM_BASE to be mobile-aware
old_cam_base = "    const CAM_BASE = { x: -0.3, y: 12, z: 3 };"
new_cam_base = "    const CAM_BASE = _isMobileScene ? { x: 0, y: 14, z: 0 } : { x: -0.3, y: 12, z: 3 };"

if old_cam_base in content:
    content = content.replace(old_cam_base, new_cam_base)
else:
    print("WARNING: Could not find CAM_BASE")

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done patching 3D scene for mobile table rotation.")
