import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = '<button id="vip-submit-btn" onclick="checkVipCode()" class="vip-pill vip-btn">Entrar</button>'
replacement = '''<button id="vip-submit-btn" onclick="checkVipCode()" class="vip-pill vip-btn" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
            Entrar
            <svg style="width: 20px; height: 20px; margin-top: -1px;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </button>'''

if search in content:
    content = content.replace(search, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added arrow to CTA in index.html")
else:
    print("Could not find button in index.html")
