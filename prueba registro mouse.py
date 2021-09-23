import pyautogui,time,keyboard

clicks_guardados = [(23, 1053), (1232, 859), (908, 955), (1272, 893), (1543, 656), (1919, 0)]

time.sleep(1)
while True:
    for i in clicks_guardados:
        time.sleep(3) # You can select the seconds between the clicks
        pyautogui.click(i)
        time.sleep(3)


    #You can intervenir en un click con el codigo de abajo

    '''if i == (valorX , ValorY):
        pyautogui.write('chrome')
        pyautogui.hotkey('enter')'''










