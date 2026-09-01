
(function() {
  function initMarquee(trackEl, direction) {
    // Duplicar el pill-copy para tener 2 copias identicas
    var original = trackEl.querySelector('.pill-copy');
    if (!original) return;
    var clone = original.cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    trackEl.appendChild(clone);

    var offset = 0;
    var speed = 77.4; // px/s â€â€ misma velocidad que antes
    var lastTime = null;
    var copyHeight = null;

    function getHeight() {
      return original.offsetHeight;
    }

    function step(timestamp) {
      if (!lastTime) lastTime = timestamp;
      var delta = (timestamp - lastTime) / 1000; // segundos
      lastTime = timestamp;

      if (!copyHeight) copyHeight = getHeight();

      if (direction === 'up') {
        // Columna izquierda: sube
        offset += speed * delta;
        if (offset >= copyHeight) offset -= copyHeight;
        trackEl.style.transform = 'translateY(-' + offset + 'px)';
      } else {
        // Columna derecha: baja (sentido contrario)
        offset += speed * delta;
        if (offset >= copyHeight) offset -= copyHeight;
        trackEl.style.transform = 'translateY(' + (offset - copyHeight) + 'px)';
      }

      requestAnimationFrame(step);
    }

    requestAnimationFrame(step);
  }

  window.addEventListener('load', function() {
    var up = document.getElementById('pill-col-up');
    var down = document.getElementById('pill-col-down');
    if (up) initMarquee(up, 'up');
    if (down) initMarquee(down, 'down');
  });

    
})();
