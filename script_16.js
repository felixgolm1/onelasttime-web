
// Listener global para el botón de contenido sensible (capture phase para evitar bloqueos)
window.addEventListener('click', function(e) {
  var btn = e.target.closest ? e.target.closest('.sensitive-reveal-btn') : null;
  if (!btn) return;
  e.stopPropagation();
  var overlay = btn.parentElement;
  if (overlay) {
    overlay.style.opacity = '0';
    overlay.style.pointerEvents = 'none';
  }
}, true);
