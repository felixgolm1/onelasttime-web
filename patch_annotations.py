with open('3d-test.html','r',encoding='utf-8') as f: text=f.read()

# ---- Replace CSS ----
old_style = '''<!-- ======= BRAIN ANATOMICAL ANNOTATIONS OVERLAY ======= -->
<style>
  #brain-annotations {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    z-index: 10009; pointer-events: none;
    font-family: 'Inter', sans-serif;
  }
  .bann { position: absolute; opacity: 0; transition: opacity 0.7s ease; }
  .bann.active { opacity: 1; }

  /* Pulsing dot on brain region */
  .bann-dot {
    position: absolute;
    width: 10px; height: 10px; border-radius: 50%;
    background: white;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 0 0 rgba(255,255,255,0.6);
    animation: ann-pulse 1.8s ease-out infinite;
  }
  @keyframes ann-pulse {
    0%   { box-shadow: 0 0 0 0 rgba(255,255,255,0.7); }
    70%  { box-shadow: 0 0 0 12px rgba(255,255,255,0); }
    100% { box-shadow: 0 0 0 0 rgba(255,255,255,0); }
  }

  /* Glass info card */
  .bann-card {
    position: absolute;
    width: 210px;
    background: rgba(6,12,8,0.78);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
    padding: 14px 16px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  }
  .bann-tag {
    font-size: 9px; letter-spacing: 2.5px; font-weight: 700;
    text-transform: uppercase; color: #a3ff00; margin-bottom: 6px;
  }
  .bann-area {
    font-size: 13px; font-weight: 700; color: #fff; margin-bottom: 8px;
    line-height: 1.3;
  }
  .bann-row { font-size: 11px; color: rgba(255,255,255,0.65); margin-bottom: 3px; line-height: 1.5; }
  .bann-row strong { color: rgba(255,255,255,0.9); }
</style>'''

new_style = '''<!-- ======= BRAIN ANATOMICAL ANNOTATIONS OVERLAY ======= -->
<style>
  #brain-annotations {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    z-index: 10009; pointer-events: none;
    font-family: 'Inter', sans-serif;
  }
  .bann { position: absolute; width:100%; height:100%; opacity: 0; transition: opacity 0.7s ease; }
  .bann.active { opacity: 1; }

  .bann-dot {
    position: absolute;
    width: 8px; height: 8px; border-radius: 50%;
    transform: translate(-50%, -50%);
    animation: ann-pulse 2s ease-out infinite;
  }
  @keyframes ann-pulse {
    0%   { box-shadow: 0 0 0 0 currentColor; }
    70%  { box-shadow: 0 0 0 10px transparent; }
    100% { box-shadow: 0 0 0 0 transparent; }
  }
  .bann-label {
    position: absolute;
    transform: translateY(-50%);
    text-align: right;
  }
  .bann-phase {
    font-size: 8px; letter-spacing: 2px; font-weight: 700;
    text-transform: uppercase; opacity: 0.6; margin-bottom: 2px;
  }
  .bann-name { font-size: 12px; font-weight: 700; color: #fff; line-height: 1.25; margin-bottom: 3px; }
  .bann-chem { font-size: 10px; font-weight: 600; letter-spacing: 0.5px; }
  .bann-emo  { font-size: 10px; color: rgba(255,255,255,0.50); margin-top: 1px; }
  .bann-line { transition: opacity 0.7s ease; }
</style>'''

if old_style in text:
    text = text.replace(old_style, new_style)
    print('CSS OK')
else:
    print('CSS NOT FOUND'); exit(1)

# ---- Replace HTML ----
old_html_start = '<div id="brain-annotations">\n\n  <!-- FASE 1: Corteza Prefrontal Dorsal'
old_html_end = '</div>\n\n<script>\n  // Show correct annotation based on brain heatmap progress'

si = text.find(old_html_start)
ei = text.find(old_html_end, si)
print(f'HTML block: {si} -> {ei}')

new_html = '''<div id="brain-annotations">
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
  // Show correct annotation based on brain heatmap progress'''

text = text[:si] + new_html + text[ei + len(old_html_end):]
# Put back the script closing
text = text[:si + len(new_html)] + '\n  function updateBrainAnnotations(heatP, brainVisible) {\n    const a1=document.getElementById(\'bann-1\'), a2=document.getElementById(\'bann-2\'), a3=document.getElementById(\'bann-3\');\n    if(!a1) return;\n    const show = brainVisible && heatP > 0.02;\n    const s1=show&&heatP<0.40, s2=show&&heatP>=0.30&&heatP<0.72, s3=show&&heatP>=0.62;\n    a1.classList.toggle(\'active\',s1); a2.classList.toggle(\'active\',s2); a3.classList.toggle(\'active\',s3);\n    const op = function(id,v){const el=document.getElementById(id); if(el) el.style.opacity=v;};\n    op(\'bl1\',s1?\'0.7\':\'0\'); op(\'bl2\',s2?\'0.7\':\'0\'); op(\'bl3\',s3?\'0.7\':\'0\');\n  }\n  window.updateBrainAnnotations = updateBrainAnnotations;\n</script>\n\n</body>\n</html>\n' + text[text.find('</body>', si + len(new_html)) + len('</body>\n</html>\n'):]

with open('3d-test.html','w',encoding='utf-8') as f: f.write(text)
print('All done')
