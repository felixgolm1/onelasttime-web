with open('3d-test.html','r',encoding='utf-8') as f: current=f.read()
with open('3d-test-git.html','r',encoding='utf-8') as f: git=f.read()

print('Current (truncated):', len(current))
print('Git version:', len(git))

# Current file ends with PROC_BRAIN. We need to append the tail from git.
# The tail starts at the renderer.render(scene,camera) call in git,
# BUT we need to inject the brain render call INSIDE it.

# In git, the render section starts before renderer.render and ends with });()
# Let's find the exact block in git:
git_render_start = git.find('    renderer.render(scene, camera);')
git_render_block = git[git_render_start:]
# Find the animate IIFE closing that wraps the render
git_rAF_end = git.find('  })();\n\n  window.addEventListener', git_render_start)
print('Render block:', git_render_start, '-> animate end:', git_rAF_end)

# Extract: from git, from the render call to end of animate + rest of file
# We need everything from 'renderer.render' back to find the IIFE start
# Actually let's find '  (function animate()'
animate_start = git.rfind('  (function animate()', 0, git_render_start)
if animate_start < 0:
    # Try to find the IIFE start
    animate_start = git.rfind('\n\n  (function', 0, git_render_start)
print('animate start in git:', animate_start)

# Get the tail: from animate_start in git to end of git
git_tail = git[animate_start:]
print('Git tail length:', len(git_tail))
print('Git tail start:', repr(git_tail[:150]))

# Now inject brain render call into the tail
# Replace the simple render block with enhanced version
old_render_in_tail = '    renderer.render(scene, camera);\n    cssRenderer.render(scene, camera);\n\n    // Render separado de la carta GLB en su canvas transparente\n    if (cardRenderer2 && cardScene2 && cardCam2 && globalGlbCard && globalGlbCard.visible) {\n      cardRenderer2.render(cardScene2, cardCam2);\n    }\n  })();'

new_render_in_tail = '''    renderer.render(scene, camera);
    cssRenderer.render(scene, camera);

    // Render del cerebro en su canvas dedicado
    if (brainRenderer && brainScene && brainCam && window.brainPivot && window.brainPivot.visible) {
      const hp = brainUniforms.uProgress.value;
      const tt = brainUniforms.uTime.value;
      if (window.updateBrainVertexColors) window.updateBrainVertexColors(hp, tt);

      // Phase-based rim lights
      const ss2 = function(a,b,x){const t=Math.max(0,Math.min(1,(x-a)/(b-a)));return t*t*(3-2*t);};
      if (window.rimLight1) window.rimLight1.intensity = ss2(0.0,0.30,hp)*(1-ss2(0.45,0.65,hp))*1.8;
      if (window.rimLight2) window.rimLight2.intensity = ss2(0.25,0.58,hp)*(1-ss2(0.68,0.85,hp))*2.0;
      if (window.rimLight3) window.rimLight3.intensity = ss2(0.60,0.90,hp)*1.6;
      if (window.brainInteriorLight) {
        window.brainInteriorLight.intensity = ss2(0.28,0.58,hp)*(1-ss2(0.72,0.90,hp))*3.5*(0.85+Math.sin(tt*2.1)*0.15);
      }
      if (window.insulaSphere) {
        window.insulaSphere.material.opacity = ss2(0.62,0.85,hp)*0.85*(0.7+Math.sin(tt*1.3)*0.3);
        window.insulaSphere.scale.setScalar(1.0+Math.sin(tt*1.3)*0.15);
      }
      if (window.brainComposer) window.brainComposer.render();
      else brainRenderer.render(brainScene, brainCam);
    }

    // Render separado de la carta GLB en su canvas transparente
    if (cardRenderer2 && cardScene2 && cardCam2 && globalGlbCard && globalGlbCard.visible) {
      cardRenderer2.render(cardScene2, cardCam2);
    }
  })();'''

if old_render_in_tail in git_tail:
    git_tail = git_tail.replace(old_render_in_tail, new_render_in_tail)
    print('Render injected OK')
else:
    print('WARNING: old render not found, appending tail as-is')

