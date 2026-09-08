import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

target = """                  // Fade out particles before redirect
                  setTimeout(() => {
                      window._forceEmbersFadeOut = true;
                  }, 2000);"""

replacement = """                  // Fade out particles before redirect removed"""

norm_text = text.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')

print("Matches:", norm_text.count(norm_target))

new_text = norm_text.replace(norm_target, replacement)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(new_text)
