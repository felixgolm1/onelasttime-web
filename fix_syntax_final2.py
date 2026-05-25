import os

path = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web\3d-test.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# For the first one, we just replace the exact block
target1 = """          updateGlobalScenes();
          }
  
          // ─ Edge glow: matemáticamente atado a prog (y apoyado por transition CSS)"""
          
replacement1 = """          updateGlobalScenes();
  
          // ─ Edge glow: matemáticamente atado a prog (y apoyado por transition CSS)"""

# In python string literal, the em-dash might not match if the encoding is weird.
# So I'll just use string replacement
content = content.replace("          updateGlobalScenes();\n          }", "          updateGlobalScenes();")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
