import telebot
from telebot  import  types
import requests, bs4
import datetime
import lutsk

bot = telebot.TeleBot("842277315:AAGYaZV9kRdrvGUdpVLmONUaT-qUYyJvB5o")


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_pogoda1 = types.KeyboardButton('Погода на сегодня')
btn_pogoda2 = types.KeyboardButton('Погода на завтра')
markup_menu.add(btn_pogoda1, btn_pogoda2)


@bot.message_handler(commands=['start'])
def send_welcom(message):
    bot.send_message(message.chat.id, "Привет, я бот прогноза погоды", reply_markup=markup_menu)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Погода на сегодня":
        bot.send_message(message.chat.id, lutsk.answer, reply_markup=markup_menu)
    elif message.text == "Погода на завтра":
        bot.send_message(message.chat.id, lutsk.answer2, reply_markup=markup_menu)
        bot.send_message(message.chat.id, lutsk.answer10, reply_markup=markup_menu)





#bot.send_message(message.chat.id, answer)
#bot.send_message(message.chat.id,'==================================================================================================================')
#bot.send_message(message.chat.id, answer2)
#bot.send_message(message.chat.id, answer10)

if __name__ == '__main__':
    bot.polling(none_stop=True)

