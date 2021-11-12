import pyautogui
from pynput.mouse import Listener
from pynput import mouse
import time

saved_clicks = []
time_each_click = []
time_between_clicks = []
clicks_coordinates = []

# With this function we clean the output string from Pyautogui.


def replace_and_add_item(items, old1, new1, old2, new2, old3, new3):
    new_item = items.replace(old1, new1)
    new_item = new_item.replace(old2, new2)
    new_item = new_item.replace(old3, new3)
    clicks_coordinates.append(new_item)

# With this function we detect and save mouse clicks.


def on_click(x, y, button, pressed):

   # If we put the mouse in the upper corner of the screen the loop
   # ends.

    if pressed:
        if str(pyautogui.position()) == 'Point(x=0, y=0)':
            n = False
            return n

    if not pressed:
        return False
    else:
        time.sleep(0.1)
        saved_clicks.append(pyautogui.position())
        time_each_click.append(time.time())
        print('A click was saved')


def save_lists():
    clicks = str(clicks_coordinates).replace("'", "")
    file_name = input('Choose the filename: ') + '.json'
    file_clicks = open(file_name, 'w+')
    file_clicks.write(clicks + '\n')
    file_clicks.write(str(time_between_clicks))
    file_clicks.close()


def main():

    n = True
    while n:
        with Listener(on_click=on_click) as listener:
            listener.join()

    # This line breaks the bucle.
        if str(pyautogui.position()) == 'Point(x=0, y=0)':
            n = False

    #The for loop below is to generate a list with the time interval between clicks.
    for i in range(1, len(time_each_click)):
        if time_each_click[i] != time_each_click[0]:
            x = time_each_click[i] - time_each_click[i - 1]
            time_between_clicks.append(x)
    time_between_clicks.insert(0, 1) # This insert one initial second in the list.

    for i in saved_clicks:
        replace_and_add_item(str(i), 'Point', '', 'x=', '', 'y=', '')

    print('The list has been proccessed succesfully')

# ------------------Start program-----------------------------------------

if __name__ == "__main__":
    main()
    decision = input('¿Do you want to save it? press y/n')

    if decision == 'y':
        save_lists()
