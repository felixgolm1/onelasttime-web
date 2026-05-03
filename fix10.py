import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS
css = '''
    /* ── ORYZO REVIEW PANEL ── */
    #oryzo-review {
      position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
      z-index: 9000; pointer-events: none; opacity: 0; visibility: hidden;
      display: flex; flex-direction: column;
      padding: clamp(20px, 4vw, 50px);
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }
    .or-header {
      display: flex; justify-content: space-between; align-items: flex-start;
      margin-bottom: 5vh; opacity: 0; transform: translateY(-20px);
    }
    .or-h-item {
      flex: 1; color: rgba(255,255,255,0.4); font-size: 0.8rem; font-weight: 600; letter-spacing: 0.1em;
    }
    .or-h-center {
      text-align: center; color: #c1ff00;
    }
    .or-star { width: 14px; height: 14px; margin: 0 4px; display: inline-block; }
    .or-content {
      flex: 1; display: flex; gap: 4vw;
    }
    .or-c-left, .or-c-right {
      flex: 1; display: flex; flex-direction: column; justify-content: center;
    }
    .or-story {
      font-family: 'Inter', sans-serif; font-size: clamp(0.9rem, 1.2vw, 1.2rem); font-weight: 400; line-height: 1.6; color: #ffffff;
    }
    #elsa-scroll-video {
      width: clamp(100px, 15vw, 200px); height: auto; border-radius: 8px; margin-top: 3vh;
      filter: grayscale(10%) contrast(1.05); opacity: 0; transform-origin: top left;
      transition: opacity 0.5s ease; pointer-events: none; object-fit: cover;
    }
    .or-quote {
      font-family: 'Playfair Display', serif; font-size: clamp(2rem, 3.5vw, 4rem);
      font-weight: 500; font-style: italic; line-height: 1.2; color: #ffffff; margin-bottom: 2rem;
    }
    .or-author {
      font-size: 1rem; color: #c1ff00; font-weight: 500; opacity: 0; transform: translateX(20px);
    }
'''
content = content.replace('</style>', css + '\n</style>')

# 2. HTML
html = '''
  <div id="oryzo-review">
    <div class="or-header">
      <div class="or-h-item">LA HISTORIA DE ESTA CARTA</div>
      <div class="or-h-item or-h-center">
        <svg viewBox="0 0 100 100" class="or-star"><path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill="currentColor"/></svg>
        <svg viewBox="0 0 100 100" class="or-star"><path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill="currentColor"/></svg>
        <svg viewBox="0 0 100 100" class="or-star"><path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill="currentColor"/></svg>
        <svg viewBox="0 0 100 100" class="or-star"><path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill="currentColor"/></svg>
        <svg viewBox="0 0 100 100" class="or-star"><path d="M50 0 L60 40 L100 50 L60 60 L50 100 L40 60 L0 50 L40 40 Z" fill="currentColor"/></svg>
      </div>
      <div class="or-h-item" style="text-align: right;">EL TESTIMONIO</div>
    </div>
    <div class="or-content">
      <div class="or-c-left">
        <div class="or-story">Es una de las cartas que generamos para Sara y sus amigxs de baile que quisieron tener una conversación con un tono profundo para conocerse más.<br><br>Y como fue un éxito, la hemos aprovechado en otras ocasiones, incluso para convertir primeras citas en segundas.<br><br>¿Con quién te imaginas usando esta carta?</div>
        <video id="elsa-scroll-video" src="assets/img/video_elsa_kf.mp4" muted playsinline preload="auto"></video>
      </div>
      <div class="or-c-right">
        <div class="or-quote">"La utilicé con mi pareja en nuestra cena de aniversario y nos hizo abrirnos sobre temas que llevábamos meses esquivando sin darnos cuenta."</div>
        <div class="or-author">— Elsa & Michel Sants</div>
      </div>
    </div>
  </div>
'''
content = content.replace('<div id="made-by-ai"', html + '\n  <div id="made-by-ai"')


