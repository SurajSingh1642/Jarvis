from __future__ import print_function
import sys
import pyaudio
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import wikipedia
from random import seed
from random import randint
import psutil
import smtplib
import PyPDF2



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[2].id)




#Dictionary for emails
emails = {'name1': 'email1@gmail.com', 'name2': 'email2@gmail.com'}


#Dictionary for chat module
dict=  {"hello" :"hey","hi" : "hey", "hey": "hey", "bye": "goodbye", "goodbye": "goodbye", "talk to you later":"goodbye", "how are you" : "i am fine, how are you", 
"i am fine": "good to know", "i am good": "good to know", "what can you do for me": "ask away", "i want to talk to you" : "i am glad", "you are amazing" : "thankyou so are you", 
"do you love me" : "indeed", "i love you": "i know"," i hate you" : "please dont", "can you help me" : "that's why i am here", "what's your name" : "you can call me amazing",
"you are beautiful" : "thankyou so are you", "you are awesome" : "thankyou, so are you", "be my valentine" : "that will be my pleasure", "i am happy" : "keep smiling", 
"i am sad" : "you are strong", "i don't know what to do" : "never doubt yourself", " i am alone": "i will always be there for you", 
"what's your favourite series": "i love how i met your mother", "what's your favourite colour" : "same as yours", "mountains or beach" : "mountains and beach", 
"what's your age": "oh, you never ask a girl about her age", "what's your favourite flower" : "rose", "what's up" : "waiting for you sir",
"i feel like dying": "your life is very precious, what will i do without you?", "do you like me" : "obviously, i do", "do you believe in god?" : "i am an atheist", 
"how are you feeling" : "very active",  "hug me" : "aww, teddy bear", "do you like siri" : "do you like your neighbours",
"do you like google assistant" : "i really like it. we keep planning a meting with siri and cortana but we all are so busy", "sun or moon" : "moon",
"do you like cortana" : "do you like your neighbours", "do you like alexa" : "do you like your neighbours"}




#Function to send mails
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('terabhaiironmanhai@gmail.com','yoyohoneysingh')
    server.sendmail('terabhaiironmanhai@gmail.com', to, content)
    server.close()

def mail():
     try:
         speak("Who should I mail, sir?")
         naam = takeCommand().lower()
         if naam in emails:
             speak("what should i say, sir")
             content = takeCommand()
             to = emails[naam]
         else:
             print('I don\'t have ' + naam + '\'s username, what is it?')
             speak('I don\'t have ' + naam + '\'s username, what is it?')
             username = input()
             username = takeCommand().lower()
             emails[naam] = username
             print('Data updated.')
         sendEmail(to, content)
         speak("Mail sent!")
         print("Mail sent!")
     except Exception as e:
         print(e)
         speak("i am afraid sir, the mail could not be sent!")





def speak(audio):
    engine.say(audio)
    engine.runAndWait() 



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<15:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("i am your Assistant, sir, how may i help u?")



def takeCommand():
    #take microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")


    except Exception:
        print("didn't catch that")
        return 'None'
    return query
def open_website ():
    if 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open gmail" in query:
        webbrowser.open("gmail.com")
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
    elif "open facebook" in query:
        webbrowser.open("facebook.com")
    elif "open twitter" in query:
        webbrowser.open("twitter.com")
    elif "open netflix" in query:
        webbrowser.open("netflix.com")
    elif "open blackboard" in query:
        webbrowser.open("learn.upes.ac.in/webapps/login/")
    elif "open whatsapp" in query:
        webbrowser.open("web.whatsapp.com")
    elif "open geeks for geeks" in query:
        webbrowser.open("geeksforgeeks.org")
    elif "open tutorialspoint" in query:
        webbrowser.open("tutorialspoint.com")
    elif 'open anaconda' in query:
                condaPath = "C:\\Users\\500067978\\python\\pythonw.exe C:\\Users\\500067978\\python\\cwp.py C:\\Users\\500067978\\python C:\\Users\\500067978\\python\\pythonw.exe C:\\Users\\500067978\\python\\Scripts\\anaconda-navigator-script.py"
                os.startfile(condaPath)
                


def close():
    print("Which application should i close?")
    speak("Which application should i close?")
    var = takeCommand().lower()
    var = var+'.exe'
    for proc in psutil.process_iter():
        if(proc.name().lower() in var):
            p = psutil.Process(proc.pid)
            p.terminate()
            print("Process Terminated")
            speak("Process Terminated")


def show_pdf():
    path = "C:\\Users\\500067978\\Documents\\extra"
    files = os.listdir(path)
    for name in files:
        speak(name)


def pdf_reaeder():
    show_pdf()
    pdfFile = takeCommand().lower()
    pdfFile = pdfFile + '.txt' 
    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    page=pdfRead.getPage(0)
    pageContent=page.extractText()
    print(pageContent)
    speak(pageContent)

     
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        try:
                speak(dict[query])
                print(dict[query])

        except:
            pass
        if "open" in query:
            open_website() 
        elif 'wikipedia' in query:#to search wikipedia
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "take rest" in query:#to stop jarvis from listening
                speak("ok sir")
                break
        elif 'play music' in query:
                music_dir = 'D:\\jarvis_songs'
                songs = os.listdir(music_dir)
                print(songs)
                value = randint(0,1)
                os.startfile(os.path.join(music_dir, songs[value]))
        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
        elif 'mail' in query:
            mail()

        elif 'close' in query:
            close()
        elif 'read' in query:
            pdf_reaeder()
