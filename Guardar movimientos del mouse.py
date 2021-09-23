import pyautogui, time,random
from pynput.mouse import Listener
from pynput import keyboard
import keyboard as key2

clicks_guardados = []



def on_click(x, y, button, pressed):

    if pressed:
        time.sleep(0.1)
        clicks_guardados.append(pyautogui.position())
        print('se guardo un click')
        print(clicks_guardados)
    elif key2.wait('f'):
        return False
        
    
    
        

with Listener(on_click=on_click) as listener:
    listener.join()


while True:
    print('hola')
    if keyboard.is_pressed('c'):
        pass
    elif keyboard.is_pressed('f'):
        break

    #elif keyboard.is_pressed('x'):
        #mensaje = ' aca va algo del teclado'
        #clicks_guardados.append(str(pyautogui.position())+mensaje)
        #print(mensaje)
        #time.sleep(0.5)
    else:
        continue

new_list = []
#Delete Unwished characters from first list.
def replace_and_add_item(items,old1,new1,old2,new2,old3,new3):
    new_item = items.replace(old1, new1)
    new_item = new_item.replace(old2, new2)
    new_item = new_item.replace(old3, new3)
    new_list.append(new_item)
for i in clicks_guardados:
    replace_and_add_item(str(i),'Point','','x=','','y=','')

clicks = str(new_list).replace("'", "")
print(new_list)
print('Se ha procesado la lista satisfactoriamente')
decision = input('¿Deseas guardarla ? press y/n')

if decision == 'y':
    file_name = input('Choose the filename: ')+'.txt'
    file_clicks = open(file_name,'w+')
    file_clicks.write(clicks)
    file_clicks.close()
print(new_list)

input()
