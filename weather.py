import requests
import os

api_key         = os.getenv['OWM_API_KEY']
weather_url     = "https://api.openweathermap.org/data/2.5/weather?"
geo_url         = "https://api.openweathermap.org/geo/1.0/direct?"

city = input("Enter city name: ")

geo_api         = f'{geo_url}q={city}&appid={api_key}'
geo_req         = requests.get(geo_api)
coords          = geo_req.json()
lon             = coords[0]['lon']
lat             = coords[0]['lat']

weather_api     = f'{weather_url}lat={lat}&lon={lon}&appid={api_key}&units=metric'
weather_req     = requests.get(weather_api)
weather_data    = weather_req.json()

for x in weather_data['main']:
    print(x, weather_data['main'][x])