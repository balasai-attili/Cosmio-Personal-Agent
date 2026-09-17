import webbrowser
import pyautogui
import time


def open_website(url):
    try:
        webbrowser.open(url)
        return True
    except Exception as e:
        print("Error:", e)
        return False


def wait(seconds):
    time.sleep(seconds)


def type_text(text):
    pyautogui.write(
        text,
        interval=0.03
    )


def press_enter():
    pyautogui.press("enter")


def press_key(key):
    pyautogui.press(key)


def hotkey(*keys):
    pyautogui.hotkey(*keys)


def click():
    pyautogui.click()


def right_click():
    pyautogui.rightClick()


def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def scroll_up(amount=500):
    pyautogui.scroll(amount)


def scroll_down(amount=500):
    pyautogui.scroll(-amount)