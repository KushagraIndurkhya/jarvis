from utils.speak_util import SpeakText
import requests
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
	return res.json()
def speak_result(result, city):
	SpeakText("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	SpeakText("Wind speed: {} m/s".format(result['wind']['speed']))
	SpeakText("Description: {}".format(result['weather'][0]['description']))
	SpeakText("Weather: {}".format(result['weather'][0]['main']))
def weather(city):
	try:
	  query='q='+city
	  w_data=weather_data(query)
	  speak_result(w_data, city)
	  print()
	except:
	  SpeakText("Your request couldn't be completed please try again")