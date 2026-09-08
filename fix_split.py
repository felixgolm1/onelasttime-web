# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_split = '''    function splitFltChars(selector) {

      const chars = [];
      document.querySelectorAll(selector).forEach(span => {
        const text = span.textContent;
        span.textContent = '';
        [...text].forEach(ch => {
          const el = document.createElement('span');
          el.className = 'flt-ch';
          el.style.display = 'inline-block';
          el.textContent = ch === ' ' ? '\u00a0' : ch;
          span.appendChild(el);
          chars.push(el);
        });
      });
      return chars;
    }'''

new_split = '''    function splitFltChars(selector) {
      const chars = [];
      document.querySelectorAll(selector).forEach(span => {
        const text = span.textContent;
        span.textContent = '';
        
        const words = text.split(' ');
        words.forEach((word, wIdx) => {
           const wordSpan = document.createElement('span');
           wordSpan.style.whiteSpace = 'nowrap';
           wordSpan.style.display = 'inline-block';
           
           [...word].forEach(ch => {
             const el = document.createElement('span');
             el.className = 'flt-ch';
             el.style.display = 'inline-block';
             el.textContent = ch;
             wordSpan.appendChild(el);
             chars.push(el);
           });
           
           span.appendChild(wordSpan);
           
           if (wIdx < words.length - 1) {
               const spaceEl = document.createElement('span');
               spaceEl.className = 'flt-ch';
               spaceEl.style.display = 'inline-block';
               spaceEl.innerHTML = '&nbsp;';
               span.appendChild(spaceEl);
               chars.push(spaceEl);
           }
        });
      });
      return chars;
    }'''
content = content.replace(old_split, new_split)

# Fix bullet point opacity
old_bullet = '''<li style="color: rgba(255,255,255,0.7); display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-bullet" style="color: rgba(204,255,0,0.7);">&#8226;</div></div><div class="dyn-text">Mi ex (solo para valientes... o insensatxs).</div></li>'''
new_bullet = '''<li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-bullet" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mi ex (solo para valientes... o insensatxs).</div></li>'''
content = content.replace(old_bullet, new_bullet)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
