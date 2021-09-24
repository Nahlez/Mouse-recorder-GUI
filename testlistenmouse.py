import pyautogui, time,random
from pynput.mouse import Listener
import keyboard as key2


clicks_guardados = []



def on_click(x, y, button, pressed):

    if pressed:
        time.sleep(0.1)
        clicks_guardados.append(pyautogui.position())
        print(pyautogui.position())
        print('se guardo un click')
        print(clicks_guardados)
    if not pressed:
        return False
  
    
    
n = True        
while n == True:
    with Listener(on_click=on_click) as listener:
        listener.join()

    if str(pyautogui.position()) == 'Point(x=0, y=0)':
        n = False
    
    