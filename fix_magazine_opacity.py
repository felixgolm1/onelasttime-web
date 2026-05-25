import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_logic = """if (webglCanvas) { webglCanvas.style.opacity = op3D; webglCanvas.style.pointerEvents = op3D > 0 ? 'auto' : 'none'; }
      if (cssContainer) { cssContainer.style.opacity = op3D; cssContainer.style.pointerEvents = op3D > 0 ? 'auto' : 'none'; }"""

new_logic = """if (webglCanvas) { webglCanvas.style.opacity = op3D; webglCanvas.style.pointerEvents = op3D > 0 ? 'auto' : 'none'; }
      if (cssContainer) { cssContainer.style.opacity = op3D; cssContainer.style.pointerEvents = op3D > 0 ? 'auto' : 'none'; }
      const cCanvas = document.getElementById('card-canvas');
      if (cCanvas) { cCanvas.style.opacity = op3D; cCanvas.style.pointerEvents = op3D > 0 ? 'auto' : 'none'; }
      const cTable = document.getElementById('card-table');
      if (cTable) { cTable.style.opacity = op3D; cTable.style.pointerEvents = op3D > 0 ? 'auto' : 'none'; }
      const overlay = document.getElementById('scene-overlay');
      if (overlay) { overlay.style.opacity = op3D; }
"""

if old_logic in text:
    text = text.replace(old_logic, new_logic)
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed opacity for card-canvas and card-table.")
else:
    print("Could not find old_logic in text.")
