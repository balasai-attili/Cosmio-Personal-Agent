import tkinter as tk

import commands
import speech
import memory


def send_message():

    user_text = input_box.get().lower()

    if user_text.strip() == "":
        return

    chat_box.insert(tk.END, f"You: {user_text}\n")

    # Greetings

    if user_text == "hello":
        response = "Hello! How can I help you?"
        speech.speak(response)

    elif user_text == "who are you":
        response = "I am COSMIO, your personal AI assistant."
        speech.speak(response)

    # Applications

    elif user_text == "open chrome":
        response = "Opening Chrome"
        speech.speak(response)
        commands.open_chrome()

    elif user_text == "open notepad":
        response = "Opening Notepad"
        speech.speak(response)
        commands.open_notepad()

    elif user_text == "open calculator":
        response = "Opening Calculator"
        speech.speak(response)
        commands.open_calculator()

    # Folders

    elif user_text == "open downloads":
        response = "Opening Downloads"
        speech.speak(response)
        commands.open_downloads()

    elif user_text == "open documents":
        response = "Opening Documents"
        speech.speak(response)
        commands.open_documents()

    elif user_text == "open desktop":
        response = "Opening Desktop"
        speech.speak(response)
        commands.open_desktop()

    # Memory System

    elif user_text.startswith("remember "):

        try:
            data = user_text.replace("remember ", "")
            key, value = data.split(" is ", 1)

            memory.remember(key.strip(), value.strip())

            response = f"I will remember that {key} is {value}"

            speech.speak(response)

        except:
            response = "Use format: remember something is value"
            speech.speak(response)

    elif user_text.startswith("what is "):

        key = user_text.replace("what is ", "").strip()

        result = memory.recall(key)

        if key == "my name" and result != "I don't know that yet.":
            response = f"Your name is {result}"

        else:
            response = result

        speech.speak(response)

    # Unknown Command

    else:
        response = "I don't understand that command."
        speech.speak(response)

    chat_box.insert(tk.END, f"COSMIO: {response}\n\n")

    chat_box.see(tk.END)

    input_box.delete(0, tk.END)


# Main Window

root = tk.Tk()

root.title("COSMIO")
root.geometry("700x500")

# Title

title = tk.Label(
    root,
    text="COSMIO",
    font=("Arial", 28, "bold")
)

title.pack(pady=10)

# Status

status = tk.Label(
    root,
    text="Status: Online"
)

status.pack()

# Chat Area

chat_box = tk.Text(
    root,
    height=20,
    width=75
)

chat_box.pack(pady=10)

chat_box.insert(tk.END, "COSMIO: Online and ready.\n\n")

# Input Area

input_frame = tk.Frame(root)

input_frame.pack()

input_box = tk.Entry(
    input_frame,
    width=50
)

input_box.pack(
    side=tk.LEFT,
    padx=10
)

# Press Enter to Send

input_box.bind(
    "<Return>",
    lambda event: send_message()
)

# Send Button

send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message
)

send_button.pack(side=tk.LEFT)

root.mainloop()