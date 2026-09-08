import codecs

with codecs.open('3d-test.html', 'r', 'utf-8') as f:
    text = f.read()

target = """.btn-blue:hover .cta-arrow-pill {
          transform: translateY(-50%) scale(1.15);
          animation: bounceArrowPill 0.6s ease-in-out forwards;
        }
        @keyframes bounceArrowPill {
          0%   { transform: translateY(-50%) scale(1.0) translateX(0); }
          25%  { transform: translateY(-50%) scale(1.15) translateX(8px); }
          50%  { transform: translateY(-50%) scale(1.15) translateX(0); }
          75%  { transform: translateY(-50%) scale(1.15) translateX(8px); }
          100% { transform: translateY(-50%) scale(1.15) translateX(0); }
        }"""

replacement = """.btn-blue:hover .cta-arrow-pill {
        transform: translateY(-50%) scale(1.15);
      }"""

# Normalize newlines
norm_text = text.replace('\r\n', '\n')
norm_target = target.replace('\r\n', '\n')
norm_replacement = replacement.replace('\r\n', '\n')

print("Occurrences:", norm_text.count(norm_target))

new_text = norm_text.replace(norm_target, norm_replacement)

with codecs.open('3d-test.html', 'w', 'utf-8') as f:
    f.write(new_text)
