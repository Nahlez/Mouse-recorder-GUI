import pyautogui,time,keyboard

clicks_guardados = [(959, 923), (1802, 62), (1473, 196), (961, 932)]

time.sleep(2)
while True:
    for i in clicks_guardados:
        time.sleep(3) # You can select the seconds between the clicks
        pyautogui.click(i)
        time.sleep(3)


    #You can intervenir en un click con el codigo de abajo

    '''if i == (valorX , ValorY):
        pyautogui.write('chrome')
        pyautogui.hotkey('enter')'''










