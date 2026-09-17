import voice

while True:

    text = voice.listen(5)

    if len(text.strip()) > 2:
        print("\nYou said:", text)