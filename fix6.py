import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="assets/img/video elsa.mp4"', 'src="assets/img/video_elsa_kf.mp4"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Python phase 6 done")
