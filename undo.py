import re

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove UI
text = re.sub(r"<!-- Brain Heatmap UI -->.*?<!-- Debug: Mostrar scroll prog -->", "<!-- Debug: Mostrar scroll prog -->", text, flags=re.DOTALL)

# Remove Globals
text = re.sub(r"// ── BRAIN 3D MODEL & SHADER ──.*?let pendingGltf = null;", "let pendingGltf = null;", text, flags=re.DOTALL)

# Remove Load GLB
text = re.sub(r"gltfLoader\.load\('assets/models/human_brain\.glb'.*?window\.brainPivot = brainPivot;\s*\},.*?console\.error\('Error loading human_brain\.glb:', err\);\s*\}\s*\);\s*", "", text, flags=re.DOTALL)

# Remove Scroll Logic
scroll_logic_pattern = r"// --- PORTAL EFFECT & BRAIN ---.*?\}\s*\}\s*\} else \{.*?if \(brainUI\) brainUI\.style\.opacity = '0';\s*\}"
text = re.sub(scroll_logic_pattern, "", text, flags=re.DOTALL)

# Remove Loop Time injection
text = re.sub(r"if\(typeof brainUniforms !== 'undefined'\) brainUniforms\.uTime\.value = t;\s*\n\s*", "", text)

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Undo applied!")
