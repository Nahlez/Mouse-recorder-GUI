import pyautogui,time,keyboard

clicks_guardados = [(892, 1051), (1567, 324), (1567, 324), (1567, 324), (1567, 324), (1567, 324), (1567, 324), (590, 816), (590, 816)]

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










