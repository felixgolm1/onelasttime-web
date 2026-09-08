import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_css = '''      @keyframes bounceDown {
        0%, 100% { transform: translateY(-10px); }
        50% { transform: translateY(3px); }
      }'''

new_css = '''      @keyframes bounceDown {
        0%, 100% { transform: translateY(-3px); }
        50% { transform: translateY(3px); }
      }'''

content = content.replace(old_css, new_css)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
