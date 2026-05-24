import re

with open('3d-test.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to capture the innerHTML of the deck before any animations happen.
# We can just clone the cards from `#card-table` if they are missing!
# Because by the time we clone the box, the cards are in `#card-table`!
new_js = """
      var deckContainer = document.getElementById('oryzo-deck-container');
      if (deckContainer && !document.getElementById('oryzo-deck-clone')) {
          var original = document.getElementById('mag-deck-container');
          if (original) {
              var clone = original.cloneNode(true);
              clone.id = 'oryzo-deck-clone';
              
              // RESTORE CARDS
              // Since the original cards were moved to #card-table, mag-deck-container is empty!
              // We need to re-create the cards inside the clone's interior-cards.
              var interior = clone.querySelector('.interior-cards');
              if (interior) {
                  interior.innerHTML = ''; // clear any dummy
                  for(let i=1; i<=4; i++) {
                      let c = document.querySelector('.card-n' + i);
                      if (c) {
                          let cClone = c.cloneNode(true);
                          // Reset styles
                          cClone.style = '';
                          cClone.className = 'card-wrap card-n' + i + ' card-in-deck';
                          cClone.style.transformStyle = 'preserve-3d';
                          // Remove data attributes so our logic picks them up fresh
                          delete cClone.dataset.endState;
                          interior.appendChild(cClone);
                      }
                  }
              }

              clone.style.position = 'absolute';
              clone.style.left = '50%';
"""

old_target = """
      var deckContainer = document.getElementById('oryzo-deck-container');
      if (deckContainer && !document.getElementById('oryzo-deck-clone')) {
          var original = document.getElementById('mag-deck-container');
          if (original) {
              var clone = original.cloneNode(true);
              clone.id = 'oryzo-deck-clone';
              clone.style.position = 'absolute';
              clone.style.left = '50%';
"""

import sys
if old_target.strip() in content:
    content = content.replace(old_target.strip(), new_js.strip())
    with open('3d-test.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Cards restored inside clone successfully.")
else:
    print("Target block not found!")
    sys.exit(1)
