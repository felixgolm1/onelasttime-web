import codecs

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

# 1. Update HTML
old_html = '''        <li style="margin-bottom: 16px; display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-bullet" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mi ex (solo para valientes... o insensatxs)</div></li>
        <li style="display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-bullet" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">&iquest;Qu&eacute; m&aacute;s nos queda por ver?</div></li>
      </ul>'''

new_html = '''        <li style="display: flex;"><div style="overflow: hidden; flex-shrink: 0; width: 20px;"><div class="glass-bullet" style="color: #ccff00;">&#8226;</div></div><div class="dyn-text">Mi ex (solo para valientes... o insensatxs)</div></li>
      </ul>
      <hr style="border: none; border-top: 1px dashed rgba(255,255,255,0.25); margin: 40px 0;">
      <p id="glass-who-final-text" style="color: #fff; font-family: 'Inter', sans-serif; font-size: 1.25rem; font-weight: 700; line-height: 1.3; margin: 0; text-align: left; text-transform: uppercase;">
        &iquest;QU&Eacute; M&Aacute;S NOS QUEDA POR VER?
      </p>'''
content = content.replace(old_html, new_html)

# 2. Add glassWhoFinalText var
old_js1 = '''      const glassWhoTitle = splitFltChars('#glass-who h3');
      const glassObjTitle = splitFltChars('#glass-objectives h3');'''
new_js1 = '''      const glassWhoTitle = splitFltChars('#glass-who h3');
      const glassWhoFinalText = splitFltChars('#glass-who-final-text');
      const glassObjTitle = splitFltChars('#glass-objectives h3');'''
content = content.replace(old_js1, new_js1)

# 3. Add gsap.set opacity: 0
old_js2 = '''      gsap.set(glassWhoTitle, { opacity: 0 });
      gsap.set(glassObjTitle, { opacity: 0 });'''
new_js2 = '''      gsap.set(glassWhoTitle, { opacity: 0 });
      gsap.set(glassWhoFinalText, { opacity: 0 });
      gsap.set(glassObjTitle, { opacity: 0 });'''
content = content.replace(old_js2, new_js2)

# 4. Add animation to Step 2 (in)
old_js3 = '''            if (i === 1) {
              scrollTl.to('#glass-who', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
              scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.01, stagger: 0.00069, ease: 'none' }, t + 0.01);
              scrollTl.to('#glass-who .glass-mask-line', { yPercent: 0, duration: 0.0335, stagger: 0, ease: 'power2.out' }, t + 0.01);'''
new_js3 = '''            if (i === 1) {
              scrollTl.to('#glass-who', { autoAlpha: 1, duration: 0.01, ease: 'none' }, t);
              scrollTl.to(glassWhoTitle, { opacity: 1, duration: 0.01, stagger: 0.00069, ease: 'none' }, t + 0.01);
              scrollTl.to(glassWhoFinalText, { opacity: 1, duration: 0.01, stagger: -0.00029, ease: 'none' }, t + 0.01);
              scrollTl.to('#glass-who .glass-mask-line', { yPercent: 0, duration: 0.0335, stagger: 0, ease: 'power2.out' }, t + 0.01);'''
content = content.replace(old_js3, new_js3)

# 5. Add animation to Step 2 (out)
old_js4 = '''            } else {
              scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.0335, ease: 'none' }, t);
              scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01, stagger: -0.00069, ease: 'none' }, t);
              scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.0335, stagger: 0, ease: 'power2.out' }, t);'''
new_js4 = '''            } else {
              scrollTl.to('#glass-who', { autoAlpha: 0, duration: 0.0335, ease: 'none' }, t);
              scrollTl.to(glassWhoTitle, { opacity: 0, duration: 0.01, stagger: -0.00069, ease: 'none' }, t);
              scrollTl.to(glassWhoFinalText, { opacity: 0, duration: 0.01, stagger: 0.00029, ease: 'none' }, t);
              scrollTl.to('#glass-who .glass-mask-line', { yPercent: 110, duration: 0.0335, stagger: 0, ease: 'power2.out' }, t);'''
content = content.replace(old_js4, new_js4)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(content)

print("Done")
