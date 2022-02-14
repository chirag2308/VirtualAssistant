import subprocess
import speech_recognition as sr
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import os
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:

        talk("Good Morning Sir !")



    elif hour >= 12 and hour < 18:

        talk("Good Afternoon Sir !")



    else:

        talk("Good Evening Sir !")

    assname = ("Octave 2 point 0")

    talk("I am your virtual Assistant")

    talk(assname)


def usrname():
    talk("Checking your internet connection\n system online in\n 1\n 2\n 3\n creating a user environment for you\n What should i call you")

    uname = take_command()

    talk("Welcome ")

    talk(uname)

    talk("How can i Help you, Sir")



def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizing...")

        command = r.recognize_google(audio, language='en-in')

        print(f"User said: {command}\n")



    except Exception as e:

        print(e)

        print("Unable to Recognize your voice.")

        return "None"

    return command


def run_octave():
    wishMe()
    usrname()
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is' + time)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'how are you' in command:
            talk('i am fine, and what about you')

        elif 'who created you' in command:
            talk('i am created by chirag varshney')

        elif 'date' in command:\
            talk('sorry, I have a headache')

        elif 'joke' in command:
            talk(pyjokes.get_jokes())


        elif 'shutdown system' in command:
            talk("Hold On a Sec ! Your system is on its way to shut down")
            talk('i am going to terminate all the processing of the computer')
            talk('count down start')
            talk('3\n  2\n   1\n.....system shutdown successfully')
            break
            exit()

        elif 'bye' in command:
            talk('bye have a good day')
            break
            exit()

        else:
            talk('please say the command again')

run_octave()