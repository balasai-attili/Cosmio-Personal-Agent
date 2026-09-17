from click import command

import voice
import brain
import state

awake = False

while True:

    current_state = state.get_state()
    
    if current_state == state.DORMANT:

        if "mio" in command.lower():

            state.set_state(
                state.ACTIVE
            )

            print(
                "\nCOSMIO: Online and ready."
            )

        continue
    
    command = voice.listen(5)

    command = command.strip().lower()

    if not command:
        continue

    # Ignore garbage
    if command in [
        "you",
        "okay",
        "uh",
        "um",
        "a",
        "e",
        "o"
    ]:
        continue

    # Wake mode
    if not awake:

        if "mio" in command:

            awake = True

            print(
                "\nCOSMIO: Online and ready."
            )

        continue

    # Sleep mode
    if "execute void protocol" in command:

        print(
            "\nCOSMIO: Void Protocol acknowledged."
        )

        print(
            "COSMIO: Entering dormant state."
        )

        print(
            "COSMIO: Returning to singularity."
        )

        awake = False

        continue

    print("\nYou:", command)

    response = brain.process(command)

    print("COSMIO:", response)