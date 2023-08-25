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
activationSentence = "Hey"

def speak(text, rate = 150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("How can I help?")

    with sr.Microphone() as source:
        listener.pause_threshold = 2
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

if __name__ == '__main__':
    speak('Initializing Pythriend...')

    while True:
        query = parseCommand().lower().split()

        if query[0] == activationSentence:
            query.pop(0)

            if query[0]== "say":
                if 'hello' in query:
                    speak("Hello, how are you?")
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)

        if activationSentence.lower() in query:
            print("Activation Sentence Detected")
            speak("Yes, friend?")
            query = parseCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak('Opening Youtube...')
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak('Opening Google...')
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                speak('Opening Stackoverflow...')
                webbrowser.open("stackoverflow.com")

            elif 'what time is it' in query:
                strTime = datetime.now().strftime("%H:%M:%S")
                speak(f"It is {strTime}")

            elif 'open code' in query:
                speak('Opening Visual Studio Code...')
                codePath = "C:\\Users\\Ali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                webbrowser.open(codePath)

            elif 'open spotify' in query:
                speak('Opening Spotify...')
                codePath = "C:\\Users\\Ali\\AppData\\Roaming\\Spotify\\Spotify.exe"
                webbrowser.open(codePath)

            elif 'open steam' in query:
                speak('Opening Steam...')
                codePath = "C:\\Program Files (x86)\\Steam\\Steam.exe"
                webbrowser.open(codePath)

            elif 'open epic games' in query:
                speak('Opening Epic Games...')
                codePath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
                webbrowser.open(codePath)

            elif 'open origin' in query:
                speak('Opening Origin...')
                codePath = "C:\\Program Files (x86)\\Origin\\Origin.exe"
                webbrowser.open(codePath)

            elif 'open uplay' in query:
                speak('Opening Uplay...')
                codePath = "C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\Uplay.exe"
                webbrowser.open(codePath)

            elif 'open battle net' in query:
                speak('Opening Battle Net...')
