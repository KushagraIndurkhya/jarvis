from utils.weather_util import *
from utils.speak_util import SpeakText,find_in_text
from utils.greet_util import greet
from utils.news_util import speak_news
from utils.brightness_util import change_brightness
import speech_recognition as sr
import re
import webbrowser
import json
import os

with open('config.json') as config_file:
    config_data = json.load(config_file)
recog = sr.Recognizer()

greet()
while (1):
	try:
		with sr.Microphone() as micro:
			recog.adjust_for_ambient_noise(micro)
			audio = recog.listen(micro)
			processed_text = recog.recognize_google(audio)
			processed_text = processed_text.lower()
			print("Stark:"+ processed_text)
			if 'jarvis' in processed_text:
				# Web Utilities
				if (find_in_text(["go","to"],processed_text)):
					x = re.split("to", processed_text)[1]
					url = "http://www." + x[1:]
					SpeakText("opening" + x)
					webbrowser.open_new_tab(url)
				if 'google' in processed_text:
					search = processed_text.split()[(processed_text.split().index('google')) + 1:]
					SpeakText("Googling {}".format(search))
					webbrowser.open_new_tab("https://www.google.com/search?q ={}".format(search))
				if (find_in_text(['get','news'], processed_text)):
					speak_news()
				if (find_in_text(['what is','weather in'], processed_text)):
					x = re.split("weather in", processed_text)[1][1:]
					weather(x)
				# taking log
				if (find_in_text(['take','log'], processed_text)):
					log = re.split("log", processed_text)[1]
					f = open("mylog.txt", "w+")
					f.write("datetime.now()   " + log)
				#controll brightness
				if (find_in_text(['lumos'], processed_text)):
					change_brightness(1.0)
				if (find_in_text(['nox'], processed_text)) or (find_in_text(['knox'], processed_text)):
					change_brightness(0.2)


				# executing commands from config.json
				for key in config_data.keys():
					key_split=key.split()
					if find_in_text(key_split, processed_text):
						if config_data[key]['type'] == 'command':
							if config_data[key]['ask_confirmation'] == 1:
								recog = sr.Recognizer()
								SpeakText("are you sure Mr Stark")
								response = recog.listen(micro)
								rep = recog.recognize_google(response)
								if 'yes' in rep:
									os.system(config_data[key]['action'])
							else:
								os.system(config_data[key]['action'])
						elif config_data[key]['type'] == 'question':
							SpeakText(config_data[key]['answer'])
				# exiting command
				if (find_in_text(["take","rest"],processed_text)):
					SpeakText("Shutting Down")
					sys.exit()

	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))

	except sr.UnknownValueError:
		print("...")