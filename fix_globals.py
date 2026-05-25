import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

brain_decls = """
  // ===== BRAIN VARIABLES =====
  let brainCanvasEl = null, brainRenderer = null, brainScene = null, brainCam = null;
  let css2DRenderer = null;
  window.brainPivot = null;
  window.brainMeshes = [];
  window.brainUniforms = { uProgress: { value: 0.0 }, uTime: { value: 0.0 } };
"""

# Find maxProg = 20.0;
text = text.replace('const maxProg = 20.0;', 'const maxProg = 20.0;\n' + brain_decls)

# Because we changed it to window.brainUniforms just to be safe, replace all other brainUniforms
text = text.replace('brainUniforms', 'window.brainUniforms')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Injected brain_decls successfully.")
