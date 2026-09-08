import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

pattern = re.compile(r'<div class="mini-marquee-container"[^>]*>.*?</div>\s*</div>', re.DOTALL)
new_html = '<span style="position:relative; z-index:2; text-align:center; padding-right:20px;">TRANSFORMAR MI PR\u00d3XIMA CENA</span>'
content = pattern.sub(new_html, content)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
