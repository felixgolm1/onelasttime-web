# -*- coding: utf-8 -*-
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

js_start = text.find('<script>') + 8
js_end = text.rfind('</script>')
script_body = text[js_start:js_end]

wrapped = """
  window.addEventListener('error', function(e) {
    var div = document.createElement('div');
    div.style = 'position:fixed;top:0;left:0;background:red;color:white;z-index:99999;font-size:20px;padding:20px';
    div.innerHTML = 'ERROR EVENT: ' + e.message;
    document.body.appendChild(div);
  });
  try {
""" + script_body + """
  } catch(e) {
    var div = document.createElement('div');
    div.style = 'position:fixed;top:0;left:0;background:red;color:white;z-index:99999;font-size:20px;padding:20px;white-space:pre-wrap';
    div.innerHTML = 'MAIN CATCH ERROR: ' + e.message + '\\n' + e.stack;
    document.body.appendChild(div);
    throw e;
  }
"""

if 'MAIN CATCH ERROR' not in text:
    text = text[:js_start] + wrapped + text[js_end:]
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Error catcher injected!')
else:
    print('Already injected')
