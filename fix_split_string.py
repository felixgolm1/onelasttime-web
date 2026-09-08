# -*- coding: utf-8 -*-
import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

start_str = "    function splitFltChars(selector) {"
end_str = "    const leftChars  = splitFltChars('.flt-in');"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
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
    }
'''
    
    content = content[:start_idx] + new_split + content[end_idx:]

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
