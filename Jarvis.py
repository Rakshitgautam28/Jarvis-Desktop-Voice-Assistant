import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition 
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi 'Rakshit', I am Jarvis, How can i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except exception as e:
        print("Say that again Please...")
        return "None"
    return query
    
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rakshitgautam2000@gmail.com','!RGrakshit28')
    server.sendmail('rakshitgautam2000@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoring to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'play music' in query:
            music_dir='D:\\Music\\2020'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'who developed you' in query:
            speak("i was developed by Rakshit Gautam") 
        elif 'who is tanisha sharma' in query:
            print("According to me, Tanisha Sharma is a stupid girl")
            speak("According to me, Tanisha Sharma is a stupid girl")
        elif 'who is suman sharma' in query:
            print("According to me, suman Sharma is a mother of rakshit gautam as well as beautiful soul lives in ambala along with her family names Gautams")
            speak("According to me, suman Sharma is a mother of rakshit gautam as well as beautiful soul lives in ambala along with her family names Gautams")
        elif 'who is sachin gautam' in query:
            print("According to me, sachin gautam is a brother of rakshit gautam as well as handsome guy who lives in ambala along with her family names Gautams")
            speak("According to me, sachin gautam is a brother of rakshit gautam as well as handsome guy who lives in ambala along with her family names Gautams")
        elif 'who is suresh sharma' in query:
            print("According to me, suresh sharma is a father of rakshit gautam. He loves playing carrom board and uno. He lives in ambala along with her family names Gautams")
            speak("According to me, suresh sharma is a father of rakshit gautam. He loves playing carrom board and uno. He lives in ambala along with her family names Gautams")

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open python' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\pythonw.exe "
            os.startfile(os.codepath)
        elif 'send an email':
            try:
                def remove(string):
                    return string.replace(" ","")
                speak("who you want to send")
                temp = takeCommand()
                to=remove(temp.lower())
                speak("What should i say?")
                content = takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except exception as e:
                speak("Sorry i cant do it right now")
