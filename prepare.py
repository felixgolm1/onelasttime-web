import os
import re

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. REMOVE OLD HTML
old_html_regex = re.compile(r'<div id="headline" class="review-text-col">.*?</script>\s*</div>', re.DOTALL)
# Wait, look closely at the file structure. I'll just replace the exact chunks.
