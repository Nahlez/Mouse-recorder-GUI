from tkinter import *
from tkinter import filedialog
import os
import pyautogui
import time
import keyboard



root = Tk()

root.geometry('300x300')

def open_json():
    json_instructions = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("Json File", "*.json"), ("All Files", "*.*")),
                           title="Choose a file.")
    json_instructions = open(json_instructions,'r')
    lines = json_instructions.readlines()
    open_json.clicks_coordenates = eval(lines[0])
    open_json.time_clicks = eval(lines[1])

    
open_json()

# Here starts the script "Macro play test".

saved_clicks = open_json.clicks_coordenates
time_between_clicks = open_json.time_clicks

time.sleep(0.8)
index = 0
for i in saved_clicks:
    time.sleep(time_between_clicks[index]) 
    index += 1 
    pyautogui.click(i)



root.mainloop()