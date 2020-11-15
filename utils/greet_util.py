from utils.speak_util import SpeakText
from datetime import datetime
def greet():
    currentDT = datetime.now()
    if currentDT.hour<12 and currentDT.hour>4:
        greeting="Morning"
    if currentDT.hour>12 and currentDT.hour<17:
        greeting="Afternoon"
    if currentDT.hour>=17:
        greeting="evening"
    SpeakText("Good {} Mr Stark, This is jarvis your personal assistant".format(greeting))
    SpeakText("How Can I help You")