import codecs
import re

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

target = """  window._updateBrainReveal = function(tP, maskValue) {
    var canvas = document.getElementById('brain-canvas');
    if (!canvas) return;
    if (tP <= 0) {
      canvas.style.transition = 'none'; // hide instantaneo, sin flash
      canvas.style.opacity = '0';
      canvas.style.webkitMaskImage = '';
      canvas.style.maskImage = '';
    } else {
      canvas.style.transition = '';
      canvas.style.opacity = '1';
      canvas.style.webkitMaskImage = maskValue;
      canvas.style.maskImage = maskValue;
    }
  };"""

replacement = """  window._updateBrainReveal = function(tP, maskValue) {
    var canvas = document.getElementById('brain-canvas');
    if (!canvas) return;
    var p = window._brainScrollProg || 0;
    if (tP <= 0 || p > 22.1) {
      canvas.style.transition = 'none';
      canvas.style.opacity = '0';
      canvas.style.webkitMaskImage = '';
      canvas.style.maskImage = '';
    } else {
      var fadeT = 1.0;
      if (p > 21.6) {
        fadeT = 1.0 - Math.max(0, Math.min(1, (p - 21.6) / 0.5));
      }
      canvas.style.transition = '';
      canvas.style.opacity = String(fadeT);
      canvas.style.webkitMaskImage = maskValue;
      canvas.style.maskImage = maskValue;
    }
  };"""

norm_text = text.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')
norm_replacement = replacement.replace('\r\n', '\n')

print("Matches:", norm_text.count(norm_target))
if norm_text.count(norm_target) > 0:
    new_text = norm_text.replace(norm_target, norm_replacement)
    with codecs.open('3d-test.html', 'w', 'utf-8') as f:
        f.write(new_text)
else:
    print("Failed to find exact text, using regex")
    pattern = re.compile(r'window\._updateBrainReveal\s*=\s*function\(tP,\s*maskValue\)\s*\{\s*var canvas = document\.getElementById\(\'brain-canvas\'\);\s*if \(\!canvas\) return;\s*if \(tP <= 0\) \{\s*canvas\.style\.transition = \'none\';\s*// hide instantaneo, sin flash\s*canvas\.style\.opacity = \'0\';\s*canvas\.style\.webkitMaskImage = \'\';\s*canvas\.style\.maskImage = \'\';\s*\} else \{\s*canvas\.style\.transition = \'\';\s*canvas\.style\.opacity = \'1\';\s*canvas\.style\.webkitMaskImage = maskValue;\s*canvas\.style\.maskImage = maskValue;\s*\}\s*\};')
    new_text = pattern.sub(norm_replacement, norm_text)
    with codecs.open('3d-test.html', 'w', 'utf-8') as f:
        f.write(new_text)
