from datetime import datetime
from email.mime import audio
import webbrowser
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
        elif "what is the time" in request:
            getTime()
            continue
        elif "what is the day" in request:
            getDay()
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
