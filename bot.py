import requests
import datetime
from config import bot_token, open_weather_token
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Wassup, напиши название города и я тебе скажу точный прогноз погоды")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])


        await message.reply(f"погода в городе : {city} \n температура: {cur_weather}\n"
                f"влажность : {humidity}\n давление : {pressure} мм.рт.ст\n"
                f"ветер : {wind}\n время восхода солнца : {sunrise_time}\n"
                f"закат : {sunset_time}"
                )

    except:
          
        await message.reply('Проверьте ввод города')


if __name__ == '__main__':
    executor.start_polling(dp)