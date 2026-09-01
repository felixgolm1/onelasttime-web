# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<div id="vip-overlay".*?</script>', re.DOTALL)

new_overlay = '''<style>
    @keyframes vipFloatA { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-6px); } }
    @keyframes vipFloatB { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-4px); } }
    
    .vip-pill {
        padding: 15px 30px;
        border-radius: 9999px;
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.4s, color 0.4s;
        text-align: center;
        width: 300px;
        outline: none;
    }
    .vip-input {
        border: 2px solid #ccff00;
        background: #111;
        color: #ccff00;
        margin-bottom: 20px;
        animation: vipFloatA 6s ease-in-out infinite;
        box-shadow: 0 4px 15px rgba(204,255,0,0.1);
    }
    .vip-input:focus {
        animation: none;
        box-shadow: 0 8px 25px rgba(204,255,0,0.25);
        background: #1a1a1a;
        transform: translateY(-4px);
    }
    .vip-btn {
        background: #ccff00;
        color: #000;
        border: none;
        cursor: pointer;
        animation: vipFloatB 5s ease-in-out infinite 1s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08), 0 8px 20px rgba(0,0,0,0.12);
    }
    .vip-btn:hover {
        animation: none;
        box-shadow: 0 16px 32px rgba(0,0,0,0.2);
        background: #d4ff33;
        transform: translateY(-8px);
    }
    .vip-btn:active {
        animation: none;
        transform: translateY(-2px) scale(0.96);
    }
</style>
<div id="vip-overlay" style="position:fixed; top:0; left:0; width:100vw; height:100vh; background:#000; background-image: radial-gradient(ellipse at 0% 100%, rgba(204,255,0,0.36) 0%, transparent 80%), radial-gradient(ellipse at 100% 100%, rgba(204,255,0,0.18) 0%, transparent 70%); z-index:999999999; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:'Inter', sans-serif;">
    <div style="display: flex; flex-direction: column; align-items: center; gap: 8px; margin-bottom:40px;">
        <img src="assets/img/logo%20one%20last%20time.png" alt="One Last Time" style="width: 100%; max-width: 450px; height: auto; filter: brightness(0) invert(1);">
        <img src="assets/img/by_sensibles.png" alt="by Sensibles" style="width: 45%; max-width: 180px; height: auto; filter: brightness(0) invert(1);">
    </div>
    <h2 style="color:#fff; margin-bottom:30px; font-weight:600; text-align:center; padding: 0 20px; letter-spacing:-0.02em;">Introduce el c&oacute;digo de acceso</h2>
    <input type="text" id="vip-code" class="vip-pill vip-input" placeholder="C&Oacute;DIGO SECRETO">
    <button onclick="checkVipCode()" class="vip-pill vip-btn">Entrar</button>
    <p id="vip-error" style="color:#ff4444; margin-top:20px; font-size:15px; display:none; font-weight:500;">C&oacute;digo incorrecto. &iquest;Seguro que est&aacute;s en la lista?</p>
</div>
<script>
function checkVipCode() {
    var code = document.getElementById('vip-code').value.trim().toUpperCase();
    var validCodes = ['PIONEROS', 'SENS-VIP', 'INFILTRADO', 'COCREADOR', 'ORIGEN', 'ZERO', '1234'];
    if(validCodes.includes(code)) {
        var overlay = document.getElementById('vip-overlay');
        overlay.style.transition = 'opacity 0.8s ease';
        overlay.style.opacity = '0';
        setTimeout(function() { overlay.style.display = 'none'; }, 800);
    } else {
        var err = document.getElementById('vip-error');
        err.style.display = 'block';
        err.animate([ { transform: 'translateX(-5px)' }, { transform: 'translateX(5px)' }, { transform: 'translateX(-5px)' }, { transform: 'translateX(5px)' }, { transform: 'translateX(0)' } ], { duration: 400 });
    }
}
document.getElementById('vip-code').addEventListener('keypress', function(e) {
    if(e.key === 'Enter') checkVipCode();
});
</script>'''

content = pattern.sub(new_overlay, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed neon shadow, added upward movement on hover")
