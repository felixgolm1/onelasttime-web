import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the overlay div style to add the page background color
old = 'style="display:none;position:fixed;z-index:99999;background:url(\'assets/img/ciencia_bg.png\') center/cover no-repeat;pointer-events:none;border:12px solid #f9cc10;box-shadow:inset 0 0 0 2px #fff;will-change:top,left,width,height,border-width;"'
new = 'style="display:none;position:fixed;z-index:99999;background-color:#000;background-image:radial-gradient(ellipse at 0% 100%, rgba(204,255,0,0.36) 0%, transparent 80%), radial-gradient(ellipse at 100% 100%, rgba(204,255,0,0.18) 0%, transparent 70%), url(\'assets/img/ciencia_bg.png\');background-size:auto,auto,408px 544px;background-position:0% 100%,100% 100%,center center;background-repeat:no-repeat,no-repeat,no-repeat;pointer-events:none;border:12px solid #f9cc10;box-shadow:inset 0 0 0 2px #fff;will-change:top,left,width,height;"'

if old in content:
    content = content.replace(old, new, 1)
    print('Overlay style updated OK')
else:
    print('ERROR: target string not found')
    # Find the overlay div
    idx = content.find('id="mag-breakout-overlay"')
    if idx >= 0:
        print(f'Found overlay at char {idx}')
        print(content[idx:idx+300])

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
