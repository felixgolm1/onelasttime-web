import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the GSAP block for showing contact card
pattern_show = r'gsap\.to\(contactCard, \{\s*y:\s*"0%",\s*rotate:\s*0,\s*scale:\s*1,\s*opacity:\s*1,\s*pointerEvents:\s*"auto",\s*duration:\s*1\.2,\s*ease:\s*"expo\.out",\s*overwrite:\s*true\s*\}\);'
replacement_show = r'gsap.to(contactCard, { opacity: 1, pointerEvents: "auto", duration: 0.5, ease: "power2.out", overwrite: true });'
text = re.sub(pattern_show, replacement_show, text)

# Replace the GSAP block for hiding contact card
pattern_hide = r'gsap\.to\(contactCard, \{\s*y:\s*"115vh",\s*rotate:\s*12,\s*scale:\s*0\.8,\s*opacity:\s*0,\s*pointerEvents:\s*"none",\s*duration:\s*0\.8,\s*ease:\s*"power2\.in",\s*overwrite:\s*true\s*\}\);'
replacement_hide = r'gsap.to(contactCard, { opacity: 0, pointerEvents: "none", duration: 0.5, ease: "power2.out", overwrite: true });'
text = re.sub(pattern_hide, replacement_hide, text)

# Replace the direct style transform
pattern_transform = r"_cCardR\.style\.transform\s*=\s*'translateY\(115vh\) rotate\(12deg\) scale\(0\.8\)';"
replacement_transform = r"_cCardR.style.transform = 'none';"
text = re.sub(pattern_transform, replacement_transform, text)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed JS')
