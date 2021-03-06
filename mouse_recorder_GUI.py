from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pyautogui
import time
import main as save_mouse
from importlib import reload
import platform


def successfully_message():
    messagebox.showinfo('Info', 'The list has been proccessed successfully')

# Save the macro

def save_file_dialog():

    # used to convert the elements of the list that are strings
    # to transform them into tuples within the JSON.

    clicks = str(save_mouse.clicks_coordinates).replace("'", "")
    time_clicks_str = str(save_mouse.time_between_clicks)
    file_name = filedialog.asksaveasfile(initialdir=os.getcwd(),
                                         filetypes=(("Json File", "*.json"),),
                                         defaultextension=".json",
                                         title="Choose a name.")
    if file_name is None:
        pass

    else:
        file_name.write(clicks + '\n')
        file_name.write(time_clicks_str)
        file_name.close()
        reload(save_mouse)

# This function opens the file with the coordinates.


def open_json():

    json_instructions = filedialog.askopenfilename(
        initialdir=os.getcwd(), filetypes=(
            ("Json file", "*.json"),), title="Choose a file.")

    if json_instructions == "":
        pass
   
    else:
        show_open_file.config(text=os.path.basename(json_instructions))
        json_instructions_read = open(json_instructions, 'r')
        lines = json_instructions_read.readlines()
        open_json.clicks_coordinates = eval(lines[0])
        open_json.time_clicks = eval(lines[1])


#  Execute the coordinates.

def macro_play():
    saved_clicks = open_json.clicks_coordinates
    time_between_clicks = open_json.time_clicks

    time.sleep(2)
    index = 0
    for i in saved_clicks:
        time.sleep(time_between_clicks[index])
        index += 1
        pyautogui.click(i)
    messagebox.showinfo('Info', 'The macro has finished')


# ---------------GUI starts-----------------------------------------------
root = Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Macro recorder')
# Change icon for different systems.
if platform.system() == "Windows":
    root.iconbitmap('mouse.ico')
 
show_open_file = Label(root, text='No open file')
show_open_file.place(x=10, y=172)

# -------------Buttons----------------------------------------------

button = Button(root, text='Open file',
                command=open_json, width=12).place(x=155, y=50)
button_run = Button(root, text='Run',
                    command=macro_play, width=12).place(x=155, y=90)
button_generate_macro = Button(
    root,
    text='Record macro', command=lambda:
        [save_mouse.main(), successfully_message()],
        width=12).place(x=40, y=50)

button_savemacro = Button(root, text='Save file',
                          command=save_file_dialog,
                          width=12).place(x=40, y=90)
root.mainloop()
