
console.log("Embers script initializing...");
const embersCanvas = document.getElementById("embers-canvas");
const embersCtx = embersCanvas ? embersCanvas.getContext("2d") : null;
const fakeBgFade = document.getElementById("fake-bg-fade");
console.log("Canvas:", embersCanvas, "Context:", embersCtx);

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
            this.y = Math.random() * height; 
        }

        reset() {
            this.x = Math.random() * width;
            this.y = height + 10;
            this.size = Math.random() * 4 + 1.5; // Made them bigger!
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = -(Math.random() * 2 + 1); // Made them faster!
            this.life = Math.random() * 0.5 + 0.5;
            this.lifeSpeed = (Math.random() * 0.02) + 0.01;
            
            const colors = [
                "rgba(255, 200, 50,", 
                "rgba(255, 150, 0,", 
                "rgba(255, 100, 0,"
            ];
            this.colorBase = colors[Math.floor(Math.random() * colors.length)];
        }

        update() {
            let dx = this.x - mouse.x;
            let dy = this.y - mouse.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < 250) { // increased radius
                let force = (250 - distance) / 250;
                this.vx += (dx / distance) * force * 1.5;
                this.vy += (dy / distance) * force * 1.5;
            }

            this.vx *= 0.96;
            this.x += this.vx;
            this.y += this.vy;
            this.x += Math.sin(this.y * 0.01) * 0.4;

            this.life += this.lifeSpeed;
            this.alpha = (Math.sin(this.life) * 0.5 + 0.5);

            if (this.y < -50 || this.x < -50 || this.x > width + 50) {
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

    for (let i = 0; i < 150; i++) { // increased count
        particles.push(new Particle());
    }

    let started = false;
    function animate() {
        requestAnimationFrame(animate);
        
        // Use getComputedStyle to ensure we get the real opacity, even if modified via JS on another ref
        let opacity = parseFloat(window.getComputedStyle(fakeBgFade).opacity);
        
        if (opacity > 0.01) {
            if (!started) { console.log("Embers animation started!"); started = true; }
            embersCtx.clearRect(0, 0, width, height);
            
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw(embersCtx);
            }
        }
    }

    animate();
}

