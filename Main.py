import speech
import memory
import commands

print("Speech module loaded from:")
print(speech.__file__)

def cosmio():
    print("=================================")
    print("COSMIO Activated")
    print("Type 'exit' to close")
    print("=================================")

    while True:
        user_command = input("You: ").lower()

        if user_command == "hello":
            print("COSMIO: Hello! How can I help you?")
            speech.speak("Hello! How can I help you?")

        elif user_command == "who are you":
            print("COSMIO: I am COSMIO, your personal AI assistant.")
            speech.speak("I am COSMIO, your personal AI assistant.")

        elif user_command == "test voice":
            print("COSMIO: Testing voice")
            speech.speak("Testing voice. Can you hear me?")

        elif user_command == "open notepad":
            print("COSMIO: Opening Notepad")
            speech.speak("Opening Notepad")
            commands.open_notepad()

        elif user_command == "open calculator":
            print("COSMIO: Opening Calculator")
            speech.speak("Opening Calculator")
            commands.open_calculator()

        elif user_command == "open chrome":
            print("COSMIO: Opening Chrome")
            speech.speak("Opening Chrome")
            commands.open_chrome()

        elif user_command == "open downloads":
            print("COSMIO: Opening Downloads")
            speech.speak("Opening Downloads")
            commands.open_downloads()

        elif user_command == "open documents":
            print("COSMIO: Opening Documents")
            speech.speak("Opening Documents")
            commands.open_documents()

        elif user_command == "open desktop":
            print("COSMIO: Opening Desktop")
            speech.speak("Opening Desktop")
            commands.open_desktop()

        elif user_command.startswith("remember "):
            try:
                data = user_command.replace("remember ", "")
                key, value = data.split(" is ", 1)

                memory.remember(key.strip(), value.strip())

                print(f"COSMIO: I will remember that {key} is {value}")
                speech.speak(f"I will remember that {key} is {value}")

            except Exception as e:
                print("Error:", e)
                speech.speak("Sorry, I encountered an error.")

        elif user_command.startswith("what is "):
            key = user_command.replace("what is ", "").strip()

            result = memory.recall(key)

            if result != "I don't know that yet.":

                if key == "my name":
                    response = f"Your name is {result}"
                else:
                    response = f"{key} is {result}"

                print("COSMIO:", response)
                speech.speak(response)

            else:
                print("COSMIO: I don't know that yet.")
                speech.speak("I don't know that yet.")

        elif user_command == "exit":
            print("COSMIO: Shutting down.")
            speech.speak("Shutting down")
            break

        else:
            print("COSMIO: I don't understand that command.")
            speech.speak("I don't understand that command.")

cosmio()