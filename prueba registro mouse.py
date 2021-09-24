import pyautogui,time,keyboard

clicks_guardados = [(891, 1049), (891, 1049), (582, 399), (582, 399), (962, 991), (1916, 0)]
tiempo_entre_clicks = [1,0.16002655029296875, 5.704802751541138, 0.15761470794677734, 6.452815055847168, 1.3998219966888428]

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




