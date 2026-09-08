
    if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
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
    }

var vipMode = 'code';

function toggleVipMode(e) {
    if(e) e.preventDefault();
    vipMode = (vipMode === 'code') ? 'waitlist' : 'code';
    var title = document.getElementById('vip-title');
    var input = document.getElementById('vip-code');
    var btn = document.getElementById('vip-submit-btn');
    var toggle = document.getElementById('vip-toggle-mode');
    var prefix = document.getElementById('vip-toggle-prefix');
    var err = document.getElementById('vip-error');
    
    // Animacion sutil
    document.getElementById('vip-form-container').style.animation = 'none';
    document.getElementById('vip-form-container').style.opacity = '0';
    
    setTimeout(function() {
        err.style.visibility = 'hidden';
        btn.style.display = 'block';
        
        if(vipMode === 'waitlist') {
            title.innerHTML = 'D&eacute;janos tu email y te avisaremos cuando abramos m&aacute;s plazas';
            input.placeholder = 'tu@email.com';
            input.value = '';
            input.type = 'email';
            btn.innerHTML = 'APUNTARME';
            toggle.innerHTML = 'Ya tengo el c&oacute;digo';
            prefix.innerHTML = '';
        } else {
            title.innerHTML = 'Introduce el c&oacute;digo de acceso para vivir la cena m&aacute;s transformadora de tu vida';
            input.placeholder = 'Código secreto';
            input.value = '';
            input.type = 'text';
            btn.innerHTML = 'Entrar';
            toggle.innerHTML = 'Ap&uacute;ntate a la lista de espera';
            prefix.innerHTML = '&iquest;No tienes el c&oacute;digo? ';
        }
        document.getElementById('vip-form-container').style.opacity = '1';
    }, 500);
}

function showVipError(msg, isSuccess) {
    var err = document.getElementById('vip-error');
    var input = document.getElementById('vip-code');
    
    err.innerHTML = msg;
    err.style.color = isSuccess ? '#ccff00' : '#ff4444';
    err.style.visibility = 'visible';
    
    // Fade IN
    err.style.opacity = '0';
    err.style.transition = 'opacity 0.3s ease';
    void err.offsetWidth; // force reflow
    err.style.opacity = '1';
    
    if (!isSuccess) {
        input.style.borderColor = '#ff4444';
        err.classList.remove('vip-shake');
        input.classList.remove('vip-shake');
        void err.offsetWidth; // trigger reflow
        err.classList.add('vip-shake');
        input.classList.add('vip-shake');
    }
    
    if(window._vipErrTimeout) clearTimeout(window._vipErrTimeout);
    
    // Fade OUT after 3s (only for errors, success stays)
    if (!isSuccess) {
        window._vipErrTimeout = setTimeout(function() {
            err.style.opacity = '0';
            input.style.borderColor = '#ccff00';
            setTimeout(function() { err.style.visibility = 'hidden'; }, 300);
        }, 3000);
    }
}

function checkVipCode() {
    var val = document.getElementById('vip-code').value.trim().toUpperCase();
    
    if (vipMode === 'waitlist') {
        if(val.includes('@') && val.includes('.')) {
            showVipError('&iexcl;Genial! Est&aacute;s en la lista. Te avisaremos pronto.', true);
            document.getElementById('vip-submit-btn').style.display = 'none';
            
            // Enviar al backend de Python -> Google Sheets
            fetch('http://localhost:8003/api/waitlist', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: val })
            }).catch(e => console.log('Error enviando a lista de espera', e));
        } else {
            showVipError('Introduce un email v&aacute;lido', false);
        }
        return;
    }

    var validCodes = ['PASS007'];
    if(validCodes.includes(val)) {
        // Enviar chivatazo a Google Analytics 4
        if (typeof gtag === 'function') {
            gtag('event', 'pass_code', {
                'codigo_usado': val
            });
        }
        // Identificar la sesion en Clarity con el codigo usado
        if (typeof clarity === 'function') {
            clarity("set", "VIP_Code", val);
        }
        
        // Generar User ID unico y guardarlo
        var userId = sessionStorage.getItem('olt_user_id');
        if(!userId) {
            userId = 'OLT-' + Math.random().toString(36).substr(2, 6).toUpperCase();
            sessionStorage.setItem('olt_user_id', userId);
        }
        sessionStorage.setItem('olt_vip_code', val);
        
        // Gestionar visitas y nuevo usuario
        var visitCount = parseInt(sessionStorage.getItem('olt_visits') || '0');
        var isNewUser = "No";
        if (!sessionStorage.getItem('olt_session_active')) {
            visitCount++;
            sessionStorage.setItem('olt_visits', visitCount);
            sessionStorage.setItem('olt_session_active', 'true');
        }
        if (visitCount === 1) isNewUser = "Sí";
        
        // Procedencia (UTM parameters)
        var urlParams = new URLSearchParams(window.location.search);
        var source = urlParams.get('utm_source') || sessionStorage.getItem('olt_source') || 'Directo';
        if (urlParams.get('utm_source')) {
            sessionStorage.setItem('olt_source', source);
        }
        
        // Enviar evento de entrada a backend
        fetch('http://localhost:8003/api/track', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                events: [{
                    sessionId: userId,
                    isNewUser: isNewUser,
                    visitCount: visitCount,
                    trafficSource: source,
                    event: 'Login VIP',
                    details: 'Código: ' + val,
                    page: 'index.html',
                    scroll: 0,
                    timeSpent: 0
                }]
            })
        }).catch(e => console.log(e));

        
        var overlay = document.getElementById('vip-overlay');
        sessionStorage.setItem('olt_vip_unlocked', 'true');
        document.body.style.overflow = 'auto';
        
        // Efecto de intensificar luces
        if (window.triggerEmberExplosion) window.triggerEmberExplosion();
        
        setTimeout(function() {
            overlay.style.transition = 'opacity 1.2s ease';
            overlay.style.opacity = '0';
            setTimeout(function() { 
                overlay.style.display = 'none'; 
                // Secuencia de carga de la landing page (letras, etc)
                if (typeof window._runIntroAnim === 'function') {
                    window._runIntroAnim();
                    window._runIntroAnim = null;
                }
            }, 1200);
            if (typeof vipEmberInterval !== 'undefined' && vipEmberInterval) clearInterval(vipEmberInterval);
            window._ctaHoverActive = false;
        }, 800);
    } else {
        showVipError('C&oacute;digo incorrecto', false);
    }
}

document.getElementById('vip-code').addEventListener('keypress', function(e) {
    if(e.key === 'Enter') {
        var btn = document.getElementById('vip-submit-btn');
        if(btn.style.display !== 'none') {
            btn.animate([
                { transform: 'scale(0.95) translateY(2px)', filter: 'brightness(0.8)' },
                { transform: 'scale(1) translateY(0)', filter: 'brightness(1)' }
            ], { duration: 150, easing: 'ease-out' });
        }
        setTimeout(checkVipCode, 50); // slight delay to feel the click
    }
});
