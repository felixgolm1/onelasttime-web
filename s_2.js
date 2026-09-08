
(function() {
    var userId = localStorage.getItem('olt_user_id');
    if (!userId) {
        userId = 'OLT-' + Math.random().toString(36).substr(2, 6).toUpperCase();
        localStorage.setItem('olt_user_id', userId);
    }
    var visitCount = parseInt(localStorage.getItem('olt_visits') || '0');
    var isNewUser = (visitCount <= 1) ? 'Sí' : 'No';
    var source = localStorage.getItem('olt_source') || 'Directo';
    
    var pageLoadTime = Date.now();
    var pageName = window.location.pathname.split('/').pop() || 'index.html';
    
    window.oltTrackEvent = function(eventName, details, extraData = {}) {
        var timeSpent = Math.round((Date.now() - pageLoadTime) / 1000);
        var scrollPerc = 0;
        if (document.body && document.documentElement) {
            var h = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
            var sh = document.documentElement.scrollHeight || document.body.scrollHeight;
            if (sh > h) scrollPerc = Math.round((window.scrollY / (sh - h)) * 100);
        }
        
        var payload = {
            sessionId: userId,
            isNewUser: isNewUser,
            visitCount: visitCount,
            trafficSource: source,
            page: pageName,
            event: eventName,
            details: details,
            scroll: scrollPerc + '%',
            timeSpent: timeSpent + 's',
            dato1: extraData.dato1 || '',
            dato2: extraData.dato2 || '',
            dato3: extraData.dato3 || '',
            dato4: extraData.dato4 || '',
            dato5: extraData.dato5 || ''
        };
        
        // Use sendBeacon for more reliable exit tracking if available
        if (navigator.sendBeacon) {
            var blob = new Blob([JSON.stringify({events: [payload]})], {type : 'application/json'});
            navigator.sendBeacon('http://localhost:8003/api/track', blob);
        } else {
            fetch('http://localhost:8003/api/track', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ events: [payload] }),
                keepalive: true
            }).catch(e => {});
        }
    };

    document.addEventListener('click', function(e) {
        var el = e.target.closest('a, button, .cta-button, .btn, .decision-card');
        if (el) {
            var text = (el.innerText || el.value || 'Botón sin texto').substring(0, 50).trim().replace(/\n/g, ' ');
            var id = el.id ? '#' + el.id : '';
            var type = 'no-menu-CTA';
            if (el.closest('nav') || el.closest('.menu') || el.closest('.navbar') || el.closest('.navigation') || el.id === 'cta-btn') {
                type = 'menu CTA';
            }
            window.oltTrackEvent('Clic en Botón', type, { dato1: text + ' ' + id });
        }
    });
    
    window.addEventListener('load', function() {
        if(pageName !== 'index.html' && pageName !== '') {
           window.oltTrackEvent('Visita Página', 'Entrada');
        }
    });
})();
