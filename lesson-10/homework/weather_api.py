import requests
from geopy.geocoders import Nominatim

def get_coordinates(city):
    geolocater = Nominatim(user_agent = 'geo_finder')
    location = geolocater.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None

city_name = input("Enter the city: ")
lat, lon = get_coordinates(city_name)
key = '3b9e9eb99c87e30035b48da0b227a431'
res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}")

type_1 = res.json()
weather = type_1['weather']
weather1 = type_1['main']
print(f'Main: {weather[0]['main']}\nDescription: {weather[0]['description']}')
print(f'Temperature: {(weather1['temp']-273.15):.2f} °C\nHumidity: {weather1['humidity']}\nPressure: {weather1['pressure']}')