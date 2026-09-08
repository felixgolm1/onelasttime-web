# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# Add ID to the paragraph
old_p = '''<p style="color: #fff; font-family: 'Inter', sans-serif; font-size: 1.25rem; font-weight: 700; line-height: 1.3; margin: 0; text-align: right; text-transform: uppercase;">
        SI NO LO CONSIGUES, ESTA EXPERIENCIA CORRE A NUESTRA CUENTA Y TE REGALAMOS OTRA
      </p>'''
new_p = '''<p id="glass-obj-final-text" style="color: #fff; font-family: 'Inter', sans-serif; font-size: 1.25rem; font-weight: 700; line-height: 1.3; margin: 0; text-align: right; text-transform: uppercase;">
        SI NO LO CONSIGUES, ESTA EXPERIENCIA CORRE A NUESTRA CUENTA Y TE REGALAMOS OTRA
      </p>'''
content = content.replace(old_p, new_p)

# In JS, split it
old_split = "const glassObjTitle = splitFltChars('#glass-objectives h3');"
new_split = "const glassObjTitle = splitFltChars('#glass-objectives h3');\n      const glassObjFinalText = splitFltChars('#glass-obj-final-text');"
content = content.replace(old_split, new_split)

# GSAP initial set
old_set = "gsap.set(glassObjTitle, { opacity: 0 });"
new_set = "gsap.set(glassObjTitle, { opacity: 0 });\n      gsap.set(glassObjFinalText, { opacity: 0 });"
content = content.replace(old_set, new_set)

# Step 3 animation in
# The length of "SI NO LO CONSIGUES, ESTA EXPERIENCIA CORRE A NUESTRA CUENTA Y TE REGALAMOS OTRA" is 77 chars.
# Total time should be 0.02. If duration=0.01, total stagger time=0.01.
# 0.01 / 77 = 0.00013.
# So stagger: -0.00015 is perfect.
old_anim1 = "scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.01, stagger: 0.0004, ease: 'none' }, t + 0.01);"
new_anim1 = "scrollTl.to(glassObjTitle, { opacity: 1, duration: 0.01, stagger: 0.0004, ease: 'none' }, t + 0.01);\n            scrollTl.to(glassObjFinalText, { opacity: 1, duration: 0.01, stagger: -0.00015, ease: 'none' }, t + 0.01);"
content = content.replace(old_anim1, new_anim1)

# Step 3 animation out
old_anim2 = "scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01 }, t);"
new_anim2 = "scrollTl.to(glassObjTitle, { opacity: 0, duration: 0.01 }, t);\n            scrollTl.to(glassObjFinalText, { opacity: 0, duration: 0.01 }, t);"
content = content.replace(old_anim2, new_anim2)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
