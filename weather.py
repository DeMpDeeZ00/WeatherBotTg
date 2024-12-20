import telebot
import requests
import json
bot = telebot.TeleBot("7537206114:AAFoP7WY2OD9EjL0KQ4PX_xJmCpCqMWE824")
API = "ff80e7ae9562a2e7a019f927dec37938"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "В каком городе ты проживаешь?")

@bot.message_handler(content_types=["text"])
def city(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code==200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        tempR = round(temp, 1)
        if tempR>=20:
            images = "sunny.png"
            bot.send_message(message.chat.id, f'Погода: {tempR} градусов')
        elif tempR <20 and tempR >10:
            bot.send_message(message.chat.id, f'Погода: {tempR} градусов')
            images = "partly_cloudy.png"
        else:
            bot.send_message(message.chat.id, f'Погода: {tempR} градусов')
        images = "cloudy.png"
        file = open("./"+images, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Введите название города еще раз:")

bot.polling(non_stop=True)
