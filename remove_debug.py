import re
with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the debug element
text = re.sub(r'<div id="DEBUG_PANEL".*?</div>', '', text, flags=re.DOTALL)

# Remove the debug script entirely up to the next <script>
text = re.sub(r'<script>\s*window\.addEventListener\(\'error\', e => \{\s*document\.getElementById\(\'DEBUG_PANEL\'.*?</script>\n?\s*<script', '<script', text, flags=re.DOTALL)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Removed debug panel')
