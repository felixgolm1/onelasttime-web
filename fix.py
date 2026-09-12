import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern1 = re.compile(r'(\.box-3d-wrapper\s*\{\s*[^}]*?top:\s*)50%;')
html = pattern1.sub(r'\g<1>calc(50% - 4.5vh);', html)

pattern2 = re.compile(r'(\.sc-board\s*\{\s*position:\s*absolute;\s*top:\s*)50%;')
html = pattern2.sub(r'\g<1>calc(50% - 4.5vh);', html)

html = html.replace('id="made-by-humans" style="position: fixed; top: 50%;', 'id="made-by-humans" style="position: fixed; top: calc(50% - 4.5vh);')
html = html.replace('id="made-by-ai" style="position: fixed; top: 50%;', 'id="made-by-ai" style="position: fixed; top: calc(50% - 4.5vh);')

html = html.replace("(window._cIsMobile ? 'top:45%' : 'top:50%')", "(window._cIsMobile ? 'top:45%' : 'top:calc(50% - 4.5vh)')")

html = html.replace('id="visible-input-overlay" style="display: none !important; position: fixed; inset: 0; pointer-events: none; z-index: 10050; align-items: center; justify-content: center;"', 'id="visible-input-overlay" style="display: none !important; position: fixed; inset: 0; pointer-events: none; z-index: 10050; padding-bottom: 9vh; align-items: center; justify-content: center;"')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
