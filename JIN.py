import pyttsx3 as a1
import datetime
import speech_recognition  as a2
import wikipedia as a3    


engine = a1.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[3].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour=datetime.datetime.now().hour
    if hour>=4 and hour<12:
        speak("Good Moring deep ")

    elif hour<=12 and hour>=16 :
        speak("Good Afternoon deep")

    else:
        speak("Good Evening deep")

    speak("I am JIN , How may help YOU Deep")
 
def mic():
    M=a2.Recognizer()
    with a2.Microphone() as source :
        print("listening....")
        M.pause_threshold = 0.8
        audio = M.listen(source)
    try:
        print("Recognizing...")    
        query = M.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as g:
        print("Pardon deep")
        speak("Pardon deep")
        return"none"
    return query


if __name__ == '__main__' :
    greeting()
    while True:
        query = mic()
        if 'wikipedia' in query:
            speak('Searching....')
            query = query.replace("wikipedia","")
            results = a3.summary(query,sentence=5)
            speak("According to wikipedia")
            speak(results)








