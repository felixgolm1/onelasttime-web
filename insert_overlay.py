import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

overlay_html = '''  <!-- MAGAZINE BREAKOUT OVERLAY — body-level para evitar problemas con transforms del carrusel -->
  <div id="mag-breakout-overlay" style="display:none;position:fixed;z-index:99999;background:url('assets/img/ciencia_bg.png') center/cover no-repeat;pointer-events:none;border:12px solid #f9cc10;box-shadow:inset 0 0 0 2px #fff;will-change:top,left,width,height,border-width;"></div>

'''

content = content.replace('</body>', overlay_html + '</body>', 1)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Overlay inserted. Total lines:', len(content.split('\n')))
