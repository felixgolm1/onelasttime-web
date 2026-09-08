import codecs

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

css_to_replace = """.btn-blue:hover .cta-arrow-pill {
          transform: translateY(-50%) scale(1.15);
        }"""

new_css = """.btn-blue:hover .cta-arrow-pill {
          transform: translateY(-50%) scale(1.15);
          animation: bounceArrowPill 0.75s ease-in-out forwards;
        }
        @keyframes bounceArrowPill {
          0%   { transform: translateY(-50%) scale(1.0) translateX(0); }
          20%  { transform: translateY(-50%) scale(1.15) translateX(8px); }
          40%  { transform: translateY(-50%) scale(1.15) translateX(0); }
          60%  { transform: translateY(-50%) scale(1.15) translateX(4px); }
          80%  { transform: translateY(-50%) scale(1.15) translateX(0); }
          90%  { transform: translateY(-50%) scale(1.15) translateX(1px); }
          100% { transform: translateY(-50%) scale(1.15) translateX(0); }
        }"""

# Replace all occurrences
text = text.replace(css_to_replace, new_css)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(text)
