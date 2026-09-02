# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the checkVipCode function block
old_func_pattern = re.compile(r'function checkVipCode\(\) \{.*?(?=document\.getElementById\(\'vip-code\'\)\.addEventListener)', re.DOTALL)

new_func = '''function showVipError(msg, isSuccess) {
    var err = document.getElementById('vip-error');
    var input = document.getElementById('vip-code');
    
    err.innerHTML = msg;
    err.style.color = isSuccess ? '#ccff00' : '#ff4444';
    err.style.display = 'block';
    
    // Fade IN
    err.style.opacity = '0';
    err.style.transition = 'opacity 0.3s ease';
    void err.offsetWidth; // force reflow
    err.style.opacity = '1';
    
    if (!isSuccess) {
        var shakeKeys = [
            { transform: 'translateX(-8px)' },
            { transform: 'translateX(8px)' },
            { transform: 'translateX(-8px)' },
            { transform: 'translateX(8px)' },
            { transform: 'translateX(0)' }
        ];
        err.animate(shakeKeys, { duration: 400 });
        input.animate(shakeKeys, { duration: 400, composite: 'add' });
    }
    
    if(window._vipErrTimeout) clearTimeout(window._vipErrTimeout);
    
    // Fade OUT after 3s (only for errors, success stays)
    if (!isSuccess) {
        window._vipErrTimeout = setTimeout(function() {
            err.style.opacity = '0';
            setTimeout(function() { err.style.display = 'none'; }, 300);
        }, 3000);
    }
}

function checkVipCode() {
    var val = document.getElementById('vip-code').value.trim().toUpperCase();
    
    if (vipMode === 'waitlist') {
        if(val.includes('@') && val.includes('.')) {
            showVipError('&iexcl;Genial! Est&aacute;s en la lista. Te avisaremos pronto.', true);
            document.getElementById('vip-submit-btn').style.display = 'none';
        } else {
            showVipError('Por favor, introduce un email v&aacute;lido.', false);
        }
        return;
    }

    var validCodes = ['PIONEROS', 'SENS-VIP', 'INFILTRADO', 'COCREADOR', 'ORIGEN', 'ZERO', '1234'];
    if(validCodes.includes(val)) {
        var overlay = document.getElementById('vip-overlay');
        overlay.style.transition = 'opacity 0.8s ease';
        overlay.style.opacity = '0';
        setTimeout(function() { overlay.style.display = 'none'; }, 800);
        clearInterval(vipEmberInterval);
        window._ctaHoverActive = false;
    } else {
        showVipError('C&oacute;digo incorrecto. &iquest;Seguro que est&aacute;s en la lista?', false);
    }
}

'''

content = old_func_pattern.sub(new_func, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated checkVipCode with new animations")
