import pyautogui
import time

repeticiones = int(input("How many times do you want to press the button?"))

delay = int(input("How many milliseconds do you want to wait in between each click? "))

boton = int(input("Choose 1 (Left) or 2 (Right) to select the mouse button."))

print("You have five seconds to refocus the area of your click")

time.sleep(5)

for i in range(0,repeticiones): 

	if boton == 1:       
		pyautogui.click(button='left')

	elif boton == 2:
		pyautogui.click(button='right')

time.sleep(delay/1000)

print("Autoclicker finished.\n")


