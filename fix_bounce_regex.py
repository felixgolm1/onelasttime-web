import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

pattern = re.compile(r'@keyframes bounceDown \{\s*0%, 100% \{ transform: translateY\(-10px\); \}\s*50% \{ transform: translateY\(3px\); \}\s*\}', re.DOTALL)

new_css = '''@keyframes bounceDown {
        0%, 100% { transform: translateY(-3px); }
        50% { transform: translateY(3px); }
      }'''

content = pattern.sub(new_css, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
