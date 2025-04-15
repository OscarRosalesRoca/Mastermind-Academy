import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear_me():
    with sr.Microphone() as source:
        print("Capturing voice...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es-ES")
            print("I have understood: {}".format(text))
            return  text
        except sr.UnknownValueError:
            return

if __name__ == "__main__":
    speak("prueba")
    print(hear_me())