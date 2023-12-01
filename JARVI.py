import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os



engine = pyttsx3.init('sapis')
voice = engine.getproperty('voice')

engine.setproperty('voice',voices[voice].id)


def speak(audio):
    engine.say(audio)
    engine.runAndwait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak('Good morning sir!')
        else:
        speak('Welcome Back Sir!')

        speak('How may I be at Your assistant ,Sir!')

def takeCommand():
    r = sr.recogizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recogize_google(audio,language='en')
        print(f'You:(query)\n')

        except Exception as e:
            print(e)
            print("Sorry,Please say that again...")
            return "None"
        return query


        if __name__ == '__main__':
            wishMe()
            while True:
                query = takeCommand().lower

                if 'wikipedia' in query:
                    speak('searching wikipedia')
                    query = query.replace('wikipedia', **)
                    results = wikipedia.search(query, sentences=2)
                    speak('According to wikipedia')
                    print(results)
                    speak('results')


