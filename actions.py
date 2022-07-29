import datetime
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

# simple introduction method to be called when assistant is powered on 
def Hello():
    speak("Hello, I am ahva, Your desktop assistant. How may I help you?")

# tell time function gets the user the time 
def getTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    
    speak( "The current time is "+ hour + min)

# getting the day of the week
def getDay():
    day = datetime.datetime.today().weekday()+1 
    day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if day in day_dict.keys():
        current_day = day_dict[day]
        print(current_day)
        speak("Today is " + current_day)