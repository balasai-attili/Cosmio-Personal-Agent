import automation
import commands
import memory
import re
import browser
import agent
import desktop
import launcher
import state
def process(command):
    
    command = command.lower().strip()

    command = command.replace(".", "")
    command = command.replace(",", "")
    command = command.replace("?", "")
    command = command.replace("!", "")

    command = command.lower()

    if command == "hello":
        return "Hello! How can I help you?"

    elif command.startswith("close"):

        app_name = command.replace(
            "close ",
            "",
            1
        ).strip()

        if not app_name:
            return "close requires an application name."

        if launcher.close_app(app_name):

            return f"Anti-Nexus protocol complete. {app_name} has been terminated."

        return f"{app_name} does not appear to be running."
    
    elif command.startswith("open "):

        app_name = command.replace(
            "open ",
            ""
        ).strip()

        if launcher.open_app(app_name):

            return f"Opening {app_name}"

        return f"I couldn't find {app_name}"
    
    elif "execute void protocol" in command.lower():

        state.set_state(
            state.DORMANT
        )

        return (
            "Void Protocol acknowledged. "
            "Entering dormant state. "
            "Returning to singularity."
        )
    
    elif command.startswith("open chatgpt and ask"):

        prompt = command.replace(
            "open chatgpt and ask",
            ""
        ).strip()

        agent.set_action({
            "type": "chatgpt",
            "prompt": prompt
        })

        return f"""
    Prepared prompt:

    {prompt}

    Say SEND to continue.
    """

    elif command == "send":

        print("DEBUG: SEND BLOCK REACHED")

        action = agent.get_action()

        print("DEBUG ACTION:", action)

        if action:

            print("DEBUG: OPENING CHATGPT")
            browser.open_chatgpt()

            print("DEBUG: WAITING")
        
            print("DEBUG: TYPING")
            browser.type_text(
                action["prompt"]
            )

            print("DEBUG: FINISHED TYPING")

            return "Prompt typed into ChatGPT."

        return "No pending action."
    
    elif command == "send now":

        browser.press_enter()

        agent.clear_action()

        return "Prompt submitted."
    
    elif command.startswith("remember "):

        try:
            data = command.replace("remember ", "")

            key, value = data.split(" is ", 1)

            memory.remember(
                key.strip(),
                value.strip()
            )

            return f"I will remember that {key} is {value}"

        except:
            return "Use format: remember something is value"

    elif command.startswith("search google for"):

        query = command.replace(
            "search google for",
            ""
        ).strip()

        query = query.replace(" ", "+")

        automation.open_website(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for {query}"

    elif command.startswith("search youtube for"):

        query = command.replace(
            "search youtube for",
            ""
        ).strip()

        query = query.replace(" ", "+")

        automation.open_website(
            f"https://www.youtube.com/results?search_query={query}"
        )

        return f"Searching YouTube for {query}"
    
    elif command == "":
        return "Stopping COSMIO"
    
    elif command.startswith("what is "):

        key = command.replace(
            "what is ",
            ""
        ).strip()

        result = memory.recall(key)

        if key == "my name" and result != "I don't know that yet.":
            return f"Your name is {result}"

        return result
    def clean_response(text):

        # Remove markdown symbols
        text = re.sub(r'[*_`#>\[\]\(\)]', '', text)

        # Remove multiple spaces
        text = re.sub(r'\s+', ' ', text)

        # Remove leading/trailing spaces
        text = text.strip()

        return text
    
    return "I don't understand that command yet."