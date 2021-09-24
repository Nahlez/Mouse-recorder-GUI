import pyautogui, time,random
from pynput.mouse import Listener
import keyboard as key2
from pynput import mouse


import time  


clicks_guardados = []
time_each_click = [3,]
time_between_clicks = []
tiempo_list = []



new_list = []
def replace_and_add_item(items,old1,new1,old2,new2,old3,new3):
    new_item = items.replace(old1, new1)
    new_item = new_item.replace(old2, new2)
    new_item = new_item.replace(old3, new3)
    new_list.append(new_item)

# Con esta funcion detectamos y guardamos los clicks del mouse.
def on_click(x, y, button, pressed):

    # Si ponemos el mouse en la esquina superior de la pantalla el loop termina.
    if pressed:
        if str(pyautogui.position()) == 'Point(x=0, y=0)':
            n = False
            return n         
        
    if not pressed:
        return False
    else:
        time.sleep(0.1)
        clicks_guardados.append(pyautogui.position())
        tiempo_list.append(time.time())
        print(tiempo_list)
        print(pyautogui.position())
        print('se guardo un click')
        print(clicks_guardados)
    
    
n = True        
while n == True:
    with Listener(on_click=on_click) as listener:
        listener.join()

    if str(pyautogui.position()) == 'Point(x=0, y=0)':
        n = False
    
    
diff_list = []
for i in range(1,len(tiempo_list)):
    if tiempo_list[i] != tiempo_list[0]:
        x = tiempo_list[i] - tiempo_list[i-1]
        diff_list.append(x)

print(diff_list)

#while True:
       #elif keyboard.is_pressed('x'):
        #mensaje = ' aca va algo del teclado'
        #clicks_guardados.append(str(pyautogui.position())+mensaje)
        #print(mensaje)
        #time.sleep(0.5)
    #else:
        #continue


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
