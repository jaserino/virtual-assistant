from datetime import datetime
import webbrowser
import pyttsx3

# creating the speak method
def speak(audio):
    engine = pyttsx3.init()
    # getting the current value of the engine property 
    voices = engine.getProperty('voices')
    # setting male or female voice [0] -male [1] -female
    engine.setProperty('voice', voices[1].id)
    # initializing va speech
    engine.say(audio)
    engine.runAndWait()

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
            tellTime()
            continue


# getting input from user and recognizing the command using speech recognition 
def recieveCommand():
    print("hello")



# simple introduction method to be called when assistant is powered on 
def Hello():
    speak("Hello, I am ava, Your desktop assistant. How may I help you?")

def tellTime(self):
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.speak(self, "The current time is "+ hour + min)
    