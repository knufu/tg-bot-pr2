from config import open_weather_token
from pprint import pprint
import datetime
import requests


def get_weather(city,open_weather_token):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])


        print(f"погода в городе : {city} \n температура: {cur_weather}\n"
                f"влажность : {humidity}\n давление : {pressure} мм.рт.ст\n"
                f"ветер : {wind}\n время восхода солнца : {sunrise_time}\n"
                f"закат : {sunset_time}"
                )

    except Exception as ex:
            print(ex)
            print('Проверьте ввод города')

def main():
    city = input("Введите название города: ")
    get_weather(city,open_weather_token)

if __name__ == '__main__':
    main()