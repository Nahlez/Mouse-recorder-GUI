from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pyautogui
import time
import keyboard
import Savemousemovements as savemouse

def save_file_dialog():
    clicks = str(savemouse.new_list).replace("'", "")
    file_name = filedialog.asksaveasfile(initialdir=os.getcwd(), filetypes=(("Json File", "*.json"),),
                           title="Choose a file.")
    print("testo------------", file_name)
    file_name.write(clicks+'\n')
    file_name.write(str(savemouse.diff_list))
    file_name.close()


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
#---------------GUI starts-----------------------------------------------

root.geometry('350x200')
root.title('Macro recorder')

button = Button(root, text='Open file', command=open_json).place(x=60,y=50)
button_run = Button(root, text='Run', command=macro_play).place(x=60,y=90)
button_generatemacro = Button(root, text='Generate Macro', command=savemouse.main).place(x=140,y=50)
#button_savemacro = Button(root, text='Save Macro', command= savemouse.save_lists).place(x=140,y=90)
button_savemacro = Button(root, text='Save Macro', command= save_file_dialog).place(x=140,y=90)


root.mainloop()