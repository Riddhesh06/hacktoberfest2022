import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(year)
    speak(month)

def wishme():
    speak("Welcome Commander")
    time_()

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour<12:
        speak("Good Morning Commander!")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon Commander!")
    elif hour >= 18 and hour<24:
        speak("Good Evening Commander")
    else:
        speak("Good Night Commander")
    
    speak("Jarvis at your service. How may i help you sir?")

def TakeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Could you repeat please.....?")
        return "none"
    return query 

TakeCommand()
