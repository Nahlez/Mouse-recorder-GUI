import pyautogui, time,random,keyboard
clicks_guardados = []

while True:
    if keyboard.is_pressed('c'):
        time.sleep(0.5)
        clicks_guardados.append(pyautogui.position())
        print('se guardo un click')
    elif keyboard.is_pressed('f'):
        break

    elif keyboard.is_pressed('x'):
        mensaje = ' aca va algo del teclado'
        clicks_guardados.append(str(pyautogui.position())+mensaje)
        print(mensaje)
        time.sleep(0.5)
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

new_list = str(new_list)
new_list = new_list.replace("'","")
print(new_list)

input()
