import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the cold color bright blue and increase alpha
text = text.replace("vec3 cold = vec3(0.02, 0.0, 0.15);", "vec3 cold = vec3(0.2, 0.5, 1.0); // Bright Blue!")
text = text.replace("float alpha = mix(0.2, 0.95, heat + fresnel*0.5);", "float alpha = mix(0.8, 1.0, heat + fresnel*0.5);")

# Change blending to NormalBlending so it overrides the background instead of getting lost in it
text = text.replace("blending: THREE.AdditiveBlending", "blending: THREE.NormalBlending")

# To debug if the mesh even loads, we inject a visual indicator in the UI
# If the mesh loads, we will change the "Actividad Cerebral" text to "CEREBRO CARGADO"
debug_inject = """
        globalBrainMesh.traverse(child => {
          if (child.isMesh) {
            child.material = brainMat;
          }
        });
        document.getElementById('brain-ui').querySelector('div').innerText = "CEREBRO CARGADO";
"""
text = re.sub(r"globalBrainMesh\.traverse\(child => \{.*?\}\);", debug_inject, text, flags=re.DOTALL)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch v7 applied (Colors + Debug)")
