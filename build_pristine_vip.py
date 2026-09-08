import re

new_vip_code = """
<!-- VIP OVERLAY START -->
<style>
    .vip-pill {
        padding: 15px 30px;
        border-radius: 9999px;
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: 0.1em;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        text-align: center;
        width: 320px;
        max-width: 90vw;
        border: none;
        outline: none;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    #vip-code {
        background: rgba(255, 255, 255, 0.05);
        color: #fff;
        border: 2px solid rgba(204, 255, 0, 0.3);
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
    }
    #vip-code:focus {
        border-color: rgba(204, 255, 0, 1);
        box-shadow: inset 0 0 20px rgba(0,0,0,0.8), 0 0 15px rgba(204, 255, 0, 0.4);
    }
    #vip-submit-btn {
        background: #ccff00;
        color: #000;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(204, 255, 0, 0.3);
    }
    #vip-submit-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(204, 255, 0, 0.5);
    }
</style>
<div id="vip-overlay" style="position:fixed; top:0; left:0; width:100vw; height:100vh; background:#000; background-image: radial-gradient(ellipse at 0% 100%, rgba(204,255,0,0.36) 0%, transparent 80%), radial-gradient(ellipse at 100% 100%, rgba(204,255,0,0.18) 0%, transparent 70%); z-index:85000000; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:'Inter', sans-serif;">
    <img src="assets/img/by_sensibles.png" alt="by Sensibles" style="height:28px; filter:brightness(0) invert(1); margin-bottom:50px; opacity:0.8;">
    <h2 style="font-size:24px; font-weight:700; color:#fff; text-align:center; max-width:80%; line-height:1.4; margin-bottom:40px;">Introduce el código de acceso para vivir la cena más transformadora de tu vida</h2>
    <input type="password" id="vip-code" class="vip-pill" placeholder="Código secreto">
    <div id="vip-error" style="color:#ff3333; font-size:14px; margin-top:-10px; margin-bottom:15px; min-height:20px; font-weight:600; text-align:center; opacity:0; transition:opacity 0.3s;">Código incorrecto</div>
    <button id="vip-submit-btn" class="vip-pill" onclick="checkVipCode()">ENTRAR</button>
    <a href="#" style="color:#ccff00; font-size:14px; text-decoration:underline; margin-top:30px; opacity:0.8; font-weight:500;">¿No tienes el código?<br>Apúntate a la lista de espera</a>
</div>
<script>
    // Comprobar si ya esta desbloqueado en ESTA SESION
    if (sessionStorage.getItem('olt_vip_unlocked') === 'true') {
        document.getElementById('vip-overlay').style.display = 'none';
        document.body.style.overflow = 'auto';
    } else {
        document.body.style.overflow = 'hidden';
    }

    function checkVipCode() {
        var val = document.getElementById('vip-code').value.trim().toLowerCase();
        if (val === 'tonight' || val === 'tonight1') {
            sessionStorage.setItem('olt_vip_unlocked', 'true');
            if (window.oltTrackEvent) {
                window.oltTrackEvent('Login VIP', 'Código Correcto: ' + val);
            }
            var overlay = document.getElementById('vip-overlay');
            overlay.style.transition = 'opacity 0.8s ease';
            overlay.style.opacity = '0';
            setTimeout(function() { overlay.style.display = 'none'; }, 800);
            document.body.style.overflow = 'auto';
        } else {
            var err = document.getElementById('vip-error');
            err.innerHTML = 'Código incorrecto. ¿Seguro que estás en la lista?';
            err.style.opacity = '1';
            setTimeout(function() { err.style.opacity = '0'; }, 3000);
            if (window.oltTrackEvent) {
                window.oltTrackEvent('Login VIP', 'Intento Fallido: ' + val);
            }
        }
    }

    document.getElementById('vip-code').addEventListener('keypress', function(e) {
        if(e.key === 'Enter') checkVipCode();
    });
</script>
<!-- VIP OVERLAY END -->
"""

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# inyectar justo antes del cierre del body, o al final
if '</body>' in content:
    content = content.replace('</body>', new_vip_code + '\n</body>')
else:
    # 3d-test has </html> at the end usually
    if '</html>' in content:
        content = content.replace('</html>', new_vip_code + '\n</html>')
    else:
        content += '\n' + new_vip_code

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected pristine VIP gateway into 3d-test.html")
