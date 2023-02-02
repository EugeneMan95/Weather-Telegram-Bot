import city_processing as city


# choosing reply message in english
def eng_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hi', 'hey', 'hello'):
        return 'Hey! Specify the city in which you want to know the weather.'

    if user_message in ('who are you?', 'who are you'):
        return 'I am Eugene\'s Wether bot. ' \
               'Specify the city in which you want to know the weather.'

    city_time_zone = city.get_timezone(user_message)
    if city_time_zone == 'incorrect data':
        return 'Incorrect city, try again.'
    elif 'Moscow' in city_time_zone:
        return 'There are no good weather in hell.\n' \
               'Glory to Ukraine!'
    else:
        city_name = user_message.title()
        city_time = city.get_time(city_time_zone)
        city_temp = city.get_temp(city_name)
        city_humidity = city.get_humidity(city_name)
        city_clouds = city.get_clouds(city_name).capitalize()
        city_rain = 'It rains' if city.get_rain(city_name) else 'There is no rain ☀️'
        city_snow = 'It\'s snowing' if city.get_rain(city_name) else 'There is no snow ☀️'
        rain_or_snow = city_rain if city_temp > 0 else city_snow
        message = f'In {city_name} now:\n' \
                  f'🕰️: {city_time}.\n' \
                  f'🌡️: {city_temp}°C.\n' \
                  f'☂️: {rain_or_snow}.\n' \
                  f'☁️: {city_clouds}.\n' \
                  f'💧: {city_humidity}.'
        return message


# choosing reply message in ukrainian
def ukr_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('привіт', 'хай', 'привіт!', 'хай!'):
        return 'Привіт! Вкажи місто, в якому хочеш дізнатись погоду'

    if user_message in ('хто ти?', 'хто ти', 'ти хто?', 'ти хто'):
        return 'Я тестовий бот з погодою від Євгенія. ' \
               'Вкажи місто, в якому хочеш дізнатись погоду'

    city_time_zone = city.get_timezone(user_message)
    if city_time_zone == 'incorrect data':
        return 'Неправильна назва міста, спробуй ще.'
    elif 'Moscow' in city_time_zone:
        return 'Нема гарної погоди в пеклі.\n' \
               'Слава Україні! Слава нації! Пиздець російській федерації!!!'
    else:
        city_name = user_message.title()
        city_time = city.get_time(city_time_zone)
        city_temp = city.get_temp(city_name)
        city_humidity = city.get_humidity(city_name)
        city_clouds = 'Небо чисте ☀️' if city.get_clouds(city_name) == 'clear sky' else 'Хмарно'
        city_rain = 'Йде дощ 🌧️' if city.get_rain(city_name) else 'Дощу нема ☀️'
        city_snow = 'Йде сніг ❄️' if city.get_rain(city_name) else 'Снігу нема ☀️'
        rain_or_snow = city_rain if city_temp > 0 else city_snow
        message = f'У місті {city_name} зараз:\n' \
                  f'🕰️: {city_time}.\n' \
                  f'🌡️: {city_temp}°C.\n' \
                  f'☂️: {rain_or_snow}.\n' \
                  f'☁️: {city_clouds}.\n' \
                  f'💧: {city_humidity}.'
        return message
