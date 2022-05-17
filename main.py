import os

import telebot

import text2mp3
import weather
from telebot import types

secret = os.environ['token']
bot = telebot.TeleBot(secret)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}!')


@bot.message_handler(content_types='text')
def send_answer(message):
    if message.text == 'weather':
        answer = weather.weather_message_for_send()
        bot.send_message(message.chat.id, answer)
    else:
        text = message.text
        text2mp3.convert_text(text)
        bot.send_audio(message.chat.id, audio=open('last_sound.mp3', 'rb'))


@bot.message_handler(commands=['help'])
def get_all_commands(message):
    markup = types.ReplyKeyboardMarkup()
    all_weather = types.KeyboardButton('weather')
    markup.add(all_weather)

    bot.send_message(message.chat.id, 'Commands:', reply_markup=markup)


bot.polling(none_stop=True)
