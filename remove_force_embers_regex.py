import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

pattern = re.compile(r'// Fade out particles before redirect\s*setTimeout\(\(\) => \{\s*window\._forceEmbersFadeOut = true;\s*\}, 2000\);')
new_text = pattern.sub('// Fade out particles removed', text)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(new_text)
