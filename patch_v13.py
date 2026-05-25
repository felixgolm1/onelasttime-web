import os

dev_file = 'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'

with open(dev_file, 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace the traversal logic in gltfLoader.load to count elements and apply material to anything that has a material

new_traversal = """
        let meshCount = 0;
        globalBrainMesh.traverse(child => {
          if (child.isMesh || child.isLine || child.isPoints) {
            meshCount++;
            child.material = brainMat;
            child.frustumCulled = false;
          }
        });
        
        uiText.innerText = `ACTIVIDAD CEREBRAL (${meshCount} MESHES)`;
"""

text = text.replace("""
        globalBrainMesh.traverse(child => {
          if (child.isMesh) {
            child.material = brainMat;
            child.frustumCulled = false;
          }
        });
        
        uiText.innerText = "ACTIVIDAD CEREBRAL";
""".strip(), new_traversal.strip())

with open(dev_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch v13 applied (Mesh Counter)")
