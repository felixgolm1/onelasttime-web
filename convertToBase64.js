const fs = require('fs');
const path = require('path');

const inputFile = path.join(__dirname, 'assets', 'models', 'id_card.glb');
const outputFile = path.join(__dirname, 'assets', 'models', 'id_card_base64.js');

try {
  const binaryData = fs.readFileSync(inputFile);
  const base64String = binaryData.toString('base64');
  const fileContent = `const idCardBase64 = "data:application/octet-stream;base64,${base64String}";`;
  
  fs.writeFileSync(outputFile, fileContent);
  console.log(`Successfully created ${outputFile}`);
} catch (e) {
  console.error("Error converting file:", e);
}
