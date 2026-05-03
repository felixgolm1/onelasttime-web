import os

filepath = r'c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\assets\img\elsa.png'
if os.path.exists(filepath):
    size = os.path.getsize(filepath)
    print(f"File size: {size / 1024 / 1024:.2f} MB")
else:
    print("File not found")
