# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

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

    function splitFltChars(selector) {
'''

content = re.sub(r'\s{2,}function splitFltChars\(selector\) \{', new_splitter, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
