import re

files = [
    'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/index.html',
    'c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html'
]

bolitas_full = '''
<!-- EFECTO BOLITAS HOVER CTAs -->
<canvas id="cta-sparks-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:999999; opacity: 1 !important;"></canvas>
<script>
(function() {
    const canvas = document.getElementById('cta-sparks-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let width = window.innerWidth;
    let height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
    
    window.addEventListener('resize', () => {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
    });

    let particles = [];
    
    class CtaParticle {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.size = Math.random() * 2.5 + 1;
            this.vx = (Math.random() - 0.5) * 1.0;
            this.vy = -(Math.random() * 1.5 + 0.5); 
            this.life = 1.0; 
            this.lifeSpeed = Math.random() * 0.02 + 0.01;
            this.swayOffset = Math.random() * Math.PI * 2;
            
            const colors = [
                "rgba(204, 255, 0,",
                "rgba(255, 255, 180,",
                "rgba(180, 255, 100,"
            ];
            this.colorBase = colors[Math.floor(Math.random() * colors.length)];
        }
        
        update() {
            this.x += this.vx + Math.sin(this.life * 10 + this.swayOffset) * 0.5;
            this.y += this.vy;
            this.life -= this.lifeSpeed;
        }
        
        draw(ctx) {
            if (this.life <= 0) return;
            let alpha = this.life < 0.2 ? (this.life / 0.2) : (this.life > 0.8 ? (1.0 - this.life)/0.2 : 1.0);
            alpha *= 0.8; 
            
            let grad = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.size * 2.5);
            grad.addColorStop(0, this.colorBase + alpha + ")");
            grad.addColorStop(0.4, this.colorBase + (alpha * 0.6) + ")");
            grad.addColorStop(1, this.colorBase + "0)");

            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size * 2.5, 0, Math.PI * 2);
            ctx.fillStyle = grad;
            ctx.fill();
        }
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, width, height);
        
        for (let i = particles.length - 1; i >= 0; i--) {
            particles[i].update();
            particles[i].draw(ctx);
            if (particles[i].life <= 0) {
                particles.splice(i, 1);
            }
        }
    }
    animate();

    let spawnInterval = null;
    let hoveredRect = null;
    
    function updateRect(cta) {
        hoveredRect = cta.getBoundingClientRect();
    }

    document.addEventListener('mouseover', (e) => {
        const cta = e.target.closest('a[href*="arbol.html"], button[onclick*="arbol.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
        if (cta) {
            updateRect(cta);
            if (!spawnInterval) {
                spawnInterval = setInterval(() => {
                    updateRect(cta);
                    for(let i=0; i<4; i++) {
                        const x = hoveredRect.left + Math.random() * hoveredRect.width;
                        const y = hoveredRect.top + Math.random() * hoveredRect.height;
                        particles.push(new CtaParticle(x, y));
                    }
                }, 30);
            }
        }
    });

    document.addEventListener('mouseout', (e) => {
        const cta = e.target.closest('a[href*="arbol.html"], button[onclick*="arbol.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
        if (cta) {
            if (e.relatedTarget && cta.contains(e.relatedTarget)) return;
            clearInterval(spawnInterval);
            spawnInterval = null;
        }
    });
})();
</script>
'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    # Remove the current bolitas block completely
    txt = re.sub(r'<!-- EFECTO BOLITAS HOVER CTAs -->.*?</script>', '', txt, flags=re.DOTALL)
    
    # Re-inject the pristine one with opacity: 1 !important
    txt = txt.replace('</body>', bolitas_full + '\\n</body>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(txt)

print("Fixed opacity inheritance and cleaned debug dots!")
