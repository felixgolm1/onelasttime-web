import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and update the overlay div - make background transparent, only border visible
old = 'style="display:none;position:fixed;z-index:99998;background:#000;background-image:radial-gradient(ellipse at 0% 100%, rgba(204,255,0,0.36) 0%, transparent 80%), radial-gradient(ellipse at 100% 100%, rgba(204,255,0,0.18) 0%, transparent 70%);pointer-events:none;border:12px solid #f9cc10;box-shadow:inset 0 0 0 2px #fff;will-change:top,left,width,height;"'
new  = 'style="display:none;position:fixed;z-index:99998;background:transparent;pointer-events:none;border:12px solid #f9cc10;box-shadow:inset 0 0 0 2px #fff;will-change:top,left,width,height;"'

if old in content:
    content = content.replace(old, new, 1)
    print('OK: overlay now transparent (border-only)')
else:
    print('ERROR - searching overlay...')
    idx = content.find('mag-breakout-overlay')
    print(content[idx:idx+350])

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
