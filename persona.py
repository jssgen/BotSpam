import pyautogui
import webbrowser
import time

message = input("mensagem")
repeats  = int(input("quantas vezes?"))
delay = int(input("delay"))

isLoaded = input("aperte enter quando o discord estiver logado")

print("você tem 5 segundos antes de começar")

time.sleep(5)

for i in range (0, repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
        
    time.sleep(delay/1000)
    
print("Done\n")