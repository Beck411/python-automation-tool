import os

folder = r"C:\Users\Asus\Downloads"
prefijo = "foto_"
extension = ".jpg"

archivos = [f for f in os.listdir(folder) if f.endswith(extension)]
archivos.sort()

for i, nombre in enumerate(archivos, start=1):
    nuevo_nombre = f"{prefijo}{str(i).zfill(3)}{extension}"
    ruta_origen = os.path.join(folder, nombre)
    ruta_destino = os.path.join(folder, nuevo_nombre)
    os.rename(ruta_origen, ruta_destino)
    print(f"🔄 {nombre} → {nuevo_nombre}")

print("✅ Renombrado completo.")
