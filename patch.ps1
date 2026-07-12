$content = Get-Content "c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html" -Encoding UTF8 -Raw

# 1. Update onclick event handlers
$content = $content.Replace('onclick="window.chooseFinal(true)"', 'onclick="window.chooseFinal(event, true)"')
$content = $content.Replace('onclick="window.chooseFinal(false)"', 'onclick="window.chooseFinal(event, false)"')

# 2. Update window.chooseFinal function
$oldJS = 'window.chooseFinal = function(happy) {
  window._finalChoice = happy;
  // Ocultar el panel permanentemente
  var panel = document.getElementById(''final-panel'');
  if (panel) { panel.style.opacity = ''0''; panel.style.pointerEvents = ''none''; }
  // Crossfade a la imagen elegida en el slide de la pista GRANDE
  var largeAging = document.querySelector(''.carousel-track-large [id="final-slide"]'');
  if (largeAging) {
    var imgs = largeAging.querySelectorAll(''img'');
    if (imgs[0]) imgs[0].style.opacity = ''0'';                 // escoger final   oculta
    if (imgs[1]) imgs[1].style.opacity = happy ? ''1'' : ''0'';  // con final feliz
    if (imgs[2]) imgs[2].style.opacity = happy ? ''0'' : ''1'';  // sin final feliz
  }
};'
$newJS = 'window.chooseFinal = function(e, happy) {
  if (e) {
    e.stopPropagation();
    e.preventDefault();
  }
  window._finalChoice = happy;
  document.querySelectorAll(''.final-ov'').forEach(p => {
    p.style.opacity = ''0''; p.style.pointerEvents = ''none'';
  });
  document.querySelectorAll(''#final-slide'').forEach(slide => {
    var imgs = slide.querySelectorAll(''img'');
    if (imgs[0]) imgs[0].style.opacity = ''0'';
    if (imgs[1]) imgs[1].style.opacity = happy ? ''1'' : ''0'';
    if (imgs[2]) imgs[2].style.opacity = !happy ? ''1'' : ''0'';
  });
};'
$content = $content.Replace($oldJS, $newJS)

# 3. Update smoothScrollLoop (delete final-panel, add final-feliz reset)
# Regex to match the old FINAL PANEL block, handling encoding safely
$pattern = '(?s)// --- FINAL PANEL.*?if \([^}]*\}\s*\}\s*\}\s*\}\s*\}'
$newScroll = '// --- FINAL FELIZ RESET ---
          if (largeItems.length > 0) {
            let finalIndex = -1;
            for (let k = 0; k < largeItems.length; k++) {
              if (largeItems[k].id === ''final-slide'') { finalIndex = k; break; }
            }
            if (finalIndex >= 0 && Math.abs(currIndex - finalIndex) > 1.0 && window._finalChoice != null) {
              window._finalChoice = null;
              document.querySelectorAll(''.final-ov'').forEach(p => {
                p.style.opacity = ''1''; p.style.pointerEvents = ''auto'';
              });
              document.querySelectorAll(''#final-slide'').forEach(slide => {
                var imgs = slide.querySelectorAll(''img'');
                if (imgs[0]) imgs[0].style.opacity = ''1'';
                if (imgs[1]) imgs[1].style.opacity = ''0'';
                if (imgs[2]) imgs[2].style.opacity = ''0'';
              });
            }
          }'
$content = [regex]::Replace($content, $pattern, $newScroll)

Set-Content "c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html" $content -Encoding UTF8
