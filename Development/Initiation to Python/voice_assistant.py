import pyttsx3
import speech_recognition as sr
import re

"""
To know the voices available:

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print(f"{i}: {voice.name} | {voice.id} | {voice.languages}")
"""

def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    return engine


def say_hello(engine):
    engine.say("Hello, what's your name?")
    engine.runAndWait()


def recognize_voice(r):
    with sr.Microphone() as source:
        print("You can talk")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="en-EN")
    return text


def identify_name(text):
    name = None
    patterns = ["my name is ([A-Za-z]+)",
                "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)
        except IndexError:
            print("You don't have name...")
        return name


def main():
    engine = initialize_engine()

    say_hello(engine)

    r = sr.Recognizer()

    text = recognize_voice(r)
    name = identify_name(text)
    if name:
        engine.say("Nice to meet you {}".format(name))
    else:
        engine.say("")
    engine.runAndWait()


if __name__ == "__main__":
    main()