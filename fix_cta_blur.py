# -*- coding: utf-8 -*-
import codecs, re

with codecs.open('3d-test.html', 'r', 'utf-8-sig') as f:
    content = f.read()

old_loop = '''              cCtx.fillStyle = '#ccff00';
              ctaParticles.forEach(p => {
                  p.y -= p.v * 0.01;
                  p.a += 0.05;
                  if (p.y < 0) p.y = 1;
                  cCtx.globalAlpha = (Math.sin(p.a) * 0.5 + 0.5) * 0.7;
                  cCtx.beginPath();
                  cCtx.arc(p.x * ctaCanvas.width, p.y * ctaCanvas.height, p.s, 0, Math.PI*2);
                  cCtx.fill();
              });'''

new_loop = '''              ctaParticles.forEach(p => {
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
              });'''

content = content.replace(old_loop, new_loop)

with codecs.open('3d-test.html', 'w', 'utf-8-sig') as f:
    f.write(content)
