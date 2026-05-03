# -*- coding: utf-8 -*-
import re

original_make_card_back = '''  function makeCardBackTex() {
    const W = 760, H = 468;
    const c = document.createElement('canvas');
    c.width = W; c.height = H;
    const ctx = c.getContext('2d');
    ctx.fillStyle = '#0d0d0d';
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = 'bold 126px "Bebas Neue", Impact, sans-serif';
    ctx.fillText('4 PASOS', W / 2, H / 2);
    // Añadir el mismo borde sutil que la carta CSS
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, 1); ctx.lineTo(W, 1); ctx.stroke();
    const tex = new THREE.CanvasTexture(c);
    tex.minFilter  = THREE.LinearFilter;   // sin blur de mipmaps al girar
    tex.magFilter  = THREE.LinearFilter;
    tex.anisotropy = 16;
    tex.needsUpdate = true;
    return tex;
  }'''

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove input-3d-overlay
text = re.sub(r'<!-- OVERLAY INPUT DEL 3D -->.*?</div>', '', text, flags=re.DOTALL)

# 2. Revert makeCardBackTex
m = re.search(r'// Global map for dynamic texture update.*?return window\.sharedCardBackTex;\n  \}', text, flags=re.DOTALL)
if m:
    text = text.replace(m.group(0), original_make_card_back)

# 3. Revert scTitle initialization if it is sc-title-wrap
text = text.replace("document.getElementById('sc-title-wrap')", "document.getElementById('sc-title')")

# 4. Revert the earlier HTML change I did to #sc-intro (where I added an input and deleted h2)
m2 = re.search(r'<div id=\"sc-title-wrap\"[^>]*>.*?</div>', text, flags=re.DOTALL)
if m2:
    text = text.replace(m2.group(0), '<h2 id="sc-title" class="title">4 PASOS</h2>')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Reverted 3D test file')
