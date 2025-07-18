import pyautogui
import time

print("Empezando en 5 segundos. Cambia al juego o app...")
time.sleep(5)

while True:
    pyautogui.click()
    print("Click!")
    time.sleep(2)
