#!/usr/bin/env python3
"""
NUEVO ENFOQUE: Mover cartas a oryzoSec directamente (position:fixed dentro),
en vez de endCardTable. oryzoSec es el mismo contexto donde ya son visibles
(peeking funciona). Con position:fixed + z-index alto quedan encima del deck.
"""

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# Reemplazar endCardTable.appendChild(ec1/ec2/ec3/ec4) 
# por oryzoSec.appendChild(ec?), y cambiar position a 'fixed'

for i in ['1','2','3','4']:
    # Reemplazar appendChild y posicion en bloque parentNode
    old = f'endCardTable.appendChild(ec{i});ec{i}.classList.remove(\'card-in-deck\',\'card-peeking\');ec{i}.classList.add(\'card-on-table\');ec{i}.style.position=\'absolute\''
    new = f'oryzoSec.appendChild(ec{i});ec{i}.classList.remove(\'card-in-deck\',\'card-peeking\');ec{i}.classList.add(\'card-on-table\');ec{i}.style.position=\'fixed\''
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f'EC{i}: appendChild to oryzoSec + position:fixed OK')
    else:
        print(f'EC{i}: NOT FOUND - checking...')
        idx = content.find(f'endCardTable.appendChild(ec{i})')
        if idx >= 0:
            print(repr(content[idx:idx+150]))

# Tambien cambiar la condicion parentNode para cada carta
for i in ['1','2','3','4']:
    old = f'ec{i}.parentNode!==endCardTable'
    new = f'ec{i}.parentNode!==oryzoSec'
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f'EC{i}: parentNode check updated')
    else:
        print(f'EC{i}: parentNode check NOT FOUND')

# Aseguramos que oryzoSec esta disponible en el scope del bloque de cartas
# Buscar donde se declara oryzoSec y verificar que esta en scope
idx_oryzo = content.find("var oryzoSec = document.getElementById('oryzo-section');")
idx_cards = content.find("let ec1_peek =")
print(f"\noryzoSec declarada en caracter {idx_oryzo}, cartas en {idx_cards}")
print(f"oryzoSec esta antes que las cartas: {idx_oryzo < idx_cards}")

with open('3d-test.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n=== {changes} cambios aplicados ===")
