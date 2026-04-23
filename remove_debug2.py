import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<div id=\"DEBUG_PANEL\".*?</div>', '', text, flags=re.DOTALL)
text = re.sub(r'<script>\s*window\.addEventListener\(\'error\'.*?</script>\n?', '', text, flags=re.DOTALL)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('DEBUG_PANEL removed')
