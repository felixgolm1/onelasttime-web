
        // Insertar el clon prístino guardado al inicio del body
        document.addEventListener('DOMContentLoaded', function() {
          var cont = document.getElementById('oryzo-deck-container');
          if(window._pristineMainDeckClone && cont) {
             var clone = window._pristineMainDeckClone;
             clone.id = 'oryzo-deck-clone';
             clone.style.display = 'block';
             clone.style.opacity = '1';
             clone.style.position = 'relative';
             clone.style.top = 'auto';
             clone.style.left = 'auto';
             clone.style.margin = '0';
             // Forzar orientacion correcta antes de que el loop empiece
             var vol = clone.querySelector('.box-3d-volume');
             if (vol) {
               vol.style.transition = 'none';
               vol.style.transform = 'rotateX(-15deg) rotateY(-25deg) rotateZ(0deg)';
             }
             cont.appendChild(clone);
          }
        });
      