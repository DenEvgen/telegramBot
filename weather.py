import requests
import json


def get_weather(city):
    cities = {'ufa': [54.775, 56.0375], 'msc': [55.636295, 37.547122], 'spb': [59.750064, 30.20226]}
    lat = cities.get(city)[0]
    lon = cities.get(city)[1]
    weather = []
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}5&lon={lon}&appid' \
              '=d7e1d10ab7206592c528b4df6dab1bb1&units=metric'
    response = requests.get(api_url)
    text_weather = response.text
    my_weather_json = json.loads(text_weather)
    cur_weather_ufa = my_weather_json['main']['temp']
    feels_like_weather_ufa = my_weather_json['main']['feels_like']
    weather.append(cur_weather_ufa)
    weather.append(feels_like_weather_ufa)
    return weather


def weather_message_for_send():
    text = 'Погода:\n'
    ufa = f'Уфа: текущая погода {round(get_weather("ufa")[0])}, ощущается как {round(get_weather("ufa")[1])}'
    msc = f'Москва: текущая погода {round(get_weather("msc")[0])}, ощущается как {round(get_weather("msc")[1])}'
    spb = f'Питер: текущая погода {round(get_weather("spb")[0])}, ощущается как {round(get_weather("spb")[1])}'

    text += ufa + '\n' + msc + '\n' + spb
    return text
