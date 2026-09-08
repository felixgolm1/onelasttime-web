import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

search = """        // Ocultar formulario sutilmente para disfrutar de la explosion
        var formContainer = document.getElementById('vip-form-container');
        if (formContainer) {
            formContainer.style.transition = 'opacity 0.4s ease';
            formContainer.style.opacity = '0';
        }
        
        // Redirigir suavemente a la landing page
        setTimeout(function() {
            window.location.href = '3d-test.html';
        }, 600);"""

replacement = """        // Ocultar toda la pagina sutilmente (fade to black total)
        document.body.style.transition = 'opacity 0.8s ease';
        document.body.style.opacity = '0';
        
        // Redirigir a la landing page una vez todo esta en negro
        setTimeout(function() {
            window.location.href = '3d-test.html';
        }, 850);"""

if search in content:
    content = content.replace(search, replacement)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed fade out in index.html")
else:
    print("Could not find the target string in index.html")
