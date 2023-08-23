import pyttsx3

engine=pyttsx3.init()
voice=engine.getProperty("voices")
engine.setProperty('voice',voice[1].id)


newVoiceRate=200
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
speak("i said shutup")