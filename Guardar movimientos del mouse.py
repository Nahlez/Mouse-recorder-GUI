import pyautogui
from pynput.mouse import Listener
import keyboard as key2
from pynput import mouse
# Fijarse si discrimina entre click derecho e izquierdo
import time  

clicks_guardados = []
time_each_click = []
time_between_clicks = []
tiempo_list = []

new_list = []

# With this function we clean the output string from Pyautogui.
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
        print('A click was saved')
        print(clicks_guardados)
    
# ------------------Start program-----------------------------------------------
n = True        
while n == True:
    with Listener(on_click=on_click) as listener:
        listener.join()

#Esta linea corta el while 
    if str(pyautogui.position()) == 'Point(x=0, y=0)':
        n = False
    
    
diff_list = []
# El bucle for de acontinuacion nos genera el intervalo final de tiempo.
for i in range(1,len(tiempo_list)):
    if tiempo_list[i] != tiempo_list[0]:
        x = tiempo_list[i] - tiempo_list[i-1]
        diff_list.append(x)
diff_list.insert(0, 1)
print(diff_list)

for i in clicks_guardados:
    replace_and_add_item(str(i),'Point','','x=','','y=','')

clicks = str(new_list).replace("'", "")
print(new_list)
print('The list has been proccessed succesfully')
decision = input('¿Do you want to save it? press y/n')

if decision == 'y':
    file_name = input('Choose the filename: ')+'.json'
    file_clicks = open(file_name,'w+')
    file_clicks.write(clicks+'\n')
    file_clicks.write(str(diff_list))
    file_clicks.close()


