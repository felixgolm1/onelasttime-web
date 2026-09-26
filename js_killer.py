import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the brute force css hack
content = content.replace("""  /* KILL CORNER GLITCH BRUTE FORCE */
  @media (max-width: 768px) {
      html { background-color: #000 !important; }
      body { clip-path: inset(2px 0 0 2px) !important; background-color: transparent !important; }
      #css-container, #c, #pWrap { clip-path: inset(2px 0 0 2px) !important; }
  }""", "")

# Inject JS at the end of the body to literally delete stray text nodes from the DOM
js_killer = """
<script>
  // SCRIPT DEFINITIVO MATA-FANTASMAS (SOLO MÓVIL)
  window.addEventListener('DOMContentLoaded', () => {
      if (window.innerWidth <= 768 || window._cIsMobile) {
          // Destruye cualquier salto de línea o nodo de texto suelto en el body
          const nodes = Array.from(document.body.childNodes);
          nodes.forEach(node => {
              if (node.nodeType === Node.TEXT_NODE) {
                  node.remove();
              }
          });
      }
  });
</script>
</body>
"""

content = re.sub(r'</body>', js_killer, content)

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Injected JS killer")
