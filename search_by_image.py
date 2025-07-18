import pyautogui
import cv2
import time

# Espera unos segundos para que puedas cambiar de ventana
print("El bot comenzará en 5 segundos...")
time.sleep(5)

# Nombre de la imagen de referencia (debe estar en la misma carpeta)
target_image = 'target.png'

while True:
    # Busca la imagen en pantalla
    location = pyautogui.locateCenterOnScreen(target_image, confidence=0.8)

    if location is not None:
        print(f"Imagen encontrada en: {location}")
        pyautogui.moveTo(location)
        pyautogui.click()
        time.sleep(1)  # tiempo entre clicks
    else:
        print("Imagen no encontrada.")
    
    time.sleep(2)  # espera antes de volver a buscar
