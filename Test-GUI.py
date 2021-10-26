from tkinter import *
from tkinter import filedialog
import os
import pyautogui
import time
import keyboard
import Savemousemovements as savemouse

root = Tk()

root.geometry('300x300')



def open_json():
    json_instructions = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("Json File", "*.json"), ("All Files", "*.*")),
                           title="Choose a file.")
    json_instructions = open(json_instructions,'r')
    lines = json_instructions.readlines()
    open_json.clicks_coordenates = eval(lines[0])
    open_json.time_clicks = eval(lines[1])

def macro_play():
    saved_clicks = open_json.clicks_coordenates
    time_between_clicks = open_json.time_clicks

    time.sleep(0.8)
    index = 0
    for i in saved_clicks:
        time.sleep(time_between_clicks[index]) 
        index += 1 
        pyautogui.click(i)

button = Button(root, text='Open file', command=open_json).pack()
button_run = Button(root, text='Run', command=macro_play).pack()
button_savemouse = Button(root, text='Generate Macro', command=savemouse.main).pack()


# Here starts the script "Macro play test".



root.mainloop()