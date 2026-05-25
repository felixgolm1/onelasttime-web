import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the GLB loader callback
new_loader = """
      (gltf) => {
        globalBrainMesh = gltf.scene;
        
        // FORCING SCALE TO BYPASS BOX CALCULATION ISSUES
        // Try a medium scale first. If it's a typical model, 1, 10, or 100 will show something.
        globalBrainMesh.scale.setScalar(5.0); 
        globalBrainMesh.position.set(0, 0, 0);
        
        const brainPivot = new THREE.Group();
        brainPivot.add(globalBrainMesh);
        
        // Force a basic solid RED material to rule out Shader bugs completely!
        const testMat = new THREE.MeshBasicMaterial({ color: 0xff0000, wireframe: true });
        
        globalBrainMesh.traverse(child => {
          if (child.isMesh) {
            child.material = testMat;
          }
        });
        
        document.getElementById('brain-ui').querySelector('div').innerText = "CEREBRO RED WIREFRAME";
        
        brainPivot.visible = false;
        brainPivot.position.set(0, 0, -5); // Closer to camera just in case
        scene.add(brainPivot);
        window.brainPivot = brainPivot;
      }
"""

text = re.sub(r"\(gltf\) => \{.*?window\.brainPivot = brainPivot;\s*\}", new_loader, text, flags=re.DOTALL)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch v8 applied (Wireframe + Force Scale)")
