import os

def open_notepad():
    os.system("start notepad")

def open_calculator():
    os.system("start calc")

def open_chrome():
    os.system("start chrome")

def open_downloads():
    os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))

def open_documents():
    os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))

def open_desktop():
    os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))