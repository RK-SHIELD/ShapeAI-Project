import requests
import os
from datetime import datetime

#To create a file with a name
file_name = input("Enter the file name: ")+".txt"

#To access the 3rd party API we use api key
api_key = '97d3a761e3b2d7e8b403f9bc98fb8aa5'
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#To import the data into the file
file = open(file_name,'w')
file.write("City name : ",location)
file.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
file.write("Current temperature is: {:.2f} deg C".format(temp_city))
file.write("Current weather desc  :",weather_desc)
file.write("Current Humidity      :",hmdt, '%')
file.write("Current wind speed    :",wind_spd ,'kmph')
file.close()

#To open the file
os.startfile(file_name)
