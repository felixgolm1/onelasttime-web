import re
with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Restore scOverlay tween
text = text.replace(
    "// Overlay desactivado para no quitar la mesa de fondo como se solicitó\n    // scrollTl.to(scOverlay, { opacity: 1, duration: 0.08, ease: 'power3.inOut' }, 0);",
    "// Overlay: 0->100%\n    scrollTl.to(scOverlay, { opacity: 1, duration: 0.08, ease: 'power3.inOut' }, 0);"
)

# 2. Disable tooltip
text = text.replace(
    "setupCardTooltip('.card-n2', 'card2-tooltip', htmlCard2);",
    "// setupCardTooltip('.card-n2', 'card2-tooltip', htmlCard2); // Desactivado como se solicitó"
)

# 3. Fix HTML structure for oryzo-reviews-container
# Let's extract the old one and replace it.
import re
new_html = '''
  <div class="oryzo-reviews-container">
    <div class="oryzo-review-panel" id="review-panel-1">
      <div class="osr-top-line">
        <div class="osr-top-left">RATING & REVIEWS</div>
        <div class="osr-top-center">CUSTOM REVIEWS [ 364 ] <span class="osr-stars">★★★★★ [ 5/5 ]</span></div>
        <div class="osr-top-right">SENSIBLES IN USE</div>
      </div>
      <div class="osr-body">
        <div class="review-text-col">
          <div class="osr-stars-small">★★★★★ [ 5/5 ]</div>
          <div class="review-quote">
            <span class="review-quote-bg">"Es increíble cómo una simple carta puede generar <span class="review-highlight">conversaciones tan profundas</span> y auténticas. Lo recomiendo 100%."</span>
            <span class="review-quote-fg">"Es increíble cómo una simple carta puede generar <span class="review-highlight">conversaciones tan profundas</span> y auténticas. Lo recomiendo 100%."</span>
          </div>
          <div class="review-author">SARA M.<br><span style="font-size:0.65rem;font-weight:400;opacity:0.6;">APASIONADA DEL BAILE</span></div>
        </div>
        <div class="review-img-col">
          <img src="assets/img/elsa.png" alt="Review Elsa">
        </div>
      </div>
    </div>
  </div>
'''

text = re.sub(r'<div class="oryzo-reviews-container">.*?</div>\s*</div>\s*</div>', new_html, text, flags=re.DOTALL)

with open(r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
