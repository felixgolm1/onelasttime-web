import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos el inicio
start_marker = "if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {"
start_idx = content.find(start_marker)

end_marker = "}, 50);"
end_idx = content.find(end_marker, start_idx) + len(end_marker)

new_logic = """if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
        var ov = document.getElementById('vip-overlay');
        if(ov) ov.style.display = 'none';
        document.body.style.overflow = 'auto';
        window._ctaHoverActive = false;
        var vipEmberInterval = null; // No lo iniciamos
    } else {
        document.body.style.overflow = 'hidden';
        var vipEmberInterval = setInterval(function() {
            window._ctaHoverActive = true;
        }, 50);
    }"""

content = content[:start_idx] + new_logic + content[end_idx:]

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Properly fixed interval logic")
