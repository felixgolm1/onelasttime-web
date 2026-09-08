import os
import shutil
import subprocess

dev_dir = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web"
prod_dir = r"c:\Users\Félix Gol\.gemini\antigravity\scratch\sensibles-web-produccion"

print("1. Copiando 3d-test.html a index.html en PROD...")
shutil.copy2(os.path.join(dev_dir, "3d-test.html"), os.path.join(prod_dir, "index.html"))

print("2. Copiando reservar-mi-cena.html a PROD...")
shutil.copy2(os.path.join(dev_dir, "reservar-mi-cena.html"), os.path.join(prod_dir, "reservar-mi-cena.html"))

print("3. Copiando assets/ a PROD...")
shutil.copytree(os.path.join(dev_dir, "assets"), os.path.join(prod_dir, "assets"), dirs_exist_ok=True)

print("4. Sincronizando DEV a GitHub...")
subprocess.run(["git", "push", "origin", "main"], cwd=dev_dir)

print("5. Sincronizando PROD a GitHub...")
subprocess.run(["git", "add", "."], cwd=prod_dir)
subprocess.run(["git", "commit", "-m", "hecho: pase a produccion"], cwd=prod_dir)
subprocess.run(["git", "push", "origin", "main"], cwd=prod_dir)

print("¡Pase a producción completado!")
