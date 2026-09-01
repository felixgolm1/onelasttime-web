
// Ã¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•Â
//  MAPA DE CALOR 2D ANIMADO â€â€ zonas respiran, cerebro parece vivo
// Ã¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•ÂÃ¢•Â
(function initHeatMap() {
  var wrap = document.getElementById('brain-2d-wrap');
  var hc   = document.getElementById('brain-2d-heat');
  if (!wrap || !hc) return;

  // Ã¢â€€Ã¢â€€ ZONAS: cx/cy posición, rx/ry radio, heat base, phase y speed para animación Ã¢â€€Ã¢â€€
  var ZONES = [
    // 1. VTA â€â€ Área tegmental ventral (más caliente, pulso más rápido)
    { id:'VTA',  cx:0.52, cy:0.72, rx:0.08, ry:0.06, heat:1.00, phase:0.0,  speed:0.9  },
    // 2. ACC â€â€ Corteza cingulada anterior
    { id:'ACC',  cx:0.38, cy:0.30, rx:0.18, ry:0.09, heat:0.97, phase:1.1,  speed:0.7  },
    // 3. Ínsula posterior
    { id:'INS',  cx:0.62, cy:0.45, rx:0.13, ry:0.10, heat:0.94, phase:2.3,  speed:0.75 },
    // 4. Núcleo caudado
    { id:'CAU',  cx:0.45, cy:0.40, rx:0.16, ry:0.10, heat:0.90, phase:3.5,  speed:0.65 }
  ];

  // Ã¢â€€Ã¢â€€ Paleta Oryzo Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€Ã¢â€€
  function oryzoRGB(heat) {
    heat = Math.max(0, Math.min(1, heat));
    var stops = [
      [0.00, [20,  0, 60]],
      [0.20, [100, 0,120]],
      [0.40, [200,10, 80]],
      [0.58, [220,40,  0]],
      [0.75, [255,120, 0]],
      [0.88, [255,200,20]],
      [1.00, [255,240,80]]
    ];
    for (var i = 0; i < stops.length-1; i++) {
      var t0=stops[i][0], t1=stops[i+1][0];
      if (heat >= t0 && heat <= t1) {
        var f=(heat-t0)/(t1-t0), c0=stops[i][1], c1=stops[i+1][1];
        return [Math.round(c0[0]+f*(c1[0]-c0[0])),
                Math.round(c0[1]+f*(c1[1]-c0[1])),
                Math.round(c0[2]+f*(c1[2]-c0[2]))];
      }
    }
    return stops[stops.length-1][1];
  }

  var _swapT = 0;
  var _running = false;
  var _t0 = performance.now();

  function drawFrame() {
    if (_swapT <= 0) { _running = false; return; }
    requestAnimationFrame(drawFrame);

    var W = hc.offsetWidth, H = hc.offsetHeight;
    if (!W || !H) return;
    if (hc.width !== W || hc.height !== H) { hc.width = W; hc.height = H; }

    var ctx = hc.getContext('2d');
    ctx.clearRect(0, 0, W, H);
    var t = (performance.now() - _t0) / 1000; // segundos

    ZONES.forEach(function(z) {
      // Pulso de calor: oscila Â±0.05 alrededor del valor base
      var pulse = Math.sin(t * z.speed * Math.PI * 2 + z.phase) * 0.05;
      var h = z.heat + pulse;

      // Micro-drift orgánico del centro (Â±1.5% del tamaño)
      var drift = 0.015;
      var dx = Math.sin(t * z.speed * 0.7 + z.phase * 1.3) * drift;
      var dy = Math.cos(t * z.speed * 0.5 + z.phase * 0.9) * drift;
      var cx = (z.cx + dx) * W;
      var cy = (z.cy + dy) * H;
      var rx = z.rx * W;
      var ry = z.ry * H;

      var col    = oryzoRGB(h);
      var colMid = oryzoRGB(h - 0.12);
      var colEdge= oryzoRGB(h - 0.28);

      ctx.save();
      ctx.scale(1, ry/rx);
      var yS = cy * (rx/ry);
      var gr = ctx.createRadialGradient(cx, yS, 0, cx, yS, rx);
      gr.addColorStop(0.00,'rgba('+col[0]+','+col[1]+','+col[2]+',0.78)');
      gr.addColorStop(0.40,'rgba('+colMid[0]+','+colMid[1]+','+colMid[2]+',0.50)');
      gr.addColorStop(0.75,'rgba('+colEdge[0]+','+colEdge[1]+','+colEdge[2]+',0.18)');
      gr.addColorStop(1.00,'rgba(0,0,0,0)');
      ctx.fillStyle = gr;
      ctx.fillRect(cx-rx, yS-rx, rx*2, rx*2);
      ctx.restore();
    });
  }

  window._drawHeatMap = function(swapT) {
    _swapT = swapT;
    wrap.style.opacity = swapT.toFixed(3);
    if (swapT > 0 && !_running) {
      _running = true;
      _t0 = performance.now();
      requestAnimationFrame(drawFrame);
    }
  };

  window.HEAT_ZONES = ZONES;

    
})();
