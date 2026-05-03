/* ═══ EDGE GLOW — perimeter-following gradient ══════════════════════════════════
     Reglas:
     1. Cada color = misma longitud de arc en el perímetro
     2. El espectro se usa UNA sola vez por vuelta (sin repetición en lados opuestos)
     3. Transiciones suaves: stop cada 50px + lerp RGB continuo
     4. Ola de brillo independiente: viaje a diferente velocidad
  ═════════════════════════════════════════════════════════════ */
  (function() {
    var cv  = document.getElementById('edge-glow');
    var ctx = cv.getContext('2d');

    /* Conversión de HSL a RGB para obtener un espectro neón matemáticamente perfecto y continuo.
       Esto garantiza que TODOS los colores ocupan el mismo ancho visual sin bandas. */
    function hslToRgb(h, s, l) {
      var r, g, b;
      if (s === 0) {
        r = g = b = l; // achromatic
      } else {
        var hue2rgb = function hue2rgb(p, q, t) {
          if (t < 0) t += 1;
          if (t > 1) t -= 1;
          if (t < 1/6) return p + (q - p) * 6 * t;
          if (t < 1/2) return q;
          if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
          return p;
        };
        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - q;
        r = hue2rgb(p, q, h + 1/3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1/3);
      }
      return [r * 255, g * 255, b * 255];
    }

    /* Devuelve color RGB para posición p ∈ [0,1) navegando el círculo cromático HSL. */
    function colorAt(p) {
      p = ((p % 1) + 1) % 1;
      // Desplazamos ligeramente (p - 0.05) para que el inicio (0) sea un rosa-rojo intenso
      return hslToRgb((p - 0.05 + 1) % 1, 1.0, 0.5);
    }

    /* Color RGB con brillo aplicado, clamped a 255 */
    function css(c, b) {
      return 'rgb(' + Math.min(255, c[0]*b|0) + ',' + Math.min(255, c[1]*b|0) + ',' + Math.min(255, c[2]*b|0) + ')';
    }

    var cPhase = 0;  /* 0..1, avanza cada frame = rotación de color */

    function draw(ts) {
      var W = window.innerWidth, H = window.innerHeight;
      if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; }
      ctx.clearRect(0, 0, W, H);

      /* Si el canvas está oculto, avanzar fase pero no dibujar */
      if (parseFloat(window.getComputedStyle(cv).opacity) < 0.01) {
        cPhase = (cPhase + 0.003) % 1;
        requestAnimationFrame(draw); return;
      }

      var R = 20, LW = 38, LW2 = 11, LW3 = 3;
      var arcL = Math.PI / 2 * R;  /* longitud de un cuarto de círculo */

      /* Segmentos en sentido horario desde esquina superior-izquierda.
         Los lados straight van por el BORDE del viewport (y=0, x=W, etc.)
         El stroke (LW=35) se extiende mitad fuera (recortada) y mitad dentro. */
      var segs = [
        {k:'h', len:W-2*R, x1:R,   y1:0,   x2:W-R, y2:0   },  /* top          */
        {k:'a', len:arcL,  cx:W-R, cy:R,   a0:-Math.PI/2, a1:0           },  /* TR           */
        {k:'v', len:H-2*R, x1:W,   y1:R,   x2:W,   y2:H-R },  /* right        */
        {k:'a', len:arcL,  cx:W-R, cy:H-R, a0:0,          a1:Math.PI/2  },  /* BR           */
        {k:'h', len:W-2*R, x1:W-R, y1:H,   x2:R,   y2:H   },  /* bottom (RTL) */
        {k:'a', len:arcL,  cx:R,   cy:H-R, a0:Math.PI/2,  a1:Math.PI    },  /* BL           */
        {k:'v', len:H-2*R, x1:0,   y1:H-R, x2:0,   y2:R   },  /* left (BTT)   */
        {k:'a', len:arcL,  cx:R,   cy:R,   a0:Math.PI,    a1:3*Math.PI/2},  /* TL           */
      ];

      var P = segs.reduce(function(s,g){return s+g.len;}, 0);

      /* sp1: foco rápido en sentido horario (1 vuelta cada 2.5s)
         sp2: foco lento en sentido antihorario (1 vuelta cada 5s)
         Gaussiana estrecha → cuando el foco pasa, el color se satura a blanco */
      var sp1 = (ts / 2500) % 1;
      var sp2 = 1 - (ts / 5000) % 1;

      /* Dibuja un pass del perímetro con el lineWidth y multiplicador dados */
      function drawPass(lw, bwMult, spotStr) {
        ctx.lineWidth = lw;
        ctx.lineCap   = 'butt';
        var cum = 0;
        segs.forEach(function(seg) {
          var f0 = cum / P, f1 = (cum + seg.len) / P;
          cum += seg.len;
          if (seg.k === 'a') {
            var N = 40, da = (seg.a1 - seg.a0) / N; // Aumentado a 40 para que las esquinas sean ultra-suaves
            for (var i = 0; i < N; i++) {
              var f  = f0 + (f1 - f0) * (i + .5) / N;
              /* ola de brillo base: ±25% */
              var bw = (0.75 + 0.25 * Math.sin((f - ts / 4000) * Math.PI * 2)) * bwMult;
              /* focos: gaussiana estrecha (sharpness=45) sobre posición del perímetro */
              var d1 = Math.abs(((f - sp1 + 1.5) % 1) - 0.5) * 2;
              var d2 = Math.abs(((f - sp2 + 1.5) % 1) - 0.5) * 2;
              var spot = (Math.exp(-d1*d1*45) + Math.exp(-d2*d2*45)) * spotStr;
              ctx.beginPath();
              ctx.arc(seg.cx, seg.cy, R, seg.a0 + da*i, seg.a0 + da*(i+1) + 0.01); // +0.01 oculta uniones
              ctx.strokeStyle = css(colorAt(f + cPhase), bw + spot);
              ctx.stroke();
            }
          } else {
            var N  = Math.ceil(seg.len / 10) + 1;  /* Paradas mucho más densas para degradado perfecto */
            var gr = seg.k === 'h'
              ? ctx.createLinearGradient(seg.x1, 0, seg.x2, 0)
              : ctx.createLinearGradient(0, seg.y1, 0, seg.y2);
            for (var i = 0; i <= N; i++) {
              var t  = i / N;
              var f  = f0 + (f1 - f0) * t;
              var bw = (0.75 + 0.25 * Math.sin((f - ts / 4000) * Math.PI * 2)) * bwMult;
              var d1 = Math.abs(((f - sp1 + 1.5) % 1) - 0.5) * 2;
              var d2 = Math.abs(((f - sp2 + 1.5) % 1) - 0.5) * 2;
              var spot = (Math.exp(-d1*d1*45) + Math.exp(-d2*d2*45)) * spotStr;
              gr.addColorStop(t, css(colorAt(f + cPhase), bw + spot));
            }
            ctx.beginPath();
            ctx.moveTo(seg.x1, seg.y1);
            ctx.lineTo(seg.x2, seg.y2);
            ctx.strokeStyle = gr;
            ctx.stroke();
          }
        });
      }

      /* Solo dibujamos el aura y el cuerpo de color. 
         ELIMINAMOS el núcleo blanco (LW3) del margen base para que los focos sean los únicos que brillen. */
      drawPass(LW,  1.2, 1.0);  /* Aura ambiental */
      drawPass(LW2, 2.8, 2.0);  /* Cuerpo de color saturado */

      /* ── Bloom Stack: Sistema de destello multi-capa aditivo (Estilo Oryzo) ──
         Dibuja 3 capas de luz sobre el mismo punto para crear volumen y deslumbramiento. */
      function drawBloom(spotPos) {
        ctx.save();
        ctx.globalCompositeOperation = 'lighter';
        ctx.lineCap = 'round';
        
        var layers = [
          { lw: LW3 * 1.5, alpha: 1.0,  sharp: 180 }, // Núcleo ciego
          { lw: LW2 * 2.5, alpha: 0.7,  sharp: 60  }, // Resplandor
          { lw: LW * 1.8,  alpha: 0.3,  sharp: 20  }, // Flare deslumbramiento
          { lw: LW * 3.0,  alpha: 0.12, sharp: 8   }  // Overglow suave (reducido para no deformar)
        ];

        layers.forEach(function(layer) {
          ctx.lineWidth = layer.lw;
          var cum = 0;
          segs.forEach(function(seg) {
            var f0 = cum / P, f1 = (cum + seg.len) / P;
            cum += seg.len;
            if (seg.k === 'a') {
              var N = 40, da = (seg.a1 - seg.a0) / N; // Más segmentos para suavizar la curva
              for (var i = 0; i < N; i++) {
                var f = f0 + (f1 - f0) * (i + 0.5) / N;
                var d = Math.abs(((f - spotPos + 1.5) % 1) - 0.5) * 2;
                var a = Math.exp(-d * d * layer.sharp);
                if (a > 0.002) {
                  ctx.beginPath();
                  ctx.arc(seg.cx, seg.cy, R, seg.a0 + da*i, seg.a0 + da*(i+1));
                  ctx.strokeStyle = 'rgba(255,255,255,' + (a * layer.alpha) + ')';
                  ctx.stroke();
                }
              }
            } else {
              var N  = Math.ceil(seg.len / 4) + 1;
              var gr = seg.k === 'h'
                ? ctx.createLinearGradient(seg.x1, 0, seg.x2, 0)
                : ctx.createLinearGradient(0, seg.y1, 0, seg.y2);
              for (var i = 0; i <= N; i++) {
                var t = i / N;
                var f = f0 + (f1 - f0) * t;
                var d = Math.abs(((f - spotPos + 1.5) % 1) - 0.5) * 2;
                var a = Math.exp(-d * d * layer.sharp);
                gr.addColorStop(t, 'rgba(255,255,255,' + (a * layer.alpha) + ')');
              }
              ctx.beginPath();
              ctx.moveTo(seg.x1, seg.y1);
              ctx.lineTo(seg.x2, seg.y2);
              ctx.strokeStyle = gr;
              ctx.stroke();
            }
          });
        });
        ctx.restore();
      }

      /* Lanzar los Bloom Stacks en el perímetro */
      drawBloom(sp1);
      drawBloom(sp2);

      /* Avanzar fase de color: 0.010/frame @ 60fps ≈ 1 revolución cada 1.7s */
      cPhase = (cPhase + 0.010) % 1;
      requestAnimationFrame(draw);
    }

    requestAnimationFrame(draw);
  })();