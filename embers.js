
const embersCanvas = document.getElementById("embers-canvas");
const embersCtx = embersCanvas ? embersCanvas.getContext("2d") : null;
const fakeBgFade = document.getElementById("fake-bg-fade");

if (embersCanvas && embersCtx) {
    let width, height;
    let particles = [];
    let mouse = { x: -1000, y: -1000 };

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
            this.y = Math.random() * height; // initial random distribution
        }

        reset() {
            this.x = Math.random() * width;
            this.y = height + 10;
            this.size = Math.random() * 2.5 + 0.5;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = -(Math.random() * 1.5 + 0.5);
            this.life = Math.random() * 0.5 + 0.5; // for blinking/fading
            this.lifeSpeed = (Math.random() * 0.02) + 0.005;
            
            // Colores tipo brasa/fuego: dorados, naranjas
            const colors = [
                "rgba(255, 200, 50,", 
                "rgba(255, 150, 0,", 
                "rgba(255, 100, 0,"
            ];
            this.colorBase = colors[Math.floor(Math.random() * colors.length)];
        }

        update() {
            // Repulsión del ratón
            let dx = this.x - mouse.x;
            let dy = this.y - mouse.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < 150) {
                let force = (150 - distance) / 150;
                this.vx += (dx / distance) * force * 0.5;
                this.vy += (dy / distance) * force * 0.5;
            }

            // Fricción y movimiento
            this.vx *= 0.98;
            this.x += this.vx;
            this.y += this.vy;

            // Variación sutil en X (viento)
            this.x += Math.sin(this.y * 0.01) * 0.2;

            // Parpadeo
            this.life += this.lifeSpeed;
            this.alpha = (Math.sin(this.life) * 0.5 + 0.5) * 0.8;

            if (this.y < -10 || this.x < -10 || this.x > width + 10) {
                this.reset();
            }
        }

        draw(ctx) {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.colorBase + this.alpha + ")";
            ctx.fill();
        }
    }

    // Crear partículas
    for (let i = 0; i < 100; i++) {
        particles.push(new Particle());
    }

    function animate() {
        requestAnimationFrame(animate);
        
        // Solo animar si la sección final es visible
        if (fakeBgFade && parseFloat(fakeBgFade.style.opacity || 0) > 0.01) {
            embersCtx.clearRect(0, 0, width, height);
            
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw(embersCtx);
            }
        }
    }

    animate();
}

