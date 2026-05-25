import sys
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Inject an onscreen error logger
error_logger = """
<script>
window.addEventListener('error', function(e) {
    let errDiv = document.getElementById('debug-error-log');
    if (!errDiv) {
        errDiv = document.createElement('div');
        errDiv.id = 'debug-error-log';
        errDiv.style.cssText = 'position:fixed; top:10px; right:10px; background:red; color:white; z-index:9999999; padding:20px; font-size:16px; font-family:monospace; max-width:400px; white-space:pre-wrap;';
        document.body.appendChild(errDiv);
    }
    errDiv.innerHTML += e.message + ' at ' + e.filename + ':' + e.lineno + '<br>';
});
</script>
"""

script_start = text.find('<script>')
if script_start > 0:
    text = text[:script_start] + error_logger + text[script_start:]

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Error logger injected.")
