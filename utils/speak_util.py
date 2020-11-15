import pyttsx3
import speech_recognition as sr
def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
def find_in_text(words:list,text):
    for word in words:
        if word not in text:
            return 0
    return 1
