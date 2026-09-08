file = '3d-test.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Patch buildScene
old = 'function buildScene(gltf) {\n    placeTableSet(gltf, -7.0, 0, -Math.PI / 2);\n    placeTableSet(gltf,  7.0, 0,  Math.PI / 2);\n    gltfReady = true;\n    tryReveal();\n  }'

new = '''function buildScene(gltf) {
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

if old in content:
    content = content.replace(old, new)
    print("buildScene patched OK")
else:
    print("FAIL buildScene, len:", len(old))
    # Debug: find approximate match
    idx = content.find('function buildScene')
    print(repr(content[idx:idx+250]))

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
