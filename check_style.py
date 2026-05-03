import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print("First </style> at index:", content.find('</style>'))
print("Context around it:")
idx = content.find('</style>')
print(content[max(0, idx-100):idx+50])
