with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_line = "magazineScene.style.transform = `scale(${magScale})`;"
good_line = "magazineScene.style.transform = `translate(-50%, -50%) scale(${0.85 * magScale})`;"

if bad_line in text:
    text = text.replace(bad_line, good_line)
    with open('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed jump!")
else:
    print("Could not find bad line!")
