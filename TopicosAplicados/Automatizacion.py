## Ejemplos extraidos del libro "Automating the boring stuff with Python" por Al Sweigart
## http://automatetheboringstuff.com/

import pyautogui

wh = pyautogui.size()
print("Mi computadora es", wh[0], "de ancho, y", wh[1], "de alto")

## mover cursor a una cierta posicion
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)

## mover cursor de cierta manera relativo a donde se encuentra
# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)
#     pyautogui.move(0, 100, duration=0.25)
#     pyautogui.move(-100, 0, duration=0.25)
#     pyautogui.move(0, -100, duration=0.25)

# posicion = pyautogui.position()
# print("la posicion de cursor es", posicion)

## Generando clicks virtuales
#pyautogui.click(100, 540, button='left')

#pyautogui.click(890, 540, button='right') ## tambien existe la funcion pyautogui.doubleClick() que simula un doble click

## Arrastrando el cursor
## programa para dibujar en Paint (windows) o paintbrush(MacOS) o GNUpaint (Linux)
# import time
# time.sleep(7) # tiempo (segundos) para abrir paint
#
# pyautogui.click() # click virtual en paint para inicializar la ventana
# distance = 300
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2) # mover a la derecha
#     distance -= change
#     pyautogui.drag(0, distance, duration=0.2) # mover abajo
#     pyautogui.drag(-distance, 0, duration=0.2) # mover a la izquierda
#     distance -= change
#     pyautogui.drag(0, -distance, duration=0.2) # mover arriba

## Scrolling con python
#pyautogui.scroll(-400) # numeros positivos suben y numeros negativos bajan

## Obtener coordenadas y colores para planear movimientos
#pyautogui.mouseInfo()

## Obtener informacion sobre la ventana activa
#fw = pyautogui.getActiveWindow()
# print(fw)
## Ahora podemos realizar comandos mas precisos en nuestra ventana
#pyautogui.rightClick(fw.left + 150, fw.top + 20, duration=0.2)
## Otros metodos para obtener informacion de ventanas son:
# pyautogui.getAllWindows() # Devuelve objeto Window para cada ventana visible en la pantalla
# pyautogui.getWindowsAt(x, y) # Devuelve objeto Window por cada ventana visble que incluya el punto (x, y)
# pyautogui.getWindowsWithTitle(title) # Devuelve objeto Window por cada ventana visible que tenga el titulo especificado

