#

# -*- coding: utf-8 -*-
import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    content = f.read()

# 1. Replace #visible-input-overlay
old_html = '''  <!-- OPCION B: Input HTML visible perfectamente sincronizado con WebGL -->
  <div id="visible-input-overlay" style="position: fixed; inset: 0; pointer-events: none; z-index: 10050; display: flex; align-items: center; justify-content: center;">
    <div id="visible-input-group" style="width: 380px; height: 234px; pointer-events: none; transform-style: preserve-3d; opacity: 0;">
      <!-- scaleX(-1) deshace el espejo cuando rotationY llega a -180 o -540 -->
      <div style="position: absolute; inset: 0; transform: scaleX(-1); display: flex; flex-direction: column; align-items: center; justify-content: center; pointer-events: none;">
        <div style="display: flex; align-items: center; justify-content: center;">
          <!-- Texto Hola transparente para ocupar el mismo espacio que en WebGL y empujar el input a la derecha -->
          <span style="font-family:'Poppins',sans-serif; font-weight:600; font-size:32px; color:transparent; pointer-events:none; user-select:none; -webkit-user-select:none;">Hola</span>
          <input type="text" id="neon-html-input" maxlength="15" autocomplete="off" spellcheck="false" autocorrect="off" autocapitalize="off" data-gramm="false" style="pointer-events: auto; background: transparent; border: none; color: transparent; font-family: 'Inter', sans-serif; font-weight:600; font-size: 32px; width: 300px; text-align: left; outline: none; margin-left: 8px; caret-color: transparent; padding-top: 5px;">
        </div>
      </div>
    </div>
  </div>'.replace("\r", "")

new_html = '''  <!-- OPCION B: Input HTML visible perfectamente sincronizado con WebGL -->
  <div id="visible-input-overlay" style="position: fixed; inset: 0; pointer-events: none; z-index: 10050; display: flex; align-items: center; justify-content: center;">
    <div id="visible-input-group" style="width: 380px; height: 234px; pointer-events: none; transform-style: preserve-3d; opacity: 0; background: #0d0d0d; border-radius: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: inset 0 0 0 1.5px #ccff00, 0 10px 30px rgba(0,0,0,0.8); transition: box-shadow 0.3s ease;">
      <div style="transform: scaleX(-1); width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; position: relative;">
        
        <!-- FASE 1: Input de Nombre -->
        <div id="dial-phase-1" style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; position: absolute; top: 0; left: 0; transition: opacity 0.5s, transform 0.5s;">
          <span style="font-family:'Poppins',sans-serif; font-weight:600; font-size:32px; color:#ffffff;">Hola</span>
          <input type="text" id="neon-html-input" maxlength="15" autocomplete="off" spellcheck="false" autocorrect="off" autocapitalize="off" placeholder="tu nombre" style="pointer-events: auto; background: transparent; border: none; color: #ccff00; font-family: 'Inter', sans-serif; font-weight:600; font-size: 32px; width: 180px; text-align: left; outline: none; margin-left: 8px; padding-top: 5px;">
          <button id="dial-next-btn" style="pointer-events: auto; background: none; border: none; color: #ccff00; font-size: 28px; cursor: pointer; opacity: 0.5; transition: opacity 0.2s;">&#10140;</button>
        </div>

        <!-- FASE 2: Dial de Profundidad -->
        <div id="dial-phase-2" style="display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 100%; position: absolute; top: 0; left: 0; opacity: 0; pointer-events: none; transition: opacity 0.5s, transform 0.5s; padding: 20px; box-sizing: border-box;">
          <p id="dial-title" style="font-family:'Inter', sans-serif; color:#ffffff; font-size: 14px; text-align: center; margin-bottom: 25px; font-weight: 500; opacity: 0.8;"></p>
          
          <input type="range" id="depth-slider" min="0" max="100" value="0" style="pointer-events: auto; width: 80%; accent-color: #ccff00; cursor: pointer;">
          <div style="display: flex;-justify-content: space-between; width: 80%; margin-top: 5px;">
            <span style="font-family:'Inter',sans-serif; font-size:10px; color:#ffffff; opacity:0.5;">Superficial</span>
            <span style="font-family:'Inter',sans-serif; font-size:10px; color:#ffffff; opacity:0.5;">Profundo</span>
          </div>

          <p id="dial-question" style="font-family:'Poppins', sans-serif; color:#ccff00; font-size: 15px; font-weight: 600; text-align: center; margin-top: 20px; min-height: 48px; line-height: 1.3;">\u00bfCu\u00e1l es tu pel\u00edcula favorita?</p>
        </div>

      </div>
    </div>
  </div>'''.replace("\r", "")

content = content.replace("leight: 234px", "height: 234px") # clean up
content = content.replace(old_html, new_html)

# 2. Update makeCardBackTex
pat_backtex = r"(if \(typeof data === 'object' && data\.type === 'name_input'\) \{:)"
rep_backtex = rb"\1\n      return globalBackCv;\n"
local_content = content.encode("utf-8")
local_content = re.sub(pat_backtex.encode("utf-8"), rep_backtex, local_content)
content = local_content.decode("utf-8")

# 3. Update smoothScrollLoop
pat_loop = r"function smoothScrollLoop\(\) \{\s*try \{\s*const lerpF = 0\.40;"
rep_loop = '''function smoothScrollLoop() {
      try {
      const lerpF = 0.40;
      
      if (window.isDialLocked === undefined) window.isDialLocked = true;
      if (window.isDialLocked && targetProg > 0.763) {
          targetProg = 0.763;
      }'''
content = re.sub(pat_loop, rep_loop, content)

# 4. Update wheel and totÚ[Ý™B˜ÛÛ[HÛÛ[œ™\XÙJÚ[™ÝË˜Y]™[\Ý[™\Š	ÝÚY[	ËHOˆ×ˆKœ™]™[Y˜][

NÈ‹Ú[™ÝË˜Y]™[\Ý[™\Š	ÝÚY[	ËHOˆ×ˆYŠK\™Ù]YÓ˜[YHOOH	ÒS”U	ÈK\™Ù]YÓ˜[YHOOH	Ð•UÓ‰ÊH™]\›Ž×ˆKœ™]™[Y˜][

NÈŠB˜ÛÛ[HÛÛ[œ™\XÙJÚ[™ÝË˜Y]™[\Ý[™\Š	ÝÝ6†Ö÷fRrÂRÓâµÆâRç&WfVçDFVfVÇB‚“²"Â'v–æF÷ræFDWfVçDÆ—7FVæW"‚wF÷V6†Ö÷fRrÂRÓâµÆâ–b†RçF&vWBçFtæÖRÓÓÒt”åUBrÇÂRçF&vWBçFtæÖRÓÓÒt%UEDôâr’&WGW&ãµÆâRç&WfVçDFVfVÇB‚“²" ¢2RâVæBF–Â67&—@¦F–Å÷67&—BÒrrp¢Ç67&—Cà¢Fö7VÖVçBæFDWfVçDÆ—7FVæW"‚tDôÔ6öçFVçDÆöFVBrÂ‚’Óâ°¢6öç7BæW‡D'FâÒFö7VÖVçBævWDVÆVÖVçD'”–B‚vF–ÂÖæW‡BÖ'Fâr“°¢6öç7B†6SÒFö7VÖVçBævWDVÆVÖVçD'”–B‚vF–Â×†6RÓr“°¢6öç7B†6S"ÒFö7VÖVçBævWDVÆVÖVçD'”–B‚vF–Â×†6RÓ"r“°¢6öç7BF—FÆRÒFö7VÖVçBævWDVÆVÖVçD'”–B‚vF–Â×F—FÆRr“°¢6öç7B6Æ–FW"ÒFö7VÖVçBævWDVÆVÖVçD'”–B‚vepth-slider');
      const question = document.getElementById('dial-question');
      const nameInput = document.getElementById('neon-html-input');

      const questions = [
        '\u00bfCu\u00e1l es tu serie favorita?',
        '\u00bfQu\u00e9 talento in\u00fatil tienes?',
        '\u00bfCu\u00e1ndo fue la\u00a0 \u00faltima vez que re\u00edste a carcajadas?',
        '\u00bfQu\u00e9 es lo que mà\u00e1s te gusta de tu vida ahora mismo?',
        '\u00bfQu\u00e9 te daba miedo de peque\u00f1o y ahora no?',
        'Si pudieras revivir un solo d\u00eea, \u00bfcu\u00e1l ser\u00eda?',
        '\u00bfQu\u00e9 sue\u00f1o has abandonado por miedo?',
        '\u00bfCu\u00e1ndo fue la\u00a0 \u00faltima vez que te sentiste muy solo?',
        '\u00bfQu\u00e9 es lo que nunca le has perdonado a tus padres?',
        'Si hoy fuera tu \u00fartimo d\u00eea, \u00bfa qui\u00e9n llamar\u00edas?'
      ];

      nextBtn.addEventListener('click', () => {
        let name = nameInput.value.trim() || 'Desconocido';
        title.innerHTML = `<b>${name}</b>, \u00bfhasta d\u00f3nde quieres llegar?`;
        
        phase1.style.transform = 'translateY(-20px)';
        phase1.style.opacity = '0';
        
        setTimeout(() => {
          phase1.style.pointer-events = 'none';
          phase2.style.pointer-events = 'auto';
          phase2.style.transform = 'translateY(0)';
          phase2.style.opacity = '1';
        }, 500);
      });

      slider.addEventListener('input', (e) => {
        let val = parseInt(e.target.value);
        let index = Math.floor((val / 100) * (questions.length - 1));
        question.textContent = questions[index];
        
        let glow = (val / 100) * 30;
        document.getElementById('visible-input-group').style.box-shadow = `inset 0 0 0 1.5px #ccff00, 0 10px 30px rgba(0,0,0,0.8), 0 0 ${glow}px rgba(204,255,0,0.6)`;
        
        if (val === 100) {
          window.isDialLocked = false;
          question.style.textShadow = '0 0 10px #ccff00';
          slider.style.pointer-events = 'none';
          setTimeout(() => {
            question.textContent = '\u00a1Sigue haciendo scroll!';
            question.style.color = '#fff';
            question.style.textShadow = 'none';
          }, 1500);
        }
      });
      
      nameInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
          nextBtn.click();
        }
      });
      
      nameInput.addEventListener('input', (e) => {
        if(e.target.value.trim().length > 0) {
          nextBtn.style.opacity = '1';
        } else {
          nextBtn.style.opacity = '0.5';
        }
      });
    });
  </script>
''.codecomas("\r\n", "\n")

content = content.replace('</body>', dial_script + '\n\n</body>')

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)
