import os, re

css_add = '''
        .btn { position: relative; display: inline-flex; align-items: center; justify-content: center; padding: 1.3rem 2rem; border-radius: 100px; text-decoration: none; cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 700; overflow: hidden; white-space: nowrap; pointer-events: auto; -webkit-font-smoothing: antialiased; }
        .btn-full { width: 100%; }
        .btn-blue { background: rgba(0, 0, 0, 0.25); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); color: rgba(204, 255, 0, 0.95); border: 1px solid rgba(204, 255, 0, 0.45); box-shadow: inset 0 0 20px rgba(204, 255, 0, 0.25); letter-spacing: 0.1em; font-size: 1.25rem; text-transform: uppercase; transition: background 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.6s cubic-bezier(0.16, 1, 0.3, 1); }
        .btn-blue:hover { background: rgba(0, 0, 0, 0.35); border-color: rgba(204, 255, 0, 0.9); box-shadow: inset 0 0 45px rgba(204, 255, 0, 0.6); }
        .cta-arrow-pill { position: absolute; top: 50%; transform: translateY(-50%); border-radius: 100px; display: flex; align-items: center; justify-content: center; z-index: 2; background: #ccff00; box-shadow: 0 2px 8px rgba(0,0,0,0.4); color: #111; transition: transform 0.25s ease-out; }
        .btn-blue:hover .cta-arrow-pill { transform: translateY(-50%) scale(1.15); }
        .cta-text-span { padding-right: 20px !important; transform: translateX(-18px) !important; }
    </style>
'''

header_html = '''<body>
    <header style="display: flex; justify-content: space-between; align-items: center; padding: 20px 40px; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); background: rgba(0,0,0,0.5); border-bottom: 1px solid rgba(255,255,255,0.05);">
        <a href="3d-test.html" style="display: flex; flex-direction: column; align-items: flex-start; gap: 2px; text-decoration: none;">
            <img src="assets/img/logo%20one%20last%20time.png" alt="One Last Time" style="height: 48px; width: auto; filter: brightness(0) invert(1);">
            <img src="assets/img/by_sensibles.png" alt="by Sensibles" style="height: 24px; width: auto; filter: brightness(0) invert(1); transform: translateZ(0);">
        </a>
        <a href="3d-test.html" style="display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; color: #fff; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.75rem; text-decoration: none; transition: all 0.3s ease;" onmouseover="this.style.color='#ccff00'; this.style.borderColor='rgba(204,255,0,0.4)'; this.style.background='rgba(204,255,0,0.05)';" onmouseout="this.style.color='#fff'; this.style.borderColor='rgba(255,255,255,0.2)'; this.style.background='rgba(255,255,255,0.1)';">
            <span style="display:inline-block; width:4px; height:4px; background-color:currentColor; border-radius:50%; margin-right:6px;"></span>
            VOLVER A ONE LAST TIME
        </a>
    </header>
    <div class="container" style="padding-top: 40px;">'''

bottom_cta = '''
        <div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px;">
            <a href="3d-test.html" class="btn btn-blue btn-full" style="padding: 0.85rem 2rem !important; height: auto; max-width: 400px;">
                <div style="position:relative; width:100%; height:100%; display:flex; align-items:center; justify-content:center;">
                    <span class="cta-text-span" style="position:relative; z-index:2; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-size: 0.95rem;">VOLVER A ONE LAST TIME</span>
                    <div class="cta-arrow-pill" style="right: 8px; width: 36px; height: 36px;">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 2px;">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </div>
                </div>
            </a>
        </div>
    </div>
</body>
'''

for file in ['terminos.html', 'privacidad.html']:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace('</style>', css_add)
    text = re.sub(r'<body>\s*<div class="container">\s*<header.*?</header>', header_html, text, flags=re.DOTALL)
    text = re.sub(r'<div style="display: flex; justify-content: center; margin-top: 80px; margin-bottom: 40px;">.*?</div>\s*</div>\s*</body>\s*</html>', bottom_cta + '\n</html>', text, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
