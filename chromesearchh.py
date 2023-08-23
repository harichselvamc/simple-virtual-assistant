import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
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

def sendmail(to,content):
    server=smtplib.SMTP("'smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("testing@gmail.com","123@456")
    server.sendmail("harichselvamc@gmail.com",to,content)
    server.close()


if   __name__=="__main__":
    wishes()
    while True:
        query=takecommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "sendmail" in query:
              try:
                speak("what should i say?")
                content  =takecommand()
                to="dummy@gmail.com"  
                sendmail(to,content)
                speak("email sent successfully")    
              except Exception as e:
                speak(e)     
                speak("unable to send mail")
             
        elif "search in chrome" in query:
            speak("what you want to search")
            chromepath="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")