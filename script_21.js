
// Ã¢â€€Ã¢â€€ SENS OVERLAY CONTROL Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
// Inyectamos un <style> en el <head> con !important.
// Las reglas de hoja de estilo con !important ganan sobre CUALQUIER inline style,
// incluyendo el backdrop-filter que Chrome composita en GPU.
(function() {
  var _ss = document.createElement('style');
  _ss.id  = '__sens_dismiss_css';
  // Empieza vacío (overlay visible por defecto)
  _ss.textContent = '';
  document.head.appendChild(_ss);
})();

window.dismissSens = function(e) {
  if (e) { e.stopPropagation(); e.preventDefault(); }

  // Ocultar botón con fade
  var btn = document.getElementById('sens-cta-btn');
  if (btn) { btn.style.opacity = '0'; btn.style.pointerEvents = 'none'; }

  // Inyectar regla CSS !important que destruye el overlay del LARGE (miniatura no se toca)
  var ss = document.getElementById('__sens_dismiss_css');
  if (ss) {
    ss.textContent = [
      '#dummy-sens-ov-large {',
      '  display: none !important;',
      '  backdrop-filter: none !important;',
      '  -webkit-backdrop-filter: none !important;',
      '  opacity: 0 !important;',
      '  pointer-events: none !important;',
      '}'
    ].join('\n');
  }

  window._sensDismissed = true;
};

// Función de reset: borra la regla CSS → overlay vuelve a sus estilos inline originales
window._resetSensOverlay = function() {
  var ss = document.getElementById('__sens_dismiss_css');
  if (ss) ss.textContent = '';
  window._sensDismissed = false;
  // Restaurar opacidad y estado del botón fixed
  var btn = document.getElementById('sens-cta-btn');
  if (btn) { btn.style.opacity = '1'; btn.style.pointerEvents = 'auto'; }
  // El loop se encargará de mostrar/ocultar el clip container según posición
};























































setTimeout(function() {
  document.querySelectorAll('video[src*="embejecimiento"]').forEach(function(v) {
    v.muted = true;
    v.preload = 'auto';
    if (v.readyState < 4) {
      var p = v.play();
      if (p) p.then(function() { v.pause(); v.currentTime = 0; }).catch(function(){});
    }
  });
}, 800);

// --- PANEL VÍDEO ENVEJECIMIENTO ---
window.envejPlayPause = function() {
  var v = document.getElementById('envej-video');
  if (!v) return;
  if (v.paused) { v.play().catch(function(){}); } else { v.pause(); }
};

// --- FINAL FELIZ ---
window._finalChoice = null; // null = sin elegir, true = feliz, false = infeliz

window.chooseFinal = function(e, happy) {
  if (e) {
    e.stopPropagation();
    e.preventDefault();
  }
  window._finalChoice = happy;
  // Cambiar imagen en todos los final-slide
  document.querySelectorAll('#final-slide').forEach(slide => {
    var imgs = slide.querySelectorAll('img');
    if (imgs[0]) imgs[0].style.opacity = '0';
    if (imgs[1]) imgs[1].style.opacity = happy ? '1' : '0';
    if (imgs[2]) imgs[2].style.opacity = happy ? '0' : '1';
  });
  // Feedback visual en los botones: activo = fondo verde; inactivo = negro con borde verde
    var panel = document.getElementById('final-feliz-panel');
  if (panel) {
    var btns = panel.querySelectorAll('button');
    if (btns[0]) { 
      if (happy) btns[0].classList.add('selected'); else btns[0].classList.remove('selected');
    }
    if (btns[1]) { 
      if (!happy) btns[1].classList.add('selected'); else btns[1].classList.remove('selected');
    }
  }
};

// --- SLIDE 1: SECUENCIA CROSSFADE (divertido → sorprendente → profundo → emocional → neutro) ---
(function() {
  var _seq0Index = 0;
  var _seq0Total = 5;
  var _seq0Words = ['¿Divertido?', '¿Sorprendente?', '¿Profundo?', '¿Emocional?', '¿Otro? Elige el que quieras'];

  function seq0Tick() {
    _seq0Index = (_seq0Index + 1) % _seq0Total;
    // Actualiza imágenes en todos los #slide0-seq del DOM (small + large track)
    var allGroups = document.querySelectorAll('#slide0-seq');
    allGroups.forEach(function(slide) {
      var imgs = slide.querySelectorAll('.seq0-img');
      imgs.forEach(function(img, i) {
        img.style.opacity = (i === _seq0Index) ? '1' : '0';
      });
    });
    // Actualiza palabra dinámica con fade (solo en large track por data-large-only)
    var wordEls = document.querySelectorAll('.seq0-word');
    wordEls.forEach(function(el) {
      el.style.opacity = '0';
      setTimeout(function() {
        el.textContent = _seq0Words[_seq0Index];
        el.style.opacity = '1';
      }, 350);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { setInterval(seq0Tick, 2000); });
  } else {
    setInterval(seq0Tick, 2000);
  }
})();

