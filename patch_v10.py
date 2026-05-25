import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will restore the brain shader, but keeping NormalBlending and bright colors.
# I will also perfectly center and scale the brain based on its exact bounding box.
# If the bounding box is 0, I will output an error to the UI.

new_loader = """
      (gltf) => {
        globalBrainMesh = gltf.scene;
        
        // 1. Calculate Exact Size & Center
        const box = new THREE.Box3().setFromObject(globalBrainMesh);
        const size = box.getSize(new THREE.Vector3());
        const center = box.getCenter(new THREE.Vector3());
        const maxDim = Math.max(size.x, size.y, size.z);
        
        const uiText = document.getElementById('brain-ui').querySelector('div');
        
        if (maxDim === 0) {
            uiText.innerText = "ERROR: EL MODELO TIENE TAMAÑO 0";
            return;
        }
        
        // 2. Scale to Exactly 20 units and Center it
        const targetW = 20.0;
        const scale = targetW / maxDim;
        globalBrainMesh.scale.setScalar(scale);
        
        // Offset position so its center is exactly at (0,0,0) of the pivot
        globalBrainMesh.position.set(-center.x * scale, -center.y * scale, -center.z * scale);
        
        const brainPivot = new THREE.Group();
        brainPivot.add(globalBrainMesh);
        
        // 3. Apply the Shader Material
        globalBrainMesh.traverse(child => {
          if (child.isMesh) {
            child.material = brainMat; // Restoring the proper shader
            child.frustumCulled = false; // Prevent culling issues just in case
          }
        });
        
        uiText.innerText = "ACTIVIDAD CEREBRAL"; // Restore original text
        
        brainPivot.visible = false;
        brainPivot.position.set(0, 0, -15);
        scene.add(brainPivot);
        window.brainPivot = brainPivot;
      },
      undefined,
      (err) => {
          document.getElementById('brain-ui').querySelector('div').innerText = "ERROR 3D: " + err.message;
      }
"""

text = re.sub(r"\(gltf\) => \{.*?\}\s*\)", new_loader + ")", text, flags=re.DOTALL)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch v10 applied (Robust Centering + Frustum Fix)")
