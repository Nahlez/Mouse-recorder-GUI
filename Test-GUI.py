from tkinter import *
from tkinter import filedialog
import os

root = Tk()

root.geometry('300x300')

def open_json():
    json_instructions = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=(("Json File", "*.json"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    json_instructions = open(json_instructions,'r')
    lines = json_instructions.readlines()
    clicks_coordenates = lines[0]
    time_clicks = lines[1]

    print(clicks_coordenates, time_clicks)

open_json()
root.mainloop()