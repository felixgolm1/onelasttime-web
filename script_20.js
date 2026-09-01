
// Ã¢â€€Ã¢â€€ ORYZO TEXT DRIFT â€â€ "NO ES MAGIA" se desplaza a esquina sup-izq durante zoom-in Ã¢â€€Ã¢â€€
(function() {
  var h2 = document.getElementById('oxitocina-title');
  if (!h2) return;

  // Rango de scroll en el que ocurre el movimiento
  var MOVE_START = 16.5;    // mismo inicio que el zoom-in del overlay (swapT)
  var MOVE_END   = 17.3;    // mismo final que el zoom-in del overlay (swapT)

  // Inicio: centrado (top:67%, left:50%, scale:1)
  // Final: derecha junto al cerebro (top:22%, left:72%, scale:0.28)
  var S_TOP = 52,  E_TOP = 27;
  var S_LEFT = 50, E_LEFT = 72;
  var S_SCL = 1.0, E_SCL = 0.28;

  // Encadenar con la función ya existente
  var prevFn = window._updateNeuralText || function(){};
  window._updateNeuralText = function(prog) {
    prevFn(prog);

    var t  = Math.max(0, Math.min(1, (prog - MOVE_START) / (MOVE_END - MOVE_START)));
    // Ease-in-out cúbico para fluidez cinematic
    var te = t < 0.5 ? 4*t*t*t : 1 - Math.pow(-2*t+2, 3)/2;

    var top  = S_TOP  + (E_TOP  - S_TOP)  * te;
    var left = S_LEFT + (E_LEFT - S_LEFT) * te;
    var scl  = S_SCL  + (E_SCL  - S_SCL)  * te;

    h2.style.top             = top  + '%';
    h2.style.left            = left + '%';
    h2.style.transition      = 'none';
    h2.style.transform       = 'translate(-50%,-50%) scale(' + scl + ')';
    h2.style.transformOrigin = 'center center';
    h2.style.textAlign       = 'center';
  };

    
})();
