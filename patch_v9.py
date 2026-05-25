import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add an error callback to gltfLoader.load('assets/models/human_brain.glb', ...)
# The signature is loader.load( url, onLoad, onProgress, onError );
# Currently it is: gltfLoader.load('assets/models/human_brain.glb', (gltf) => { ... })
# Let's replace the whole load call.

new_load = """
    gltfLoader.load('assets/models/human_brain.glb',
      (gltf) => {
        globalBrainMesh = gltf.scene;
        globalBrainMesh.scale.setScalar(5.0); 
        globalBrainMesh.position.set(0, 0, 0);
        
        const brainPivot = new THREE.Group();
        brainPivot.add(globalBrainMesh);
        
        const testMat = new THREE.MeshBasicMaterial({ color: 0xff0000, wireframe: true });
        
        globalBrainMesh.traverse(child => {
          if (child.isMesh) {
            child.material = testMat;
          }
        });
        
        document.getElementById('brain-ui').querySelector('div').innerText = "CEREBRO RED WIREFRAME";
        
        brainPivot.visible = false;
        brainPivot.position.set(0, 0, -5); 
        scene.add(brainPivot);
        window.brainPivot = brainPivot;
      },
      undefined,
      (err) => {
          document.getElementById('brain-ui').querySelector('div').innerText = "ERROR 3D: " + err.message;
          console.error(err);
      }
    );
"""

# Replace existing load call
text = re.sub(r"gltfLoader\.load\('assets/models/human_brain\.glb'.*?window\.brainPivot = brainPivot;\s*\}\s*\);", new_load, text, flags=re.DOTALL)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch v9 applied (Error Catching)")
