import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

target = """    function tick() {
      var p = window._brainScrollProg || 0;
  
      // Fade in/out del card y el cerebro 2D
      var fadeT = p >= SHOW_START
        ? clamp01((p - SHOW_START) / (SHOW_FADE - SHOW_START))
        : 0;
      if (brain) brain.style.opacity = String(fadeT);
      if (card)  card.style.opacity  = String(fadeT);"""

replacement = """    function tick() {
      var p = window._brainScrollProg || 0;
  
      // Fade in/out del card y el cerebro 2D
      var fadeT = 0;
      if (p >= SHOW_START && p <= 21.6) {
        fadeT = clamp01((p - SHOW_START) / (SHOW_FADE - SHOW_START));
      } else if (p > 21.6) {
        fadeT = 1.0 - clamp01((p - 21.6) / 0.5);
      }
      if (brain) brain.style.opacity = String(fadeT);
      if (card)  card.style.opacity  = String(fadeT);"""

norm_text = text.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')
norm_replacement = replacement.replace('\r\n', '\n')

print("Matches:", norm_text.count(norm_target))

new_text = norm_text.replace(norm_target, norm_replacement)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(new_text)
