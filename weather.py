#Running through a terminal like python weather.py

from config_Wth import API, URL
import requests



place = input("Enter the place: ")
requests_url = f"{URL}?appid={API}&q={place}"
resp = requests.get(requests_url)

def weather():
    while resp.status_code == 200:
        js = resp.json()
	    #print(js)#To get all the keys
        weather = js['weather'][0]['description']
        print('Weather:', weather)
        temp = round(js['main']['temp'] - 273.15, 2)
        print('Temperature:', temp, 'C°')
        break
    else:
        print('code error =)')
weather()