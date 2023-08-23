import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


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

def jokesss():
    speak(pyjokes.get_joke()) 
    
    
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

def screenshott():
    img=pyautogui.screenshot()
    img.save("D:\GITHUB\simple-virtual-assistant-\screenshoott.png")
    
    
    
def cpu():
    usage=str(psutil.cpu_percent)
    speak("cpu is at "+usage)
    
    battery=psutil.sensors_battery
    speak("battery is at ")
    speak(battery.percent)
    
    
    
    
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
        
        elif "logout" in query:
            os.system("shutdown - 1")
            
        elif "logout" in query:
            os.system("shutdown /s /t 1")
            
        elif "logout" in query:
            os.system("shutdown /r /t 1")
        
        elif "play songs" in query:
            song_dir="D:\music"
            
            song=os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,song[0]))
            
        elif "Remember" in query:
            speak("what should i remember")
            data=takecommand()
            speak("you said that"+data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
            
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that "+remember.read())
            
        elif "screenshot" in query:
            screenshott()
            speak("done")
            
        elif "cpu" in query:
            cpu()
            
        elif "jokes" in query:
            jokesss()
            
            