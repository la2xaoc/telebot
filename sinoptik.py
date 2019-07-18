import telebot
from lutsk import lutsk
from telebot import types



bot = telebot.TeleBot("842277315:AAGYaZV9kRdrvGUdpVLmONUaT-qUYyJvB5o")

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_pogoda1 = types.KeyboardButton('Погода на сегодня')
btn_pogoda2 = types.KeyboardButton('Погода на завтра')
markup_menu.add(btn_pogoda1, btn_pogoda2)


@bot.message_handler(commands=['start'])
def send_welcom(message):
    bot.send_message(message.chat.id, "Привет, я бот прогноза погоды", reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def send_text(message):
    if message.text == "Погода на сегодня":
        bot.send_message(message.chat.id, lutsk.dataminuts)
        bot.send_message(message.chat.id, lutsk.answer)

    elif message.text == "Погода на завтра":
        bot.send_message(message.chat.id, lutsk.answer2)


bot.polling(none_stop=True)
updater.start_polling(clean=True)



    # checking if before dyno restart there were running jobs
check_ongoing_processes()

    # handling dyno restart
signal.signal(signal.SIGTERM, handle_dyno_restart)

    
    
