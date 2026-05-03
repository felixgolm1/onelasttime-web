import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

place_table_set = '''
  function placeTableSet(gltf, xOff, zOff, rotY) {
    const setting = gltf.scene.clone(true);
    const box  = new THREE.Box3().setFromObject(setting);
    const size = box.getSize(new THREE.Vector3());
    const targetWidth = 9.0;
    const scale = targetWidth / Math.max(size.x, size.z);
    setting.scale.setScalar(scale);
    setting.rotation.y = rotY;

    // Centrar en el puesto
    const box2    = new THREE.Box3().setFromObject(setting);
    const center2 = box2.getCenter(new THREE.Vector3());
    setting.position.set(xOff - center2.x, -box2.min.y + 0.003, zOff - center2.z);

    // Sombras + detección de cubiertos por forma alargada -> material plata
    const silverMat = new THREE.MeshStandardMaterial({
      color:           0xf5f6f8,
      roughness:       0.15,
      metalness:       0.98,
      envMapIntensity: 0.0
    });

    setting.traverse(child => {
      if (!child.isMesh) return;
      child.castShadow    = true;
      child.receiveShadow = true;

      // Detectar cubiertos: forma muy alargada en el plano horizontal
      const bb = new THREE.Box3().setFromObject(child);
      const s  = bb.getSize(new THREE.Vector3());
      const maxH = Math.max(s.x, s.z);
      const minH = Math.min(s.x, s.z);
      const isCutlery = (maxH / Math.max(minH, 0.001)) > 2.5;

      if (isCutlery) child.material = silverMat;
    });

    scene.add(setting);
  }
'''

content = content.replace('function placeWineGlass(gltf, xOff, zOff)', place_table_set + '\n  function placeWineGlass(gltf, xOff, zOff)')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 9 done")
