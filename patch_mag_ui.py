import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix double classes
text = text.replace('class="mag-ui" class="mag-ui"', 'class="mag-ui"')

# Add mag-ui to all textual UI components in the magazine
text = text.replace('<!-- Columnas Laterales -->\n          <div style="display: flex; justify-content: space-between; width: 100%; z-index: 2; margin-top: auto; margin-bottom: 30px;">', '<!-- Columnas Laterales -->\n          <div class="mag-ui" style="display: flex; justify-content: space-between; width: 100%; z-index: 2; margin-top: auto; margin-bottom: 30px;">')

text = text.replace('<!-- Bottom Title -->\n          <div style="width: 100%; text-align: center; z-index: 2; margin-bottom: 5px;">', '<!-- Bottom Title -->\n          <div class="mag-ui" style="width: 100%; text-align: center; z-index: 2; margin-bottom: 5px;">')

# Also add mag-ui to gradients so they fade out and we get the pure image
text = text.replace('<!-- Fondo Oscurecido en la base para el texto -->\n          <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 45%; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0) 100%); z-index: 1;"></div>', '<!-- Fondo Oscurecido en la base para el texto -->\n          <div class="mag-ui" style="position: absolute; bottom: 0; left: 0; width: 100%; height: 45%; background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.6) 40%, rgba(0,0,0,0) 100%); z-index: 1;"></div>')

text = text.replace('<div style="position: absolute; top: 0; left: 0; width: 100%; height: 35%; background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%); z-index: 1;"></div>', '<div class="mag-ui" style="position: absolute; top: 0; left: 0; width: 100%; height: 35%; background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%); z-index: 1;"></div>')

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('UI classes updated')
