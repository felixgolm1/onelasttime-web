from bs4 import BeautifulSoup
import sys

with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')
with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/extracted_scripts.js', 'w', encoding='utf-8') as f:
    for i, s in enumerate(scripts):
        if s.string:
            f.write(f"\n/* --- SCRIPT {i} --- */\n")
            f.write(s.string)
