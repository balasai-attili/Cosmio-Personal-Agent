import webbrowser
import pyautogui
import time

def open_chatgpt():
    webbrowser.open("https://chatgpt.com")

def type_text(text):
    import time
    import pyautogui

    print("CLICK CHATGPT MESSAGE BOX NOW")

    time.sleep(10)

    pyautogui.write(text, interval=0.05)

def press_enter():
    pyautogui.press("enter")