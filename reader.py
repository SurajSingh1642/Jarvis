import PyPDF2
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 




def main():
    pdfFile="HCK404_VanshArora.pdf"

    pdfRead = PyPDF2.PdfFileReader(pdfFile)
    page=pdfRead.getPage(0)
    pageContent=page.extractText()
    speak(pageContent)


if __name__=="__main__":
    main()