
    // Efecto de lucecitas exclusivas SIEMPRE activas dentro de los CTAs
    document.addEventListener("DOMContentLoaded", () => {
      document.querySelectorAll('.btn-blue').forEach(btn => {
          btn.style.overflow = 'hidden';
          btn.style.position = 'relative';

          const ctaCanvas = document.createElement('canvas');
          ctaCanvas.style.position = 'absolute';
          ctaCanvas.style.top = '0';
          ctaCanvas.style.left = '0';
          ctaCanvas.style.width = '100%';
          ctaCanvas.style.height = '100%';
          ctaCanvas.style.pointerEvents = 'none';
          ctaCanvas.style.zIndex = '0'; // Detras del texto
          ctaCanvas.style.opacity = '1';
          btn.appendChild(ctaCanvas);
          
          const cCtx = ctaCanvas.getContext('2d');
          
          let ctaParticles = [];
          for(let i=0; i<40; i++){
            ctaParticles.push({
              x: Math.random(),
              y: Math.random(),
              s: Math.random() * 3 + 1,
              a: Math.random() * Math.PI * 2,
              v: (Math.random() * 0.5 + 0.2)
            });
          }
          
          function drawCtaParticles() {
              ctaCanvas.width = btn.offsetWidth;
              ctaCanvas.height = btn.offsetHeight;
              cCtx.clearRect(0,0, ctaCanvas.width, ctaCanvas.height);
              ctaParticles.forEach(p => {
                  p.y -= p.v * 0.01;
                  p.a += 0.05;
                  if (p.y < 0) p.y = 1;
                  
                  let px = p.x * ctaCanvas.width;
                  let py = p.y * ctaCanvas.height;
                  let radius = p.s * 2.5;
                  let alpha = (Math.sin(p.a) * 0.5 + 0.5) * 0.7;
                  
                  let grad = cCtx.createRadialGradient(px, py, 0, px, py, radius);
                  grad.addColorStop(0, "rgba(204, 255, 0, " + alpha + ")");
                  grad.addColorStop(0.4, "rgba(204, 255, 0, " + (alpha * 0.6) + ")");
                  grad.addColorStop(1, "rgba(204, 255, 0, 0)");
                  
                  cCtx.globalAlpha = 1; // Alpha is handled by the gradient
                  cCtx.beginPath();
                  cCtx.arc(px, py, radius, 0, Math.PI*2);
                  cCtx.fillStyle = grad;
                  cCtx.fill();
              });
              requestAnimationFrame(drawCtaParticles);
          }
          drawCtaParticles();
      });
    });
  