
(function() {
    const embersCanvas = document.getElementById("embers-canvas");
    const embersCtx = embersCanvas ? embersCanvas.getContext("2d") : null;
    const fakeBgFade = document.getElementById("fake-bg-fade");

    if (embersCanvas && embersCtx) {
        let width, height;
        let particles = [];
        let mouse = { x: -1000, y: -1000 };
        let explosionActive = false;

        function resizeCanvas() {
            width = window.innerWidth;
            height = window.innerHeight;
            embersCanvas.width = width;
            embersCanvas.height = height;
        }

        window.addEventListener("resize", resizeCanvas);
        resizeCanvas();

        window.addEventListener("mousemove", (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        class Particle {
            constructor() {
                this.reset();
                this.y = Math.random() * height; 
            }

            reset() {
                this.x = Math.random() * width;
                this.y = height + 10;
                this.size = Math.random() * 3 + 1;
                this.vx = (Math.random() - 0.5) * 0.8;
                this.vy = -(Math.random() * 0.6 + 0.2); 
                this.life = Math.random() * Math.PI * 2;
                this.lifeSpeed = (Math.random() * 0.015) + 0.005;
                this.swayOffset = Math.random() * Math.PI * 2;
                this.swaySpeed = Math.random() * 0.02 + 0.01;
                
                const colors = [
                    "rgba(204, 255, 0,",
                    "rgba(255, 255, 180,",
                    "rgba(180, 255, 100,"
                ];
                this.colorBase = colors[Math.floor(Math.random() * colors.length)];
                this.maxAlpha = Math.random() * 0.5 + 0.3;
            }

            update() {
                let dx = this.x - mouse.x;
                let dy = this.y - mouse.y;
                let distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 150) { 
                    // Repulsión deshabilitada para que las "luces" (bolitas) no desaparezcan al mover el ratón rápido
                    // let force = (150 - distance) / 150;
                    // this.vx += (dx / distance) * force * 0.15;
                    // this.vy += (dy / distance) * force * 0.15;
                }

                this.vx *= 0.95; 
                this.x += this.vx;
                this.y += this.vy;

                if (explosionActive) {
                    this.vy -= (Math.random() * 0.05 + 0.02); // accelerate upwards
                    this.x += Math.sin(this.life * 1.5) * 0.5; // wider sway
                    this.alpha = Math.min(1, this.alpha * 1.5); // brighter
                }

                
                this.x += Math.sin(this.life * 2 + this.swayOffset) * 0.3;
                this.y += Math.cos(this.life * 1.5) * 0.1;

                this.life += this.lifeSpeed;
                this.alpha = (Math.sin(this.life) * 0.5 + 0.5) * this.maxAlpha;

                if (this.y < -50 || this.x < -50 || this.x > width + 50) {
                    this.reset();
                }
            }

            draw(ctx) {
                let grad = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.size * 2.5);
                grad.addColorStop(0, this.colorBase + this.alpha + ")");
                grad.addColorStop(0.4, this.colorBase + (this.alpha * 0.6) + ")");
                grad.addColorStop(1, this.colorBase + "0)");

                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size * 2.5, 0, Math.PI * 2);
                ctx.fillStyle = grad;
                ctx.fill();
            }
        }

        for (let i = 0; i < 150; i++) { 
            particles.push(new Particle());
        }

        window._ctaHoverOpacity = window._ctaHoverOpacity || 0;
        window._ctaHoverActive = window._ctaHoverActive || false;
        
        function animate() {
            requestAnimationFrame(animate);
            
            let scrollOpacity = fakeBgFade ? (parseFloat(window.getComputedStyle(fakeBgFade).opacity) || 0) : 0;
            let targetCtaOpacity = window._ctaHoverActive ? 1.0 : 0.0;
            window._ctaHoverOpacity += (targetCtaOpacity - window._ctaHoverOpacity) * 0.1;
            
            let finalOpacity = Math.max(scrollOpacity, window._ctaHoverOpacity);
            if (window._forceEmbersFadeOut) {
                window._embersFadeOutMult = (window._embersFadeOutMult === undefined) ? 1.0 : window._embersFadeOutMult;
                window._embersFadeOutMult += (0.0 - window._embersFadeOutMult) * 0.05;
                finalOpacity *= window._embersFadeOutMult;
            }
            
            embersCanvas.style.transition = 'none';
            embersCanvas.style.setProperty('opacity', finalOpacity, 'important');
            // ALWAYS update particles so they are distributed naturally even when invisible
            embersCtx.clearRect(0, 0, width, height);
            
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                
                if (finalOpacity > 0.01) {
                    particles[i].draw(embersCtx);
                }
            }
        }
        animate();

        
        window.addEventListener('pageshow', (event) => {
            if (event.persisted) {
                // Force a full reload to correctly reset WebGL, GSAP, and scroll state
                window.location.reload();
            }
        });

        document.addEventListener('click', (e) => {
            const cta = e.target.closest('a[href*="arbol.html"], button[onclick*="arbol.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
            if (cta) {
                e.preventDefault();
                e.stopPropagation();
                if (explosionActive) return;
                explosionActive = true;
                window._ctaHoverActive = true; // force opacity to 1
                
                // Show overlays
                document.getElementById('premium-bg').style.opacity = '1';
                setTimeout(() => {
                    let h1 = document.getElementById('premium-h1');
                    h1.style.opacity = '1';
                    h1.style.transform = 'translateY(0)';
                }, 400); 
                
                // Multiply particles for explosion
                for (let i = 0; i < 400; i++) {
                    let p = new Particle();
                    p.y = Math.random() * height; // scatter them randomly instantly
                    particles.push(p);
                }
                
                // Fade out particles before redirect
                setTimeout(() => {
                    window._forceEmbersFadeOut = true;
                }, 2000);
                
                // Fade to white removed as per new logic
                
                // Redirect after reading time
                setTimeout(() => {
                    window.location.href = 'arbol.html?skipIntro=true';
                }, 3800);
            }
        }, true); // use capture phase


        document.addEventListener('mouseover', (e) => {
            const cta = e.target.closest('a[href*="arbol.html"], button[onclick*="arbol.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
            if (cta) window._ctaHoverActive = true;
        });
        document.addEventListener('mouseout', (e) => {
            const cta = e.target.closest('a[href*="arbol.html"], button[onclick*="arbol.html"], .hero-cta-area a, #heroCta, #olt-final-cta, .btn-blue, .btn');
            if (cta) {
                if (e.relatedTarget && cta.contains(e.relatedTarget)) return;
                window._ctaHoverActive = false;
            }
        });
    }

    

})();
