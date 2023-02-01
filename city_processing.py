from datetime import datetime
from pyowm import OWM
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

# reading OpenWeatherMap API token from file
with open('OpenWether_API_TOKEN.txt', 'r') as weather_token:
    WEATHERTOKEN = weather_token.read()

owm = OWM(WEATHERTOKEN)
mgr = owm.weather_manager()

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")


# get timezone and check if city name is valid
def get_timezone(city):
    try:
        # getting Latitude and Longitude
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        time_zone = obj.timezone_at(lng=location.longitude,
                                    lat=location.latitude)
        return time_zone
    except NameError:
        return 'incorrect data'


def get_time(time_zone):
    city_time_zone = pytz.timezone(time_zone)
    city_time = datetime.now(city_time_zone)
    current_city_time = city_time.strftime('%d.%m, %H:%M')
    return current_city_time


# function to get temperature
def get_temp(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = round(w.temperature('celsius').get('temp'))
    return temperature


def get_humidity(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    humidity = f'{w.humidity}%'
    return humidity


def get_clouds(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    clouds = w.detailed_status
    return clouds


def get_rain(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    rain = w.rain.get('1h')
    return rain
