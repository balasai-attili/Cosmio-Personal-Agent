import speech_recognition as sr

print("Microphones found:")

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")