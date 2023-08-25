from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# Speech Recognition Engine Initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
activationSentence = "Hey Pythriend"

def speak(text, rate = 150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("How can I help, Ali?")

    with sr.Microphone() as source:
        listener.pause_threshold = 3
        input_speech = listener.listen(source)

        try:
            print("Recognizing...")
            query= listener.recognize_google(input_speech, language='en_gb')
            print(f"User said: {query}\n")
        except Exception as exception:
            print("Say that again please...")
            speak("Say that again please...")
            print("Exception: " + str(exception))
            return "None"
        return query


