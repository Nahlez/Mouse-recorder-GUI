from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import pyautogui
import time
import Save_mouse_movements as savemouse


def succesfully_message():
    messagebox.showinfo('Info', 'The list has been proccessed succesfully')

#Save the Macro

def save_file_dialog():

    # The following line is used to convert the elements of the list that are strings 
    # and transform them into tuples within the JSON.

    clicks = str(savemouse.new_list).replace("'", "")
    file_name = filedialog.asksaveasfile(initialdir=os.getcwd(),
                filetypes=(("Json File", "*.json"),),
                            defaultextension=".json",
                           title="Choose a name.")
    if file_name == None:
        pass
    
    else:
        file_name.write(clicks+'\n')
        file_name.write(str(savemouse.diff_list)) #Cambiar nombre de variable por otra mas legible # Translate comment
        file_name.close()

#This function opens the file with the coordenates.
def open_json():

    json_instructions = filedialog.askopenfilename(initialdir=os.getcwd(),
                         filetypes=(("Json file", "*.json"),),
                         title="Choose a file.")

    if json_instructions == "":
        pass
    else:
        show_open_file.config(text=os.path.basename(json_instructions))
        json_instructions_read = open(json_instructions,'r')
        lines = json_instructions_read.readlines()
        open_json.clicks_coordenates = eval(lines[0])
        open_json.time_clicks = eval(lines[1])

       

#  Execute the coordenates.

def macro_play():
    saved_clicks = open_json.clicks_coordenates
    time_between_clicks = open_json.time_clicks

    time.sleep(2)
    index = 0
    for i in saved_clicks:
        time.sleep(time_between_clicks[index]) 
        index += 1 
        pyautogui.click(i)
    messagebox.showinfo('Info','The macro has finished')


#---------------GUI starts-----------------------------------------------
root = Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Macro recorder')

show_open_file = Label(root,text='Anything open')
show_open_file.place(x=10,y=172)

button = Button(root, text='Open file', 
         command=open_json, width=12).place(x=155,y=50)
button_run = Button(root, text='Run', 
             command=macro_play,width=12).place(x=155,y=90)
button_generate_macro = Button(root, text='Record Macro', 
                       command=lambda:[savemouse.main(),succesfully_message()],
                       width=12).place(x=40,y=50) 

button_savemacro = Button(root, text='Save file', command= save_file_dialog
                   ,width=12).place(x=40,y=90) 




root.mainloop()