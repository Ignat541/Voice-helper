import pyttsx3
import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    print(words)
    engine.runAndWait()


talk("Hi, my name is Eva, ask me something")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        print("Talk")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)

        try:
            zadanie = r.recognize_google(audio).lower()
            print('You told: ' + zadanie)
        except sr.UnknownValueError:
            talk("I didn't understand you, repeat one more time please.")
            zadanie = command()
        return zadanie

def makeSomething(zadanie):
    if 'what is the weather today' in zadanie:
        talk('Wait a moment')
        url = 'https://www.google.com/search?q=weather&rlz=1C1CHBD_ruBY920BY920&oq=weather&aqs=chrome..69i57j0i402j0i131i433i512l2j46i433i512j0i433i512j0i512j69i60.1210j0j7&sourceid=chrome&ie=UTF-8'
        webbrowser.open(url)
    elif 'wanna some music' in zadanie:
        talk('Be ready to dance')
        url = 'https://www.youtube.com/watch?v=5NV6Rdv1a3I&ab_channel=DaftPunkVEVO'
        webbrowser.open(url)
    elif 'stop' in zadanie:
        talk('No problem')
        sys.exit()

while True:
    makeSomething(command())