# 3. JS Update Box State
js_logic = '''
      // Lógica de la nueva reseña estilo Oryzo (Elsa)
      const revOryzo = document.getElementById('oryzo-review');
      if (revOryzo) {
        if (prog > 3.2 && prog < 4.5) {
          let scrollP = mapRange(prog, 3.2, 4.5, 0, 1);
          revOryzo.style.visibility = 'visible';
          
          if (scrollP < 0.1) revOryzo.style.opacity = mapRange(scrollP, 0, 0.1, 0, 1);
          else if (scrollP > 0.9) revOryzo.style.opacity = mapRange(scrollP, 0.9, 1.0, 1, 0);
          else revOryzo.style.opacity = '1';

          const header = revOryzo.querySelector('.or-header');
          if (header) {
            header.style.opacity = mapRange(scrollP, 0.05, 0.15, 0, 1);
            header.style.transform = 	ranslateY(px);
          }

          const author = revOryzo.querySelector('.or-author');
          if (author) {
            author.style.opacity = mapRange(scrollP, 0.4, 0.5, 0, 1);
            author.style.transform = 	ranslateX(px);
          }

          const chars = revOryzo.querySelectorAll('.or-char');
          if (chars.length > 0) {
            let textP = mapRange(scrollP, 0.12, 0.325, 0, 1);
            let litCount = Math.floor(textP * chars.length);
            chars.forEach((c, i) => { c.style.opacity = i < litCount ? '1' : '0.2'; });
          }

          const storyChars = revOryzo.querySelectorAll('.or-story-char');
          if (storyChars.length > 0) {
            let storyP = mapRange(scrollP, 0.08, 0.35, 0, 1);
            let litStory = Math.floor(storyP * storyChars.length);
            storyChars.forEach((c, i) => { c.style.opacity = i < litStory ? '1' : '0.3'; });
          }

          const elsaVideo = document.getElementById('elsa-scroll-video');
          if (elsaVideo && elsaVideo.readyState >= 1 && !isNaN(elsaVideo.duration) && elsaVideo.duration > 0) {
            elsaVideo.style.opacity = scrollP > 0.05 ? '1' : '0';
            const maxScrubTime = Math.min(elsaVideo.duration, 4.0);
            let vTarget = mapRange(scrollP, 0.0, 0.8, 0, maxScrubTime);
            let currentVTime = elsaVideo.currentTime;
            elsaVideo.currentTime = currentVTime + (vTarget - currentVTime) * 0.15;
          }
        } else {
          revOryzo.style.opacity = '0';
          revOryzo.style.visibility = 'hidden';
        }
      }
'''
content = content.replace('if (prog > 10.0) {', js_logic + '\n      if (prog > 10.0) {')


# 4. JS Text Wrapping and Kickstart
js_init = '''
      function wrapTextNodes(node, className) {
        if (node.nodeType === 3) {
          const text = node.nodeValue;
          if (text.trim().length === 0) return;
          const fragment = document.createDocumentFragment();
          for (let i = 0; i < text.length; i++) {
            const char = text[i];
            if (char === ' ') {
              fragment.appendChild(document.createTextNode(' '));
            } else {
              const span = document.createElement('span');
              span.className = className;
              span.style.opacity = '0.3';
              span.style.transition = 'opacity 0.05s ease';
              span.textContent = char;
              fragment.appendChild(span);
            }
          }
          node.parentNode.replaceChild(fragment, node);
        } else if (node.nodeType === 1 && node.nodeName !== 'BR') {
          Array.from(node.childNodes).forEach(c => wrapTextNodes(c, className));
        }
      }
      
      const orQuote = document.querySelector('.or-quote');
      if (orQuote) wrapTextNodes(orQuote, 'or-char');

      const orStory = document.querySelector('.or-story');
      if (orStory) wrapTextNodes(orStory, 'or-story-char');

      document.body.addEventListener('pointerdown', function initVideo() {
         const v = document.getElementById('elsa-scroll-video');
         if (v) { v.play().then(() => { v.pause(); }).catch(()=>{}); }
         document.body.removeEventListener('pointerdown', initVideo);
      });
'''
content = content.replace('setupCardTooltip(\'.card-n2\', \'card2-tooltip\', htmlCard2);', js_init + '\n  setupCardTooltip(\'.card-n2\', \'card2-tooltip\', htmlCard2);')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Testimonials injected")
