import requests
import sys
import json

class WeatherService:
    API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric';
    FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}&units=metric';
    API_KEY = '3b31a7e394e41c3a30759dfde1a3383e'

    def __init__(self):
        pass

    def get_weather_data(self, city_name):
        r = requests.get(WeatherService.API_URL.format(city_name, WeatherService.API_KEY))
        weather_data = (r.json())
        temp = self._extract_temp(weather_data)
        description = self._extract_desc(weather_data)
        return 'Currently, in {}, its {} degrees with {}'.format(city_name, temp, description)

    def _extract_temp(self, weatherdata):
        temp = weatherdata['main']['temp']
        return temp

    def _extract_desc(self, weatherdata):
        return weatherdata['weather'][0]['description']

    def get_main_forecast(self, city_name):
        r = requests.get(WeatherService.FORECAST_URL.format(city_name, WeatherService.API_KEY))
        result = r.json()
        return result['list'][0]

    def get_forecast(self, city_name):
        return self.get_main_forecast(city_name)['weather'][0]['description']
    
    def get_wind(self, city_name):
        return self.get_main_forecast(city_name)['wind']['speed']

    def get_feels(self, city_name):
        return self.get_main_forecast(city_name)['main']['feels_like']

    def get_temperature(self, city_name):
        return self.get_main_forecast(city_name)['main']['temp']

def optionChecker(option, wService, cityName):
    op = wService.get_main_forecast(cityName)

    if(option == "1"):
        op = {"The current weather in {} is".format(cityName): wService.get_forecast(cityName)}
    
    elif(option == "2"):
        op = {"The current wind in {} speed is".format(cityName): wService.get_wind(cityName)}
    
    elif(option == "3"):
        op = {"It feels like ": wService.get_feels(cityName)}
    
    elif(option == "4"):
        op = {"The temperature is":wService.get_temperature(cityName)}
    
    else:
        op = {"ConMiGo got no answers ConMi": op}
    
    return op

if __name__ == "__main__" :
    wService = WeatherService()

    option = input("Enter an option \n1. Weather\n2. Windy\n3. Feels\n4.Temperature\n")
    cityName = input("Enter a city\n")

    data = optionChecker(option, wService, cityName)
    print(data)