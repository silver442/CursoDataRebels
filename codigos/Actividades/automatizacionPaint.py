# Importacion de librerias
import pyautogui
import time

# abrir el menú de inicio
pyautogui.press('win')

time.sleep(1)

# Escribir Paint
pyautogui.write('Paint')
time.sleep(1)
pyautogui.press('Enter')

time.sleep(2)
# pyautogui.size(1920,1080)
# time.sleep(1)

# pyautogui.press('winright')

pyautogui.moveTo(665, 105, duration=1)
pyautogui.click()

# Movemos el ratón hasta el area de dibujo
pyautogui.moveTo(665, 450, duration=1)

# Hacemos clic y mantenemos pulsado el botón del ratón
#pyautogui.mouseDown()

# Arrastramos el archivo a la nueva ubicación (400, 400)
#pyautogui.dragTo(400, 400, duration=2)

# Soltamos el botón del ratón para soltar el archivo
# pyautogui.mouseUp()
