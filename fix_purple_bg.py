import codecs

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

target = """              var _bgOp = Math.min(1, _tPdiv / 0.15);
              if (_bgEl)  { _bgEl.style.opacity = String(_bgOp);  _bgEl.style.webkitMaskImage = _mv;  _bgEl.style.maskImage = _mv; }
              if (_silWr) { _silWr.style.opacity = String(_bgOp); _silWr.style.webkitMaskImage = _mv; _silWr.style.maskImage = _mv; }
              if (_vigEl) { _vigEl.style.opacity = String(_bgOp); _vigEl.style.webkitMaskImage = _mv; _vigEl.style.maskImage = _mv; }"""

replacement = """              var _bgOp = Math.min(1, _tPdiv / 0.15);
              if (prog > 21.6) {
                  _bgOp *= Math.max(0, 1.0 - (prog - 21.6) / 0.5);
              }
              if (_bgEl)  { _bgEl.style.opacity = String(_bgOp);  _bgEl.style.webkitMaskImage = _mv;  _bgEl.style.maskImage = _mv; }
              if (_silWr) { _silWr.style.opacity = String(_bgOp); _silWr.style.webkitMaskImage = _mv; _silWr.style.maskImage = _mv; }
              if (_vigEl) { _vigEl.style.opacity = String(_bgOp); _vigEl.style.webkitMaskImage = _mv; _vigEl.style.maskImage = _mv; }"""

norm_text = text.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')
norm_replacement = replacement.replace('\r\n', '\n')

print("Matches:", norm_text.count(norm_target))

if norm_text.count(norm_target) > 0:
    new_text = norm_text.replace(norm_target, norm_replacement)
    with codecs.open('3d-test.html', 'w', 'utf-8') as f:
        f.write(new_text)
else:
    print("Fallback to regex")
    import re
    pattern = re.compile(r'var _bgOp = Math\.min\(1, _tPdiv / 0\.15\);\s*if \(_bgEl\)\s*\{\s*_bgEl\.style\.opacity = String\(_bgOp\);\s*_bgEl\.style\.webkitMaskImage = _mv;\s*_bgEl\.style\.maskImage = _mv;\s*\}\s*if \(_silWr\)\s*\{\s*_silWr\.style\.opacity = String\(_bgOp\);\s*_silWr\.style\.webkitMaskImage = _mv;\s*_silWr\.style\.maskImage = _mv;\s*\}\s*if \(_vigEl\)\s*\{\s*_vigEl\.style\.opacity = String\(_bgOp\);\s*_vigEl\.style\.webkitMaskImage = _mv;\s*_vigEl\.style\.maskImage = _mv;\s*\}')
    new_text = pattern.sub(norm_replacement, norm_text)
    with codecs.open('3d-test.html', 'w', 'utf-8') as f:
        f.write(new_text)
