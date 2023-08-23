import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
    

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
    
    
    
def wishes():
    speak("welcome back hari")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour <=12:
        speak("good morning")
    elif hour>=12 and hour < 18:
        speak("Good afternoon")
    elif hour>=18 and hour<=20:
        speak("Good evening")
    else:
        speak("Good Night")
    
    speak("khukoo at your service, are you ok ")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')  # Recognize speech using Google Web Speech API
        print(f"You said: {query}")
    except Exception as e:
        print(e)
        print("Sorry, I didn't catch that. Please say that again.")
        return "None"
    
    return query



takecommand()