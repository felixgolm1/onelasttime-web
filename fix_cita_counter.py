import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_block = '''    <!-- Titulo verde superior -->
  <div style="text-align:center; margin-bottom: 14px;">
    <span style="color:#ccff00; font-family:'Inter','Helvetica Neue',sans-serif; font-size:14px; font-weight:600; display:flex; align-items:center; justify-content:center; gap:3px; text-transform:uppercase;">Desde la cita 1 hasta la <span style="font-size:26px; line-height:0; margin-top:-2px;">&infin;</span></span>
  </div>
  <!-- Barra scrubber: input[range] nativo (con contador flotante) -->
  <div style="position:relative; height:28px; display:flex; align-items:center; margin-top:6px;">
    <div style="position:absolute; left:0; right:0; top:50%; height:2px; transform:translateY(-50%); background:rgba(255,255,255,0.15); border-radius:2px; pointer-events:none;"></div>
    
    <input id="envej-range" type="range" min="0" max="9999" value="0" step="1" oninput="window.envejSeekByRange(this.value); document.getElementById('envej-bar-thumb').classList.add('has-interacted');" style="position:absolute; inset:0; width:100%; height:100%; opacity:0; cursor:grab; margin:0; padding:0; z-index:10;">
    <div id="envej-bar-fill" style="position:absolute; left:0; top:50%; height:2px; transform:translateY(-50%); background:#ccff00; width:0%; border-radius:2px; pointer-events:none; transition: width 0.1s linear;"></div>
    <div id="envej-bar-thumb" style="position:absolute; top:50%; transform:translate(-50%,-50%); width:32px; height:18px; border-radius:9px; background:#ccff00; left:0%; pointer-events:none; box-shadow:0 0 8px rgba(204,255,0,0.4); display:flex; align-items:center; justify-content:space-between; padding:0 5px; box-sizing:border-box; transition:transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;">
      <svg xmlns="http://www.w3.org/2000/svg" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-top:1px;"><polyline points="15 18 9 12 15 6"></polyline></svg>
      <svg xmlns="http://www.w3.org/2000/svg" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-top:1px;"><polyline points="9 18 15 12 9 6"></polyline></svg>
      <!-- Contador flotante (CITA X) -->
      <div style="position:absolute; bottom:22px; left:50%; transform:translateX(-50%); display:flex; gap:4px; align-items:baseline; white-space:nowrap; pointer-events:none;">
        <span style="color:#fff; font-family:'Inter','Helvetica Neue',sans-serif; font-size:12.5px; font-weight:400; line-height:1.6; letter-spacing:0.05em; text-transform:uppercase;">Cita</span>
        <span id="envej-cita-num" style="color:#fff; font-family:'Inter','Helvetica Neue',sans-serif; font-size:12.5px; font-weight:400; line-height:1.6; letter-spacing:0.05em; text-transform:uppercase;">1</span>
      </div>
    </div>
  </div>'''

new_block = '''    <!-- Titulo verde superior -->
  <div style="text-align:center; margin-bottom: 8px;">
    <span style="color:#ccff00; font-family:'Inter','Helvetica Neue',sans-serif; font-size:14px; font-weight:600; display:flex; align-items:center; justify-content:center; gap:3px; text-transform:uppercase;">Desde la cita 1 hasta la <span style="font-size:26px; line-height:0; margin-top:-2px;">&infin;</span></span>
  </div>

  <!-- Contador estatico (CITA X) -->
  <div style="text-align:center; display:flex; justify-content:center; gap:4px; align-items:baseline; margin-bottom: 6px; pointer-events:none;">
    <span style="color:#fff; font-family:'Inter','Helvetica Neue',sans-serif; font-size:12.5px; font-weight:400; line-height:1.6; letter-spacing:0.05em; text-transform:uppercase;">Cita</span>
    <span id="envej-cita-num" style="color:#fff; font-family:'Inter','Helvetica Neue',sans-serif; font-size:12.5px; font-weight:400; line-height:1.6; letter-spacing:0.05em; text-transform:uppercase;">1</span>
  </div>

  <!-- Barra scrubber: input[range] nativo -->
  <div style="position:relative; height:28px; display:flex; align-items:center; margin-top:2px;">
    <div style="position:absolute; left:0; right:0; top:50%; height:2px; transform:translateY(-50%); background:rgba(255,255,255,0.15); border-radius:2px; pointer-events:none;"></div>
    
    <input id="envej-range" type="range" min="0" max="9999" value="0" step="1" oninput="window.envejSeekByRange(this.value); document.getElementById('envej-bar-thumb').classList.add('has-interacted');" style="position:absolute; inset:0; width:100%; height:100%; opacity:0; cursor:grab; margin:0; padding:0; z-index:10;">
    <div id="envej-bar-fill" style="position:absolute; left:0; top:50%; height:2px; transform:translateY(-50%); background:#ccff00; width:0%; border-radius:2px; pointer-events:none; transition: width 0.1s linear;"></div>
    <div id="envej-bar-thumb" style="position:absolute; top:50%; transform:translate(-50%,-50%); width:32px; height:18px; border-radius:9px; background:#ccff00; left:0%; pointer-events:none; box-shadow:0 0 8px rgba(204,255,0,0.4); display:flex; align-items:center; justify-content:space-between; padding:0 5px; box-sizing:border-box; transition:transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;">
      <svg xmlns="http://www.w3.org/2000/svg" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-top:1px;"><polyline points="15 18 9 12 15 6"></polyline></svg>
      <svg xmlns="http://www.w3.org/2000/svg" width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-top:1px;"><polyline points="9 18 15 12 9 6"></polyline></svg>
    </div>
  </div>'''

content = content.replace(old_block, new_block)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)

print("Done")
