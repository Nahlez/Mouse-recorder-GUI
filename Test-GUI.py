from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pyautogui
import time
import keyboard
import Savemousemovements as savemouse



def open_json():
    json_instructions = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("Json File", "*.json"),),
                           title="Choose a file.")
    if json_instructions == "":
        pass
    else:
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

root = Tk()

root.geometry('400x200')
root.title('Macro recorder')


button = Button(root, text='Open file', command=open_json).pack()
button_run = Button(root, text='Run', command=macro_play).pack()
button_generatemacro = Button(root, text='Generate Macro', command=savemouse.main).pack()
button_savemacro = Button(root, text='Save Macro', command= savemouse.save_lists).pack()




root.mainloop()