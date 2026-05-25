const fs = require('fs');
let content = fs.readFileSync('3d-test.html', 'utf8');

const replacements = {
  '37.0': '29.98',
  '9.62': '2.6',
  '10.02': '3.0',
  '10.62': '3.6',
  '11.62': '4.6',
  '12.62': '5.6',
  '13.62': '6.6',
  '14.62': '7.6',
  '14.67': '7.65',
  '14.72': '7.7',
  '14.73': '7.71',
  '15.2': '8.18',
  '15.3': '8.28',
  '15.30': '8.28',
  '15.35': '8.33',
  '15.6': '8.58',
  '15.92': '8.9',
  '16.20': '9.18',
  '16.27': '9.25',
  '16.3': '9.28',
  '16.8': '9.78',
  '17.0': '9.98',
  '17.2': '10.18',
  '17.3': '10.28',
  '17.43': '10.41',
  '17.5': '10.48',
  '17.58': '10.56',
  '17.8': '10.78',
  '26.0': '18.98'
};

// Sort keys by length descending to replace '15.35' before '15.3'
const keys = Object.keys(replacements).sort((a, b) => b.length - a.length);

keys.forEach(key => {
  // Use regex with word boundaries to ensure we match the exact number
  const regex = new RegExp('(\\\\b)' + key.replace('.', '\\\\.') + '(\\\\b)', 'g');
  content = content.replace(regex, '' + replacements[key] + '');
});

fs.writeFileSync('3d-test.html', content);
console.log('Replaced successfully.');
