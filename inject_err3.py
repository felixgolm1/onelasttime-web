import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

error_catcher = '''
<div id="error-log" style="position:fixed;top:0;left:0;width:100%;height:100%;background:red;color:white;z-index:999999;font-size:24px;padding:50px;display:none;word-wrap:break-word;"></div>
<script>
window.addEventListener('error', function(e) {
  const log = document.getElementById('error-log');
  log.style.display = 'block';
  log.innerHTML += 'Error: ' + e.message + '<br>Line: ' + e.lineno + '<br>Col: ' + e.colno + '<br><br>';
});
window.addEventListener('unhandledrejection', function(e) {
  const log = document.getElementById('error-log');
  log.style.display = 'block';
  log.innerHTML += 'Promise Error: ' + e.reason + '<br><br>';
});
</script>
'''

content = content.replace('</head>', error_catcher + '\n</head>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected safe error catcher")
