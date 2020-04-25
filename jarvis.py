import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random as rd

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Eedith...How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output!
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"Prakhar said: {query}\n")
        speak(f"Prakhar said...: {query}\n")
        speak("Sure!")
            
        

    except Exception as e:
        print(e)

        print("Say that again please...\n")
        # speak("Say that again please...\n")
        return "None"
    return query
        

if __name__ == "__main__":
    wishMe()
    x=True
    while x:
        query=takeCommand().lower()
        #Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Opening...Youtube!")
            wb.open("youtube.com")

        elif 'open google' in query:
            speak("Opening...Google!")
            wb.open("google.com")

        elif 'shutdown' in query:
            speak("Shutting Down...")
            break

        elif 'play fifa' in query or "open fifa" in query:
            os.startfile(("E:\\Games\\FIFA19\\FIFA 19\\FIFA19.exe"))

        elif 'play hollow knight' in query or "open hollow knight" in query:
            os.startfile(("E:\\Games\\Hollow Knight\\hollow_knight.exe"))

        elif 'play tomb raider' in query or 'open tomb raider' in query:
            os.startfile("C:\\Users\\Prakhar\\Desktop\\ROTTR.lnk")

        elif 'play cs go' in query or "open cs go" in query:
            os.startfile("C:\\Users\\Prakhar\\Desktop\\Counter-Strike Global Offensive.url")

        # elif 'play music' or 'open music' in query:
        #     music_dir="E:\\Music"
        #     songs=os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, songs[rd.randrange(len(songs))]))