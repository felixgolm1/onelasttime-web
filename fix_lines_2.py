# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Inject the dynamic text splitter script
splitter_script = '''
  function splitFltChars(selector) {
'''

new_splitter = '''
      function wrapDynText() {
        document.querySelectorAll('.dyn-text').forEach(container => {
            let nodes = Array.from(container.childNodes);
            container.innerHTML = '';
            let spans = [];
            
            nodes.forEach(node => {
                if (node.nodeType === 3) {
                    let words = node.nodeValue.split(' ');
                    words.forEach((w, i) => {
                        if (w === '' && i === words.length - 1) return;
                        let s = document.createElement('span');
                        s.textContent = w + (i < words.length - 1 ? ' ' : '');
                        container.appendChild(s);
                        spans.push(s);
                    });
                } else {
                    let s = document.createElement('span');
                    s.appendChild(node.cloneNode(true));
                    s.innerHTML += ' ';
                    container.appendChild(s);
                    spans.push(s);
                }
            });
            
            let lines = [];
            let current = [];
            let lastY = -1;
            spans.forEach(s => {
                let y = Math.round(s.getBoundingClientRect().top);
                if (lastY === -1) lastY = y;
                if (Math.abs(y - lastY) > 5) {
                    lines.push(current);
                    current = [];
                    lastY = y;
                }
                current.push(s);
            });
            if (current.length) lines.push(current);
            
            container.innerHTML = '';
            container.style.display = 'block';
            lines.forEach(line => {
                let lineWrap = document.createElement('div');
                lineWrap.style.overflow = 'hidden';
                let inner = document.createElement('div');
                inner.className = 'glass-mask-line';
                line.forEach(s => inner.appendChild(s));
                lineWrap.appendChild(inner);
                container.appendChild(lineWrap);
            });
        });
      }
      wrapDynText();
      window.addEventListener('resize', () => {
         // Optionally re-wrap on resize, but since it's an entrance animation, doing it once on load is fine.
      });

  function splitFltChars(selector) {
'''

content = content.replace(splitter_script, new_splitter)

# Replace GSAP set
old_set = "gsap.set('#glass-who .glass-mask-inner, #glass-objectives .glass-mask-inner', { yPercent: 110 });"
new_set = "gsap.set('#glass-who .glass-mask-line, #glass-objectives .glass-mask-line', { yPercent: 110 });"
content = content.replace(old_set, new_set)

# Replace GSAP tweens
old_anim1 = "scrollTl.to('#glass-who .glass-mask-inner', { yPercent: 0, duration: 0.02, stagger: 0, ease: 'power2.out' }, t + 0.01);"
new_anim1 = "scrollTl.to('#glass-who .glass-mask-line', { yPercent: 0, duration: 0.02, stagger: 0, ease: 'power2.out' }, t + 0.01);"
content = content.replace(old_anim1, new_anim1)

old_anim2 = "scrollTl.to('#glass-who .glass-mask-inner', { yPercent: 110, duration: 0.01 }, t);"
new_anim2 = "scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.01 }, t);"
content = content.replace(old_anim2, new_anim2)

old_anim3 = "scrollTl.to('#glass-objectives .glass-mask-inner', { yPercent: 0, duration: 0.02, stagger: 0, ease: 'power2.out' }, t + 0.01);"
new_anim3 = "scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 0, duration: 0.02, stagger: 0, ease: 'power2.out' }, t + 0.01);"
content = content.replace(old_anim3, new_anim3)

old_anim4 = "scrollTl.to('#glass-objectives .glass-mask-inner', { yPercent: 110, duration: 0.01 }, t);"
new_anim4 = "scrollTl.to('#glass-objectives .glass-mask-line', { yPercent: 110, duration: 0.01 }, t);"
content = content.replace(old_anim4, new_anim4)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
