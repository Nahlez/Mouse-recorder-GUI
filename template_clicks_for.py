import pyautogui
import time
import keyboard

saved_clicks = []  # Paste here the first list in the JSON File.
time_between_clicks = []  # Paste here the second list in the JSON File.
index = 0
for i in saved_clicks:
    # You can select the seconds between the clicks
    time.sleep(time_between_clicks[index])
    index += 1
    pyautogui.click(i)


# For example, you can intervene in one click with the code below:
# (Put it inside of one for loop)

#  if i == (valueX , ValueY):
#      pyautogui.write('Hello my friend!')
#      pyautogui.hotkey('enter')



