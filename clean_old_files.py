import os
import time

folder = r"C:\Users\Asus\Downloads"
dias_maximos = 30  # Archivos más viejos de 30 días

ahora = time.time()

for file in os.listdir(folder):
    ruta = os.path.join(folder, file)
    if os.path.isfile(ruta):
        tiempo_archivo = os.path.getmtime(ruta)
        if ahora - tiempo_archivo > dias_maximos * 86400:
            os.remove(ruta)
            print(f"🗑️ Eliminado: {file}")

print("✅ Limpieza finalizada.")
