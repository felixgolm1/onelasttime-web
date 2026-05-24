const fs = require('fs');
let content = fs.readFileSync('3d-test.html', 'utf8');

// 1. Extract reviews container
const startMarker = '<div class="oryzo-reviews-container">';
const startIndex = content.indexOf(startMarker);
const scriptStart = content.indexOf('<script>', startIndex);
const endIndex = content.lastIndexOf('</div>', scriptStart);

let reviewsHTML = content.substring(startIndex, endIndex);

// Change IDs so they don't clash
reviewsHTML = reviewsHTML.replace(/id="review-panel-(\d+)"/g, 'id="end-review-panel-$1"');
reviewsHTML = reviewsHTML.replace(/id="rev(\d+)-quote"/g, 'id="end-rev$1-quote"');
reviewsHTML = reviewsHTML.replace(/class="oryzo-reviews-container"/, 'id="end-reviews-container" class="oryzo-reviews-container" style="position:absolute; top: 100vh; left:0; width:100vw; height:100vh; pointer-events:none;"');

// 2. Insert into #oryzo-section before the closing tag of oryzo-section
const oryzoEndMarker = '<!-- ══ FIN SECCIÓN ORYZO ══════════════════════════════ -->';
content = content.replace(oryzoEndMarker, reviewsHTML + '\n    ' + oryzoEndMarker);

// 3. Update maxProg
content = content.replace('const maxProg = 28.6;', 'const maxProg = 30.6;'); // Add 2 steps for end reviews

fs.writeFileSync('3d-test.html', content);
console.log('Duplication done.');
