#Original source: https://www.youtube.com/watch?v=jBxRGcDmfWA
import pyautogui, time, os
#Sleep to give us time to select the application (like web.whatsapp.com)
time.sleep(5)
#Change the folder according to the file you want to spam, the 'r' is to read the file
f = open("lotr.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")