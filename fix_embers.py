import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos el inicio del script que inyectamos antes
search_target = """if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
        var ov = document.getElementById('vip-overlay');
        if(ov) ov.style.display = 'none';
        document.body.style.overflow = 'auto';
    } else {"""

replacement = """if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
        var ov = document.getElementById('vip-overlay');
        if(ov) ov.style.display = 'none';
        document.body.style.overflow = 'auto';
        if (typeof vipEmberInterval !== 'undefined') clearInterval(vipEmberInterval);
        window._ctaHoverActive = false;
    } else {"""

if search_target in content:
    content = content.replace(search_target, replacement)
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed embers interval on bypass")
else:
    print("Could not find the bypass logic to fix")
