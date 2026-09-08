import codecs

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

target = """  function tick() {
    var p = window._brainScrollProg || 0;

    // Fade in/out del card y el cerebro 2D
    var fadeT = p >= SHOW_START
      ? clamp01((p - SHOW_START) / (SHOW_FADE - SHOW_START))
      : 0;
    if (brain) brain.style.opacity = String(fadeT);
    if (card)  card.style.opacity  = String(fadeT);"""

replacement = """  function tick() {
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

print("Matches with 2 spaces:", norm_text.count(norm_target))

if norm_text.count(norm_target) == 0:
    # try Regex
    import re
    pattern = re.compile(r'function tick\(\) \{\s*var p = window\._brainScrollProg \|\| 0;\s*// Fade in/out del card y el cerebro 2D\s*var fadeT = p >= SHOW_START\s*\?\s*clamp01\(\(p - SHOW_START\) / \(SHOW_FADE - SHOW_START\)\)\s*:\s*0;\s*if \(brain\) brain\.style\.opacity = String\(fadeT\);\s*if \(card\)\s*card\.style\.opacity\s*=\s*String\(fadeT\);')
    
    new_text = pattern.sub(norm_replacement, norm_text)
    print("Regex replacement success!")
else:
    new_text = norm_text.replace(norm_target, norm_replacement)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(new_text)
