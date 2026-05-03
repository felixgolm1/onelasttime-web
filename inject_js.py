import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

js = '''
    // -- Animación de la Reseña Estilo Oryzo --
    const osr = document.getElementById('oryzo-style-review');
    if (osr) {
      scrollTl.fromTo(osr, 
        { y: '100vh', opacity: 1 },
        { y: '-100vh', duration: 0.80, ease: 'linear' },
        0.08
      );
      
      scrollTl.to(osr, { opacity: 0, duration: 0.16, ease: 'power2.inOut' }, 0.72);

      scrollTl.fromTo('.osr-quote-fg',
        { clipPath: 'inset(0% 0% 0% 100%)' },
        { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.30, ease: 'power1.inOut' },
        0.30 
      );

      scrollTl.fromTo('.osr-img-wrapper img',
        { scale: 1.0, filter: 'brightness(0.3)' },
        { scale: 1.3, filter: 'brightness(1.0)', duration: 0.45, ease: 'power1.out' },
        0.25
      );
    }

'''

target = "scrollTl.to([mg, visGroup], {\n      rotationY: -540, rotation: -2.5,"
if target in content and 'Animación de la Reseña Estilo Oryzo' not in content:
    content = content.replace(target, js + target)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("JS injected")
else:
    print("Target not found or already injected")

