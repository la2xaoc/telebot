import telebot
from telebot import types
import requests, bs4
import datetime
from datetime import datetime, timedelta

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
        s = requests.get('https://sinoptik.com.ru/погода-луцк')

        b = bs4.BeautifulSoup(s.text, "html.parser")

        p3 = b.select('#bd1c .temperature .p3')

        pogoda1 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda2 = p4[0].getText()

        p5 = b.select('.temperature .p5')

        pogoda3 = p5[0].getText()

        p6 = b.select('.temperature .p6')

        pogoda4 = p6[0].getText()

        p7 = b.select('.temperature .p7')

        pogoda5 = p7[0].getText()

        p8 = b.select('.temperature .p8')

        pogoda6 = p8[0].getText()

        date = b.select('#bd1 .date')
        date1 = date[0].getText()

        month = b.select('#bd1 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd1 .day-link')
        daylink1 = daylink[0].getText()

        answer = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer += 'Утром :' + pogoda1 + ' ' + pogoda2 + "\n"

        answer += 'Днём :' + pogoda3 + ' ' + pogoda4 + "\n"

        answer += 'Вечер :' + pogoda5 + ' ' + pogoda6 + "\n\n"

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer += pogoda.strip() + "\n\n"
        else:
            answer += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer += pogoda.strip() + "\n\n"
        else:
            answer += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer += pogoda.strip() + "\n\n"
        else:
            answer += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer += pogoda.strip()
        else:
            answer += ""


        bot.send_message(message.chat.id, answer)

    elif message.text == "Погода на завтра":
        now = datetime.now() 
        one_days = timedelta(1) # плюсует следущий день
        in_two_days = now + one_days
        datapogoda = in_two_days.strftime("%Y-%m-%d") #.strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
        
        s1 = requests.get('https://sinoptik.com.ru/погода-луцк/' + datapogoda)  # следущий день

        b = bs4.BeautifulSoup(s1.text, "html.parser")

        p3 = b.select('.temperature .p3')

        pogoda3 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda4 = p4[0].getText()

        p5 = b.select('.temperature .p5')

        pogoda5 = p5[0].getText()

        p6 = b.select('.temperature .p6')

        pogoda6 = p6[0].getText()

        p7 = b.select('.temperature .p7')

        pogoda7 = p7[0].getText()

        p8 = b.select('.temperature .p8')

        pogoda8 = p8[0].getText()

        date = b.select('#bd2 .date')
        date1 = date[0].getText()

        month = b.select('#bd2 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd2 .day-link')
        daylink1 = daylink[0].getText()

        answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n"

        answer2 += 'Днём :' + pogoda5 + ' ' + pogoda6 + "\n"

        answer2 += 'Вечер :' + pogoda7 + ' ' + pogoda8 + "\n"

        p = b.select('.rSide .description')

        pogoda = p[0].getText()

        answer10 = pogoda.strip()

        bot.send_message(message.chat.id, answer2)
        bot.send_message(message.chat.id, answer10)

    # bot.send_message(message.chat.id, answer)
    # bot.send_message(message.chat.id,'==================================================================================================================')
    # bot.send_message(message.chat.id, answer2)
    # bot.send_message(message.chat.id, answer10)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