# Now we also need to add brain HTML before </body>
brain_html = '''
  <!-- Brain canvas is created dynamically by JS -->

  <!-- BRAIN UI PANEL -->
  <div id="brain-ui" style="position:fixed; right:5vw; top:50%; transform:translateY(-50%); opacity:0; pointer-events:none; z-index:10010; color:white; font-family:'Inter', sans-serif; transition: opacity 0.5s ease; background: rgba(10,15,10,0.85); backdrop-filter: blur(10px); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); width: 320px; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
    <div style="font-size: 10px; letter-spacing: 2px; color: #a3ff00; font-weight: 700; margin-bottom: 10px;">ACTIVIDAD CEREBRAL</div>
    <div id="brain-title" style="font-size: 32px; font-weight: 700; margin-bottom: 15px; font-family: 'Playfair Display', serif; color: #a0d2ff; transition: color 0.5s ease;">Small Talk</div>
    <div style="width: 100%; height: 2px; background: rgba(255,255,255,0.1); margin-bottom: 15px; position: relative;">
        <div id="brain-progress-bar" style="position: absolute; left: 0; top: 0; height: 100%; width: 0%; background: #a3ff00; transition: width 0.3s ease;"></div>
    </div>
    <div id="brain-desc" style="font-size: 13px; line-height: 1.6; color: #e0e0e0;">Actividad superficial. Se liberan niveles basales de dopamina. Perfecto para romper el hielo y crear confort inicial.</div>
  </div>

<!-- ======= BRAIN ANATOMICAL ANNOTATIONS OVERLAY ======= -->
<style>
  #brain-annotations {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    z-index: 10009; pointer-events: none;
    font-family: 'Inter', sans-serif;
  }
  .bann { position: absolute; width:100%; height:100%; opacity: 0; transition: opacity 0.7s ease; }
  .bann.active { opacity: 1; }
  .bann-dot {
    position: absolute; width: 8px; height: 8px; border-radius: 50%;
    transform: translate(-50%, -50%); animation: ann-pulse 2s ease-out infinite;
  }
  @keyframes ann-pulse {
    0%   { box-shadow: 0 0 0 0 currentColor; }
    70%  { box-shadow: 0 0 0 10px transparent; }
    100% { box-shadow: 0 0 0 0 transparent; }
  }
  .bann-label { position: absolute; transform: translateY(-50%); text-align: right; }
  .bann-phase { font-size: 8px; letter-spacing: 2px; font-weight: 700; text-transform: uppercase; opacity: 0.6; margin-bottom: 2px; }
  .bann-name { font-size: 12px; font-weight: 700; color: #fff; line-height: 1.25; margin-bottom: 3px; }
  .bann-chem { font-size: 10px; font-weight: 600; letter-spacing: 0.5px; }
  .bann-emo  { font-size: 10px; color: rgba(255,255,255,0.50); margin-top: 1px; }
  .bann-line { transition: opacity 0.7s ease; }
</style>

<div id="brain-annotations">
  <svg id="bann-svg" style="position:absolute;top:0;left:0;width:100%;height:100%;overflow:visible;" pointer-events="none">
    <line class="bann-line" id="bl1" x1="38%" y1="28%" x2="28%" y2="34%" stroke="#a0d2ff" stroke-width="1" stroke-dasharray="3 5" opacity="0"/>
    <line class="bann-line" id="bl2" x1="36%" y1="47%" x2="24%" y2="47%" stroke="#ffb347" stroke-width="1" stroke-dasharray="3 5" opacity="0"/>
    <line class="bann-line" id="bl3" x1="34%" y1="59%" x2="22%" y2="58%" stroke="#ffcc00" stroke-width="1" stroke-dasharray="3 5" opacity="0"/>
  </svg>
  <div class="bann" id="bann-1">
    <div class="bann-dot" style="left:38%;top:28%;background:#a0d2ff;color:#a0d2ff;"></div>
    <div class="bann-label" style="left:3%;top:34%;">
      <div class="bann-phase" style="color:#a0d2ff;">Fase 1 · Hielo</div>
      <div class="bann-name">Corteza Prefrontal<br>Dorsolateral</div>
      <div class="bann-chem" style="color:#a0d2ff;">Adrenalina</div>
      <div class="bann-emo">Filtrado de seguridad</div>
    </div>
  </div>
  <div class="bann" id="bann-2">
    <div class="bann-dot" style="left:36%;top:47%;background:#ffb347;color:#ffb347;"></div>
    <div class="bann-label" style="left:3%;top:47%;">
      <div class="bann-phase" style="color:#ffb347;">Fase 2 · Conexion</div>
      <div class="bann-name">Nucleo Accumbens<br>/ C. Cingulada</div>
      <div class="bann-chem" style="color:#ffb347;">Dopamina</div>
      <div class="bann-emo">Recompensa cognitiva</div>
    </div>
  </div>
  <div class="bann" id="bann-3">
    <div class="bann-dot" style="left:34%;top:59%;background:#ffcc00;color:#ffcc00;"></div>
    <div class="bann-label" style="left:3%;top:58%;">
      <div class="bann-phase" style="color:#ffcc00;">Fase 3 · Flow</div>
      <div class="bann-name">Insula + Prefrontal<br>Ventromedial</div>
      <div class="bann-chem" style="color:#ffcc00;">Oxitocina</div>
      <div class="bann-emo">Vinculo inquebrantable</div>
    </div>
  </div>
</div>

<script>
  function updateBrainAnnotations(heatP, brainVisible) {
    const a1=document.getElementById('bann-1'), a2=document.getElementById('bann-2'), a3=document.getElementById('bann-3');
    if(!a1) return;
    const show = brainVisible && heatP > 0.02;
    const s1=show&&heatP<0.40, s2=show&&heatP>=0.30&&heatP<0.72, s3=show&&heatP>=0.62;
    a1.classList.toggle('active',s1); a2.classList.toggle('active',s2); a3.classList.toggle('active',s3);
    const op = function(id,v){const el=document.getElementById(id); if(el) el.style.opacity=v;};
    op('bl1',s1?'0.7':'0'); op('bl2',s2?'0.7':'0'); op('bl3',s3?'0.7':'0');
  }
  window.updateBrainAnnotations = updateBrainAnnotations;
</script>
'''

# Insert brain_html before </body> in git_tail
git_tail = git_tail.replace('\n</body>\n</html>\n', brain_html + '\n</body>\n</html>\n')

# Assemble final file
final = current + git_tail
print('Final file size:', len(final))

with open('3d-test.html','w',encoding='utf-8') as f: f.write(final)
print('Recovery complete!')
