# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

new_tex = r'''  // Global map for dynamic texture update
  window.sharedCardBackTex = null;
  window.sharedCardBackCanvas = null;
  window.sharedCardBackCtx = null;
  window.dynamicNameValue = '';

  function makeCardBackTex() {
    const W = 760, H = 468;
    
    let c = window.sharedCardBackCanvas;
    let ctx = window.sharedCardBackCtx;
    
    if(!c) {
      c = document.createElement('canvas');
      c.width = W; c.height = H;
      ctx = c.getContext('2d');
      window.sharedCardBackCanvas = c;
      window.sharedCardBackCtx = ctx;
    }
    
    // Background
    ctx.fillStyle = '#0d0d0d';
    ctx.fillRect(0, 0, W, H);
    
    // Top text (Hola,)
    ctx.fillStyle = 'rgba(255,255,255,0.45)';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '300 42px "Bebas Neue", Impact, sans-serif';
    ctx.fillText('Hola,', W / 2, H / 2 - 50);
    
    // Bottom line & text
    ctx.font = '400 90px "Bebas Neue", Impact, sans-serif';
    
    const displayStr = window.dynamicNameValue || 'tu nombre';
    // Subtle opacity when empty placeholder
    if(!window.dynamicNameValue) {
      ctx.fillStyle = 'rgba(255,255,255,0.2)';
    } else {
      ctx.fillStyle = '#ccff00';
    }
    
    ctx.fillText(displayStr, W / 2, H / 2 + 30);
    
    // Green underline
    ctx.strokeStyle = window.dynamicNameValue ? '#ccff00' : 'rgba(255,255,255,0.2)';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(W/2 - 180, H/2 + 85);
    ctx.lineTo(W/2 + 180, H/2 + 85);
    ctx.stroke();

    // Subtle edge
    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(0, 1); ctx.lineTo(W, 1); ctx.stroke();
    
    if(!window.sharedCardBackTex) {
      const tex = new THREE.CanvasTexture(c);
      tex.minFilter  = THREE.LinearFilter;
      tex.magFilter  = THREE.LinearFilter;
      tex.anisotropy = 16;
      window.sharedCardBackTex = tex;
    } else {
      window.sharedCardBackTex.needsUpdate = true;
    }
    
    return window.sharedCardBackTex;
  }
'''

invis_overlay = r'''
  <!-- OVERLAY INPUT DEL 3D -->
  <div id="input-3d-overlay" style="position: fixed; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 280px; height: 180px; z-index: 10005; pointer-events: none; display: flex; justify-content: center; align-items: center;">
     <input id="hidden-3d-input" type="text" maxlength="20" placeholder="tu nombre" style="width: 100%; height: 100%; opacity: 0; cursor: text; font-size: 80px;">
  </div>
'''

listener_injection = r'''    // Sincronizar input 3D <-> Input CSS
    const input3D = document.getElementById('hidden-3d-input');
    const inputCSS = document.getElementById('sc-name-input');
    const overlay3D = document.getElementById('input-3d-overlay');

    if(input3D && inputCSS) {
        input3D.addEventListener('input', () => {
            inputCSS.value = input3D.value;
            window.dynamicNameValue = input3D.value;
            makeCardBackTex(); // Updates THREE texture dynamically
        });
        inputCSS.addEventListener('input', () => {
            input3D.value = inputCSS.value;
            window.dynamicNameValue = inputCSS.value;
            makeCardBackTex();
        });
    }

    // El input será clickeable mid-scroll. GSAP controla todo en onUpdate del timeline.
    // Buscamos el bloque de `scrollTl = gsap.timeline({ ... onUpdate: () => { ... } })`
    // No hace falta pointer-events riguroso si solo está en esa zona, pero para ser exhaustivos:
'''

original_tex_func = r'function makeCardBackTex\(\) \{.*?(?=  // Textura de grano procedural)'

# perform substitutions
text = re.sub(original_tex_func, new_tex, text, flags=re.DOTALL)
if 'hidden-3d-input' not in text:
    text = text.replace('<body>', '<body>' + invis_overlay)
    
if 'input3D.addEventListener' not in text:
    text = text.replace('/*  EDGE GLOW', listener_injection + '\n  /*  EDGE GLOW')

# We need to make the hidden 3D input clickable during the second phase of the card intro.
# Inside updateFaceSwap() function, or inside the master GSAP timeline onUpdate.
# find updateFaceSwap:
update_face_swap_code = r'''
    function updateFaceSwap(rot) {
      // rot goes from 0 to -540. The back face is visible between -90 and -270
      // We activate pointer-events if we are in that range!
      if (rot <= -90 && rot > -270) {
        if (!facingBack) { facingBack = true; toggleNodes(true); }
        if (overlay3D) overlay3D.style.pointerEvents = "auto";
      } else {
        if (facingBack) { facingBack = false; toggleNodes(false); }
        if (overlay3D) { overlay3D.style.pointerEvents = "none"; input3D.blur(); }
      }
'''
text = re.sub(r'function updateFaceSwap\(rot\) \{.*?(?=if \(rot \<\= \-90)', update_face_swap_code, text, flags=re.DOTALL)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Patched successfully.')
