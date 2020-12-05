import urllib.request
import urllib.parse
import re
import pyttsx3
import speech_recognition as sr
import time





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

url = 'http://pythonprogramming.net'
values = {'s':'basics','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
speak(paragraphs) 

for eachP in paragraphs:
    speak(eachP)
    
    
