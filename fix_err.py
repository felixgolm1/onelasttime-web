import codecs
import re

content = codecs.open('3d-test.html', 'r', 'utf-8').read()

# Fix window.onerror
old_onerror = r"window\.onerror = function\(msg, url, line, col, err\) \{(?:\r?\n.*?){4}document\.body\.appendChild\(d\);\r?\n\};"
new_onerror = '''window.onerror = function(msg, url, line, col, err) {
  let msgStr = String(msg);
  if (msgStr.toLowerCase().indexOf('script error') > -1 || parseInt(line) === 0 || msgStr.indexOf('Extension') > -1) return;
  let d = document.createElement('div');
  d.style.cssText = 'position:fixed;top:0;left:0;z-index:9999999;background:red;color:white;padding:20px;font-size:24px;width:100%;';
  d.innerHTML = '<b>JS ERROR:</b> ' + msgStr + ' <br>Line: ' + line;
  document.body.appendChild(d);
};'''

content = re.sub(old_onerror, new_onerror, content, flags=re.MULTILINE)

# Fix second error handler
start = content.find("window.addEventListener('error', function(e) {")
if start != -1:
    end = content.find("});", start) + 3
    content = content[:start] + content[end:]

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)

print("Done")
