import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

onerror_script = '''
<script>
window.addEventListener('error', function(e) {
    var err = document.createElement('div');
    err.style.position = 'fixed';
    err.style.top = '0';
    err.style.left = '0';
    err.style.width = '100%';
    err.style.padding = '20px';
    err.style.background = 'red';
    err.style.color = 'white';
    err.style.zIndex = '999999';
    err.style.fontSize = '20px';
    err.innerHTML = 'JS ERROR: ' + e.message + ' at ' + e.filename + ':' + e.lineno;
    document.body.appendChild(err);
});
</script>
'''

if 'window.addEventListener(\'error\'' not in content:
    content = content.replace('<head>', '<head>\n' + onerror_script)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected onerror.")
