const fs = require('fs');

let html = fs.readFileSync('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', 'utf-8');

// 1. DUPLICATE rev2 logic for rev3
const rev2StartStr = `const rev2 = document.getElementById('review-panel-2');`;
const rev2Start = html.indexOf(rev2StartStr);

// Find the end of rev2 block: it ends right before `// Lógica de extracción de c1` or `// Lógica Extracción CARTA 1`
const rev2EndStr = `// Lógica Extracción CARTA 1`;
const rev2End = html.indexOf(rev2EndStr, rev2Start);

let rev2Block = html.substring(rev2Start, rev2End);

let rev3Block = rev2Block.replace(/rev2/g, 'rev3');
rev3Block = rev3Block.replace(/review-panel-2/g, 'review-panel-3');
rev3Block = rev3Block.replace(/4\.72/g, '6.52');
rev3Block = rev3Block.replace(/6\.32/g, '8.12');
// Note: we might need to adjust some specific pRev mapRanges inside, but 4.72 and 6.32 are the bounds.

html = html.substring(0, rev2End) + rev3Block + '\n      ' + html.substring(rev2End);

// 2. DUPLICATE c2 extraction logic for c3
const c2StartStr = `// Lógica de extracción de c2`;
const c2Start = html.indexOf(c2StartStr);

const tableCardsFadeStr = `// ─ Fade de cartas en la mesa`;
let c2End = html.indexOf(tableCardsFadeStr, c2Start);
// Backtrack to the start of the comment line
while(html[c2End-1] === ' ' || html[c2End-1] === '\n') {
    c2End--;
}

let c2Block = html.substring(c2Start, c2End);

let c3Block = c2Block.replace(/c2/g, 'c3');
c3Block = c3Block.replace(/fakeCard2/g, 'fakeCard3');
c3Block = c3Block.replace(/nth-child\(1\)/g, 'nth-child(2)'); // fakeCard3
// Range replacements for c3:
// c2 peek ended at 5.12. c2 move_in: 4.72 to 5.12, 5.12 to 5.52.
// We mapped c3 to: peek 6.02 to 6.52.
// Wait, the original code for c2 has:
// y = -35 - 295 * c2_peek;
c3Block = c3Block.replace(/4\.72/g, '6.52');
c3Block = c3Block.replace(/5\.12/g, '6.92');
c3Block = c3Block.replace(/5\.52/g, '7.32');
c3Block = c3Block.replace(/6\.02/g, '7.82');
c3Block = c3Block.replace(/6\.62/g, '8.42');
c3Block = c3Block.replace(/5\.02/g, '6.82');
c3Block = c3Block.replace(/5\.22/g, '7.02');
c3Block = c3Block.replace(/5\.82/g, '7.62');

html = html.substring(0, c2End) + '\n\n      ' + c3Block + html.substring(c2End);

fs.writeFileSync('c:/Users/Félix Gol/.gemini/antigravity/scratch/sensibles-web/3d-test.html', html);
console.log('Patched successfully');
