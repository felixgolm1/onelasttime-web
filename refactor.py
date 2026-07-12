import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

html_blocks = [
    {
        'id': 'end-review-panel-1',
        'quote': '"Es increíble cómo una simple carta puede generar <span class="review-highlight">conversaciones tan profundas</span> y auténticas. Lo recomiendo 100%."',
        'author': 'ELSA NARANJO',
        'handle': '@elsaaang6',
        'img': 'elsa.png'
    },
    {
        'id': 'end-review-panel-2',
        'quote': '"¡<span class="review-highlight">Flipé</span> al ver cartas hechas para nuestro aniversario! Nos hicieron tener <span class="review-highlight">conversaciones que nunca antes habíamos tenido</span>. Y sin duda ahora estamos más preparados para durar muchos años más. Ya <span class="review-highlight">he obligado a mis amigas a probarlo</span>."',
        'author': 'LAURA GIL',
        'handle': '@_laugilp',
        'img': 'lauric.jpeg'
    },
    {
        'id': 'end-review-panel-3',
        'quote': '"Conseguir expresar tanto agradecimiento no es fácil, y sin duda es el mejor regalo que se puede hacer a alguien. Fue <span class="review-highlight">uno de los momentos más bonitos que hemos compartido en familia</span>. Infinitas gracias."',
        'author': 'FRANCISCO ARBESÚ',
        'handle': '@franarbesu',
        'img': 'fran.jpeg'
    },
    {
        'id': 'end-review-panel-4',
        'quote': '"<span class="review-highlight">El equipo lloró, rió y se unió como nunca</span>. Cuando consigues que en una empresa <span class="review-highlight">se hable desde la vulnerabilidad y no desde el ego</span>, la cultura del equipo cambia para siempre. Una <span class="review-highlight">experiencia absolutamente transformadora</span>."',
        'author': 'IRIA MUDARRA',
        'handle': '@iriamudarra',
        'img': 'iria.jpeg'
    }
]

panels_html = ""
for p in html_blocks:
    rev_id = p['id'].replace("review-panel", "rev").replace("-1", "1").replace("-2", "2").replace("-3", "3").replace("-4", "4")
    panels_html += f'''
    <div class="oryzo-review-panel" id="{p['id']}">
      <div class="osr-body" style="align-items: center; flex-direction: row; justify-content: space-between; width: 100%; max-width: 1000px; gap: 4rem;">
        
        <!-- LEFT COLUMN (Text) -->
        <div class="review-text-col" style="width: 50%; display: flex; flex-direction: column; align-items: flex-start; text-align: left; color: #ffffff; font-family: 'Inter', sans-serif;">
          <div class="osr-top-line" style="justify-content: flex-start;">
            <div>LA RESEÑA</div>
          </div>
          <div class="osr-stars-small" style="font-family:'Inter', sans-serif; justify-content: flex-start; width: auto;"><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span><span class="star">★</span> <span class="rating-number" style="opacity: 0.5; margin-left: 8px; font-weight: 400;">[0/5]</span></div>
          <div class="review-quote" id="{rev_id}-quote" style="text-align: left;">{p['quote']}</div>
          <div class="review-author" style="text-align: left;">
            {p['author']}<br>
            <span style="display:inline-flex; align-items:center; gap: 6px; margin-top: 4px; text-transform: none; letter-spacing: 0; line-height: 1;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="opacity:1"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
              {p['handle']}
            </span>
          </div>
        </div>

        <!-- RIGHT COLUMN (Image) -->
        <div class="review-img-col" style="width: 40%; display: flex; justify-content: flex-end;">
          <img src="assets/img/{p['img']}" alt="Review">
        </div>
        
      </div>
    </div>
'''

# Delete lines 9131 to 9226 (which is index 9131 to 9226 in 0-based since 9132 is line index 9131)
# Wait, let's just find the start and end by content to be safe.
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="oryzo-review-panel" id="end-review-panel-1">' in line:
        start_idx = i
    if '<!-- ── IMG STRIP CAROUSEL (after testimonios) ── -->' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    # end_idx is the carousel comment. The div closing the container is right before it.
    # We want to replace from start_idx up to the end of the last panel.
    # The last panel closes right before the container closing div, which is 2 lines before end_idx.
    
    new_lines = lines[:start_idx] + [panels_html] + lines[end_idx-2:]
    
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Reemplazo de paneles exitoso.")
else:
    print(f"No se encontró start ({start_idx}) o end ({end_idx})")
