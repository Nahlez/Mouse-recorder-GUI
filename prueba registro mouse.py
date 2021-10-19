import pyautogui,time,keyboard

clicks_guardados = [(769, 1065), (68, 7), (636, 1062), (586, 227), (586, 227), (578, 402), (578, 402), (954, 952), (575, 723), (575, 723), (613, 327), (613, 327), (583, 231), (583, 230), (960, 983)]
tiempo_entre_clicks = [1, 3.936110734939575, 7.390092372894287, 11.06445026397705, 0.15624237060546875, 4.861378192901611, 0.13982391357421875, 4.335890769958496, 2.0194270610809326, 0.1247258186340332, 6.86431622505188, 0.1404862403869629, 13.05617380142212, 0.12413167953491211, 17.069056749343872]

time.sleep(0.8)
index = 0
for i in clicks_guardados:
    time.sleep(tiempo_entre_clicks[index]) # You can select the seconds between the clicks
    index += 1 
    pyautogui.click(i)


    #You can intervenir en un click con el codigo de abajo

    '''if i == (valorX , ValorY):
        pyautogui.write('chrome')
        pyautogui.hotkey('enter')'''

# Tal vez podria guardar en un diccionario el tiempo entre cada click para simular esto tamb



# Tipo que en cada click hecho guarde el tiempo y desp lo reste con el que sigue.




