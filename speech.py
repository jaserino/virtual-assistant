from datetime import datetime
from email.mime import audio
from unittest.mock import NonCallableMagicMock
import webbrowser
import os
import speech_recognition as sr 
# importing all functions from actions file
from actions import *


# creating the request method 
def Recieve_request():
    # initialize ava by calling the hello function
    Hello()

    while(True):
        # making requests lowercase so the match in most circumstances 
        request = recieveCommand().lower()
        if "open google" in request:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "open youtube" in request:
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
            continue
        elif "open twitch" in request:
            speak("Opening Twitch")
            webbrowser.open("www.twitch.tv")
            continue
        elif "open spotify" in request:
            speak("opening spotify")
            os.startfile(r'C:\Users\Jared\AppData\Roaming\Spotify\Spotify.exe')
            continue
        elif "open league of legends" in request:
            speak("opening league of legends")
            os.startfile(r'C:\Riot Games\Riot Client\RiotClientServices.exe')
            continue
        elif "what is the time" in request:
            getTime()
            continue
        elif "what is the day" in request:
            getDay()
            continue
        elif "introduce yourself" in request:
            speak("Yes, please introduce yourself so I can learn more about you")
            continue
        elif "what is your name" in request:
            speak("I am ahva, your personal assistant")
            continue
        elif "goodbye" in request:
            speak("See you later")
            exit()
        
# getting input from user and recognizing the command using speech recognition 
def recieveCommand():
    # using the recongnizer method for speech recognition
    s = sr.Recognizer()

    # using the microphone module to record command
    with sr.Microphone() as source:
        print("listening for command")

        s.pause_threshold = 1
        audio = s.listen(source)

        try:
            print("loading...") 
            Request = s.recognize_google(audio, language='en-US')
            print(Request) 
        
        except Exception as e:
            print(e)
            speak("Im sorry, I did not understand that")
            return "None"
        
        return Request

if __name__ == '__main__':
    Recieve_request()
