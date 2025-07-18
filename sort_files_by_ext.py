import os
import shutil

# Ruta de la carpeta a organizar
source_folder = r"C:\Users\Asus\Downloads"

# Crear carpetas por tipo si no existen
def create_folder(extension):
    folder = os.path.join(source_folder, extension.upper())
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

# Iterar archivos y moverlos
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        ext = file.split('.')[-1]
        target_folder = create_folder(ext)
        shutil.move(file_path, os.path.join(target_folder, file))

print("✅ Organización completa.")
