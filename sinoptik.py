import telebot
from telebot import types
import requests
import requests, bs4
#from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import mysql.connector

#bot = telebot.TeleBot("1009825598:AAFFhJy5gwamGCR5RZ3Nmpt5rGaQBAXxSuE") #@mecafetestbot
bot = telebot.TeleBot("842277315:AAGYaZV9kRdrvGUdpVLmONUaT-qUYyJvB5o") #@leopogoda_bot

user_dict = {}

# conn = mysql.connector.connect(user=user1, password=passwords1, host=host1, database=database1)
# cursor = conn.cursor(buffered=True)
# cursor.execute('''
# CREATE TABLE user (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# IDIS varchar(100),
# Name varchar(100),
# Number varchar(100),
# Date varchar(100),
# Time varchar(100),
# People varchar(100),
# Koment varchar(100),
# Street varchar(100),
# Admin varchar(100),
# UNIQUE KEY `IDIS_UNIQUE` (`IDIS`))
# ''')

global user1, passwords1, host1, database1
user1 = 'b6223a19b23c51'
passwords1 = '75e8e721'
host1 = 'eu-cdbr-west-02.cleardb.net'
database1 = 'heroku_d86f7f84b7474c6'

# conn = mysql.connector.connect(user=user1, password=passwords1, host=host1, database=database1)
# cursor = conn.cursor(buffered=True)
#
#
# cursor.execute('''
# CREATE TABLE reklama (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# Text varchar(3000))
# ''')
#

#Создание колонки в таблице
# try:
#     cursor.execute('''
#     ALTER TABLE user ADD COLUMN Reklama varchar(3000)
#     ''')
# except mysql.connector.Error as err:
#     print("Something went wrong: {}".format(err))


# global user1, passwords1, host1, database1
# user1 = 'root'
# passwords1 = 'godfazer'
# host1 = '127.0.0.1'
# database1 = 'botmaker'




timelist = ['12:00', '12:30',
            '13:00', '13:30',
            '14:00', '14:30',
            '15:00', '15:30',
            '16:00', '16:30',
            '17:00', '17:30',
            '18:00', '18:30',
            '19:00', '19:30',
            '20:00', '20:30',
            '21:00', '21:30']     # массив

class User:
    def __init__(self, gorod):
        self.gorod = gorod
        self.phone = None
        self.date = None
        self.time = None
        self.people = None
        self.user_id = None
        self.today = None
        self.tomorrow = None
        self.today3 = None
        self.today4 = None
        self.today5 = None
        self.today6 = None
        self.today7 = None


# def keyboard():
#     markup_menu = types.ReplyKeyboardMarkup(True, False)
#     markup_menu.row('Погода на сегодня')
#     markup_menu.row('Погода на сегодня', 'Погода на завтра')
#     bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu)



gorod = ''

help = "Привет, я бот прогноза погоды!\n\nВводить можно русскими и украинскими буквами. Пример: \n киев, Киев, київ, Київ"


@bot.message_handler(commands=['start'])
def first(message):
    proverka_user_id(message)
    if message.chat.id == admin_id(message):
        markup_menu = types.ReplyKeyboardMarkup(True, False)
        markup_menu.row('✔️Административная панель')
        markup_menu.row('help')
        bot.send_message(message.chat.id, 'Напишите город', reply_markup=markup_menu)

    else:
        markup_menu = types.ReplyKeyboardMarkup(True, False)
        markup_menu.row('help')
        bot.send_message(message.chat.id, 'Напишите город', reply_markup=markup_menu)



@bot.message_handler(func=lambda message: True, content_types=['text'])
def send_text(message):
    global date1, date2, date3, date4, date5, date6, date7
    gorod = message.text
    s1 = requests.get('https://sinoptik.ua/погода-' + gorod)
    if s1:
        b = bs4.BeautifulSoup(s1.text, "html.parser")
        date = b.select('#bd1 .date')
        date1 = date[0].getText()
        date = b.select('#bd2 .date')
        date2 = date[0].getText()
        date = b.select('#bd3 .date')
        date3 = date[0].getText()
        date = b.select('#bd4 .date')
        date4 = date[0].getText()
        date = b.select('#bd5 .date')
        date5 = date[0].getText()
        date = b.select('#bd6 .date')
        date6 = date[0].getText()
        date = b.select('#bd7 .date')
        date7 = date[0].getText()
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        if gorod != 'help':
            chat_id = message.chat.id
            gorod = message.text
            user = User(gorod)
            user_dict[chat_id] = user
            bot.send_message(message.chat.id, str(user.gorod), reply_markup=markup_menu1)
            #user.today = today(message)
            send = bot.send_message(message.chat.id, 'Выберите день:', reply_markup=markup_menu1)
            bot.register_next_step_handler(send, next1)
    elif message.text == 'help':
        bot.send_message(message.chat.id, help)
    elif message.text == '✔️Административная панель':
        if message.chat.id == admin_id(message):
            try:
                adminbutton1 = types.ReplyKeyboardMarkup(True, False)
                adminbutton1.row('Рассылка', 'Статистика', 'Бан/Разбан')
                adminbutton1.row('Количество пользователей')
                adminbutton1.row('Заблокированные пользователи')
                adminbutton1.row('Добавить Админа', 'Удалить Админа')
                adminbutton1.row('Ⓜ Главное меню')
                bot.send_message(message.chat.id, 'Выбирайте:', reply_markup=adminbutton1)
            except:
                pass
    elif message.text == 'Количество пользователей':
        global user_id
        user_id = message.from_user.id
        send_sms()
    elif message.text == 'Ⓜ Главное меню':
        first(message)
    else:
        first(message)

        # try:
        #     markup_menu = types.ReplyKeyboardMarkup(True, False)
        #     markup_menu.row('help')
        #     bot.send_message(message.chat.id, 'Напишите город повторно:', reply_markup=markup_menu)
        #     #send = bot.send_message(message.chat.id, 'Напишите город повторно:', reply_markup=markup_menu)
        #     #bot.register_next_step_handler(send, send_text)
        #     gorod = message.text
        #     s1 = requests.get('https://sinoptik.ua/погода-' + gorod)
        #     if s1:
        #         b = bs4.BeautifulSoup(s1.text, "html.parser")
        #         date = b.select('#bd1 .date')
        #         date1 = date[0].getText()
        #         date = b.select('#bd2 .date')
        #         date2 = date[0].getText()
        #         date = b.select('#bd3 .date')
        #         date3 = date[0].getText()
        #         date = b.select('#bd4 .date')
        #         date4 = date[0].getText()
        #         date = b.select('#bd5 .date')
        #         date5 = date[0].getText()
        #         date = b.select('#bd6 .date')
        #         date6 = date[0].getText()
        #         date = b.select('#bd7 .date')
        #         date7 = date[0].getText()
        #         markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        #         markup_menu1.row(date1, date2, date3, date4)
        #         markup_menu1.row(date5, date6, date7)
        #         markup_menu1.row('Ввести другой город')
        #         if gorod != 'help':
        #             chat_id = message.chat.id
        #             gorod = message.text
        #             user = User(gorod)
        #             user_dict[chat_id] = user
        #             bot.send_message(message.chat.id, str(user.gorod), reply_markup=markup_menu1)
        #             # user.today = today(message)
        #             send = bot.send_message(message.chat.id, 'Выберите день:', reply_markup=markup_menu1)
        #             bot.register_next_step_handler(send, next1)
        #     elif message.text == 'help':
        #         bot.send_message(message.chat.id, help)
        # except:
        #     pass

def admin_panel(message):
    if message.text == '✔️Административная панель':
        if message.chat.id == admin_id(message):
            adminbutton1 = types.ReplyKeyboardMarkup(True, False)
            adminbutton1.row('Рассылка', 'Статистика', 'Бан/Разбан')
            adminbutton1.row('Количество пользователей')
            adminbutton1.row('Заблокированные пользователи')
            adminbutton1.row('Добавить Админа', 'Удалить Админа')
            adminbutton1.row('Ⓜ Главное меню')
            bot.send_message(message.chat.id, 'Выбирайте:', reply_markup=adminbutton1)
    elif message.text == 'Количество пользователей':
        global user_id
        user_id = message.from_user.id
        send_sms()
    elif message.text == 'Ⓜ Главное меню':
        first(message)
    else:
        admin_panel(message)

def next1(message):
    if message.text == 'Ввести другой город':
        first(message)
    elif message.text == date1:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.today = today(message)
        bot.send_message(message.chat.id, str(user.today))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    elif message.text == date2:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.tomorrow = tomorrow(message)
        bot.send_message(message.chat.id, str(user.tomorrow))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    elif message.text == date3:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.today3 = today3(message)
        bot.send_message(message.chat.id, str(user.today3))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    elif message.text == date4:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.today4 = today4(message)
        bot.send_message(message.chat.id, str(user.today4))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    elif message.text == date5:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.today5 = today5(message)
        bot.send_message(message.chat.id, str(user.today5))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    elif message.text == date6:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.today6 = today6(message)
        bot.send_message(message.chat.id, str(user.today6))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    elif message.text == date7:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.today7 = today7(message)
        bot.send_message(message.chat.id, str(user.today7))
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)
    else:
        markup_menu1 = types.ReplyKeyboardMarkup(True, False)
        markup_menu1.row(date1, date2, date3, date4)
        markup_menu1.row(date5, date6, date7)
        markup_menu1.row('Ввести другой город')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=markup_menu1)
        bot.register_next_step_handler(send, next2)



def next2(message):
    if message.text == 'Ввести другой город':
        first(message)
    elif message.text == date1 or date2 or date3 or date4 or date5 or date6 or date7:
        next1(message)



# def today(message):
#     chat_id = message.chat.id
#     user = user_dict[chat_id]
#     headers = {'accept': '*/*',
#                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36'}
#     s = 'https://sinoptik.ua/погода-' + str(user.gorod)
#     session = requests.Session()
#     request = session.get(s, headers=headers)
#     if request.status_code == 200:
#         soup = bs(request.content, "html.parser")
#         print(soup)
#         divs = soup.find('div', attrs={'id': 'bd1c'})
#         #print(len(divs))
#         print(divs)
#         # for div in divs:
#         #     day = div.find('p').text
#         #     print(day)
#         #     date = div.find('p', attrs={'class': 'date'}).text
#         #     print(date)
#         #     temperature = div.find('div', attrs={'class': 'temperature'}).text
#         #     print(temperature)
#
#         # soup = bs(request.content, "html.parser")
#         # print('Good')
#         # divs = soup.find_all('div', attrs={'id': 'bd1'})
#         # print(len(divs))
#         # print(divs)
#         # for div in divs:
#         #     day = div.find('p').text
#         #     print(day)
#         #     date = div.find('p', attrs={'class': 'date'}).text
#         #     print(date)
#         #     temperature = div.find('div', attrs={'class': 'temperature'}).text
#         #     print(temperature)
#         # for div in divs:
#         #     title = div.find('p', attrs={'class': 'date'}).text
#         #     print(title)
#         # p3 = b.select('#bd1c .temperature .p3')
#         #
#         # pogoda1 = p3[0].getText()
#         #
#         # p4 = b.select('.temperature .p4')
#         #
#         # pogoda2 = p4[0].getText()
#         #
#         # p5 = b.select('.temperature .p5')
#         #
#         # pogoda3 = p5[0].getText()
#         #
#         # p6 = b.select('.temperature .p6')
#         #
#         # pogoda4 = p6[0].getText()
#         #
#         # p7 = b.select('.temperature .p7')
#         #
#         # pogoda5 = p7[0].getText()
#         #
#         # p8 = b.select('.temperature .p8')
#         #
#         # pogoda6 = p8[0].getText()
#         #
#         # date = b.select('#bd1 .date')
#         # date1 = date[0].getText()
#         #
#         # month = b.select('#bd1 .month')
#         # month1 = month[0].getText()
#         #
#         # daylink = b.select('#bd1 .day-link')
#         # daylink1 = daylink[0].getText()
#         #
#         # now = datetime.now()
#         # now = now + timedelta(hours=3)
#         #
#         # one_days = timedelta(0)  # плюсует следущий день
#         # in_two_days = now + one_days
#         # datapogoda = in_two_days.strftime(
#         #     "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
#         # # bot.send_message(message.chat.id, datapogoda)
#         # dataminuts = in_two_days.strftime(
#         #     "%Y-%m-%d %H:%M:%S")
#         #
#         # answer = dataminuts + "\n\n"
#         #
#         # answer += daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"
#         #
#         # answer += 'Утром :' + pogoda1 + ' ' + pogoda2 + "\n"
#         #
#         # answer += 'Днём :' + pogoda3 + ' ' + pogoda4 + "\n"
#         #
#         # answer += 'Вечер :' + pogoda5 + ' ' + pogoda6 + "\n\n"
#         #
#         # pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
#         # pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
#         # pw = b.select('.wDescription')  # прогноз погоды описание
#         # p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
#         # answer += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"
#         #
#         # if (pico1):  # предупреждение град, гроза, пожарность
#         #     pogoda = pico1[0].getText()
#         #     answer += pogoda.strip() + "\n\n"
#         # else:
#         #     answer += ""
#         #
#         # if (pico3):  # ветер
#         #     pogoda = pico3[0].getText()
#         #     answer += pogoda.strip() + "\n\n"
#         # else:
#         #     answer += ""
#         #
#         # if (pw):  # прогноз погоды описание
#         #     pogoda = pw[0].getText()
#         #     answer += pogoda.strip() + "\n\n"
#         # else:
#         #     answer += ""
#         #
#         # if (p):  # Народный прогноз погоды
#         #     pogoda = p[0].getText()
#         #     answer += pogoda.strip()
#         # else:
#         #     answer += ""
#         #
#         # return answer
#     else:
#         # chat_id = message.chat.id
#         # user = user_dict[chat_id]
#         # headers = {'accept': '*/*',
#         #            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36'}
#         # s = 'https://sinoptik.ua/погода-' + str(user.gorod)
#         # session = requests.Session()
#         # request = session.get(s, headers=headers)
#         # if request.status_code == 200:
#         #     b = bs4.BeautifulSoup(s.text, "html.parser")
#         #
#         #     p3 = b.select('#bd1c .temperature .p3')
#         #
#         #     pogoda1 = p3[0].getText()
#         #
#         #     p4 = b.select('.temperature .p4')
#         #
#         #     pogoda2 = p4[0].getText()
#         #
#         #     p5 = b.select('.temperature .p5')
#         #
#         #     pogoda3 = p5[0].getText()
#         #
#         #     p6 = b.select('.temperature .p6')
#         #
#         #     pogoda4 = p6[0].getText()
#         #
#         #     p7 = b.select('.temperature .p7')
#         #
#         #     pogoda5 = p7[0].getText()
#         #
#         #     p8 = b.select('.temperature .p8')
#         #
#         #     pogoda6 = p8[0].getText()
#         #
#         #     date = b.select('#bd1 .date')
#         #     date1 = date[0].getText()
#         #
#         #     month = b.select('#bd1 .month')
#         #     month1 = month[0].getText()
#         #
#         #     daylink = b.select('#bd1 .day-link')
#         #     daylink1 = daylink[0].getText()
#         #
#         #     now = datetime.now()
#         #     now = now + timedelta(hours=3)
#         #
#         #     one_days = timedelta(0)  # плюсует следущий день
#         #     in_two_days = now + one_days
#         #     datapogoda = in_two_days.strftime(
#         #         "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
#         #     # bot.send_message(message.chat.id, datapogoda)
#         #     dataminuts = in_two_days.strftime(
#         #         "%Y-%m-%d %H:%M:%S")
#         #
#         #     answer = dataminuts + "\n\n"
#         #
#         #     answer += daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"
#         #
#         #     answer += 'Утром :' + pogoda1 + ' ' + pogoda2 + "\n"
#         #
#         #     answer += 'Днём :' + pogoda3 + ' ' + pogoda4 + "\n"
#         #
#         #     answer += 'Вечер :' + pogoda5 + ' ' + pogoda6 + "\n\n"
#         #
#         #     pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
#         #     pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
#         #     pw = b.select('.wDescription')  # прогноз погоды описание
#         #     p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
#         #     answer += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"
#         #
#         #     if (pico1):  # предупреждение град, гроза, пожарность
#         #         pogoda = pico1[0].getText()
#         #         answer += pogoda.strip() + "\n\n"
#         #     else:
#         #         answer += ""
#         #
#         #     if (pico3):  # ветер
#         #         pogoda = pico3[0].getText()
#         #         answer += pogoda.strip() + "\n\n"
#         #     else:
#         #         answer += ""
#         #
#         #     if (pw):  # прогноз погоды описание
#         #         pogoda = pw[0].getText()
#         #         answer += pogoda.strip() + "\n\n"
#         #     else:
#         #         answer += ""
#         #
#         #     if (p):  # Народный прогноз погоды
#         #         pogoda = p[0].getText()
#         #         answer += pogoda.strip()
#         #     else:
#         #         answer += ""
#         #
#         #     return answer
#         print("Error")


# def tomorrow():
#     now = datetime.now()
#     now = now + timedelta(hours=3)
#
#     one_days = timedelta(1)  # плюсует следущий день
#     in_two_days = now + one_days
#     datapogoda = in_two_days.strftime(
#         "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
#     # bot.send_message(message.chat.id, datapogoda)
#     dataminuts = in_two_days.strftime(
#         "%Y-%m-%d %H:%M:%S")
#     s1 = requests.get('https://sinoptik.ua/погода-' + User.gorod + '/' + datapogoda)  # следущий день
#     if s1:
#         b = bs4.BeautifulSoup(s1.text, "html.parser")
#
#         p3 = b.select('.temperature .p3')
#
#         pogoda3 = p3[0].getText()
#
#         p4 = b.select('.temperature .p4')
#
#         pogoda4 = p4[0].getText()
#
#         p5 = b.select('.temperature .p5')
#
#         pogoda5 = p5[0].getText()
#
#         p6 = b.select('.temperature .p6')
#
#         pogoda6 = p6[0].getText()
#
#         p7 = b.select('.temperature .p7')
#
#         pogoda7 = p7[0].getText()
#
#         p8 = b.select('.temperature .p8')
#
#         pogoda8 = p8[0].getText()
#
#         date = b.select('#bd2 .date')
#         date1 = date[0].getText()
#
#         month = b.select('#bd2 .month')
#         month1 = month[0].getText()
#
#         daylink = b.select('#bd2 .day-link')
#         daylink1 = daylink[0].getText()
#
#         answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"
#
#         answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n"
#
#         answer2 += 'Днём :' + pogoda5 + ' ' + pogoda6 + "\n"
#
#         answer2 += 'Вечер :' + pogoda7 + ' ' + pogoda8 + "\n\n"
#
#         p = b.select('.rSide .description')
#
#         pogoda = p[0].getText()
#
#         answer2 += pogoda.strip()
#         return answer2
#
#     else:
#         now = datetime.now()
#         now = now + timedelta(hours=3)
#
#         one_days = timedelta(1)  # плюсует следущий день
#         in_two_days = now + one_days
#         datapogoda = in_two_days.strftime(
#             "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
#         # bot.send_message(message.chat.id, datapogoda)
#         dataminuts = in_two_days.strftime(
#             "%Y-%m-%d %H:%M:%S")
#         s1 = requests.get('https://sinoptik.ua/погода-' + User.gorod + '/' + datapogoda)  # следущий день
#         if s1:
#             b = bs4.BeautifulSoup(s1.text, "html.parser")
#
#             p3 = b.select('.temperature .p3')
#
#             pogoda3 = p3[0].getText()
#
#             p4 = b.select('.temperature .p4')
#
#             pogoda4 = p4[0].getText()
#
#             p5 = b.select('.temperature .p5')
#
#             pogoda5 = p5[0].getText()
#
#             p6 = b.select('.temperature .p6')
#
#             pogoda6 = p6[0].getText()
#
#             p7 = b.select('.temperature .p7')
#
#             pogoda7 = p7[0].getText()
#
#             p8 = b.select('.temperature .p8')
#
#             pogoda8 = p8[0].getText()
#
#             date = b.select('#bd2 .date')
#             date1 = date[0].getText()
#
#             month = b.select('#bd2 .month')
#             month1 = month[0].getText()
#
#             daylink = b.select('#bd2 .day-link')
#             daylink1 = daylink[0].getText()
#
#             answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"
#
#             answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n"
#
#             answer2 += 'Днём :' + pogoda5 + ' ' + pogoda6 + "\n"
#
#             answer2 += 'Вечер :' + pogoda7 + ' ' + pogoda8 + "\n\n"
#
#             p = b.select('.rSide .description')
#
#             pogoda = p[0].getText()
#
#             answer2 += pogoda.strip()
#
#             return answer2


def today(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s = requests.get('https://sinoptik.ua/погода-' + str(user.gorod))
    if s:
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

        now = datetime.now()
        now = now + timedelta(hours=0)

        one_days = timedelta(0)  # плюсует следущий день
        in_two_days = now + one_days
        datapogoda = in_two_days.strftime(
            "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
        # bot.send_message(message.chat.id, datapogoda)
        dataminuts = in_two_days.strftime(
            "%Y-%m-%d %H:%M:%S")

        answer = dataminuts + "\n\n"

        answer += daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

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

        return answer
    else:
        s = requests.get('https://sinoptik.ua/погода-' + str(user.gorod))
        if s:
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

            now = datetime.now()
            now = now + timedelta(hours=3)

            one_days = timedelta(0)  # плюсует следущий день
            in_two_days = now + one_days
            datapogoda = in_two_days.strftime(
                "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в строку и дает ноль спереди
            # bot.send_message(message.chat.id, datapogoda)
            dataminuts = in_two_days.strftime(
                "%Y-%m-%d %H:%M:%S")

            answer = dataminuts + "\n\n"

            answer += daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

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

            return answer


def tomorrow(message):
    now = datetime.now()
    now = now + timedelta(hours=3)

    one_days = timedelta(1)  # плюсует следущий день
    in_two_days = now + one_days
    datapogoda = in_two_days.strftime(
        "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
    # bot.send_message(message.chat.id, datapogoda)
    dataminuts = in_two_days.strftime(
        "%Y-%m-%d %H:%M:%S")
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
    if s1:
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

        answer2 += 'Вечер :' + pogoda7 + ' ' + pogoda8 + "\n\n"

        #p = b.select('.rSide .description')

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer2 += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer2 += pogoda.strip()
        else:
            answer2 += ""

        pogoda = p[0].getText()

        answer2 += pogoda.strip()
        return answer2

    else:
        now = datetime.now()
        now = now + timedelta(hours=3)

        one_days = timedelta(1)  # плюсует следущий день
        in_two_days = now + one_days
        datapogoda = in_two_days.strftime(
            "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
        # bot.send_message(message.chat.id, datapogoda)
        dataminuts = in_two_days.strftime(
            "%Y-%m-%d %H:%M:%S")
        chat_id = message.chat.id
        user = user_dict[chat_id]
        s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
        if s1:
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

            answer2 += 'Вечер :' + pogoda7 + ' ' + pogoda8 + "\n\n"

            p = b.select('.rSide .description')

            pogoda = p[0].getText()

            answer2 += pogoda.strip()

            return answer2

def today3(message):
    now = datetime.now()
    now = now + timedelta(hours=3)

    #one_days = timedelta(days=1)  # плюсует следущий день
   #in_two_days = now + timedelta(days=1)
    in_two_days = now.replace(day=int(now.day + 2))
    datapogoda = in_two_days.strftime(
        "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
    # bot.send_message(message.chat.id, datapogoda)
    dataminuts = in_two_days.strftime(
        "%Y-%m-%d %H:%M:%S")
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
    print(datapogoda)
    if s1:
        b = bs4.BeautifulSoup(s1.text, "html.parser")

        p3 = b.select('.temperature .p3')

        pogoda3 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda4 = p4[0].getText()

        date = b.select('#bd3 .date')
        date1 = date[0].getText()

        month = b.select('#bd3 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd3 .day-link')
        daylink1 = daylink[0].getText()

        answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n\n"



        #p = b.select('.rSide .description')

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer2 += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer2 += pogoda.strip()
        else:
            answer2 += ""

        pogoda = p[0].getText()

        answer2 += pogoda.strip()
        return answer2

    else:
        today3(message)

def today4(message):
    now = datetime.now()
    now = now + timedelta(hours=3)

    #one_days = timedelta(days=1)  # плюсует следущий день
   #in_two_days = now + timedelta(days=1)
    in_two_days = now.replace(day=int(now.day + 3))
    datapogoda = in_two_days.strftime(
        "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
    # bot.send_message(message.chat.id, datapogoda)
    dataminuts = in_two_days.strftime(
        "%Y-%m-%d %H:%M:%S")
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
    print(datapogoda)
    if s1:
        b = bs4.BeautifulSoup(s1.text, "html.parser")

        p3 = b.select('.temperature .p3')

        pogoda3 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda4 = p4[0].getText()

        date = b.select('#bd4 .date')
        date1 = date[0].getText()

        month = b.select('#bd4 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd4 .day-link')
        daylink1 = daylink[0].getText()

        answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n\n"



        #p = b.select('.rSide .description')

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer2 += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer2 += pogoda.strip()
        else:
            answer2 += ""

        pogoda = p[0].getText()

        answer2 += pogoda.strip()
        return answer2

    else:
        today3(message)

def today5(message):
    now = datetime.now()
    now = now + timedelta(hours=3)

    #one_days = timedelta(days=1)  # плюсует следущий день
   #in_two_days = now + timedelta(days=1)
    in_two_days = now.replace(day=int(now.day + 4))
    datapogoda = in_two_days.strftime(
        "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
    # bot.send_message(message.chat.id, datapogoda)
    dataminuts = in_two_days.strftime(
        "%Y-%m-%d %H:%M:%S")
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
    print(datapogoda)
    if s1:
        b = bs4.BeautifulSoup(s1.text, "html.parser")

        p3 = b.select('.temperature .p3')

        pogoda3 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda4 = p4[0].getText()

        date = b.select('#bd5 .date')
        date1 = date[0].getText()

        month = b.select('#bd5 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd5 .day-link')
        daylink1 = daylink[0].getText()

        answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n\n"



        #p = b.select('.rSide .description')

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer2 += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer2 += pogoda.strip()
        else:
            answer2 += ""

        pogoda = p[0].getText()

        answer2 += pogoda.strip()
        return answer2

    else:
        today3(message)

def today6(message):
    now = datetime.now()
    now = now + timedelta(hours=3)

    #one_days = timedelta(days=1)  # плюсует следущий день
   #in_two_days = now + timedelta(days=1)
    in_two_days = now.replace(day=int(now.day + 5))
    datapogoda = in_two_days.strftime(
        "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
    # bot.send_message(message.chat.id, datapogoda)
    dataminuts = in_two_days.strftime(
        "%Y-%m-%d %H:%M:%S")
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
    print(datapogoda)
    if s1:
        b = bs4.BeautifulSoup(s1.text, "html.parser")

        p3 = b.select('.temperature .p3')

        pogoda3 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda4 = p4[0].getText()

        date = b.select('#bd6 .date')
        date1 = date[0].getText()

        month = b.select('#bd6 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd6 .day-link')
        daylink1 = daylink[0].getText()

        answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n\n"



        #p = b.select('.rSide .description')

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer2 += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer2 += pogoda.strip()
        else:
            answer2 += ""

        pogoda = p[0].getText()

        answer2 += pogoda.strip()
        return answer2

    else:
        today3(message)

def today7(message):
    now = datetime.now()
    now = now + timedelta(hours=3)

    #one_days = timedelta(days=1)  # плюсует следущий день
   #in_two_days = now + timedelta(days=1)
    in_two_days = now.replace(day=int(now.day + 6))
    datapogoda = in_two_days.strftime(
        "%Y-%m-%d")  # .strftime("%Y-%m-%d") задаает формат даты в сроку и дает ноль спереди
    # bot.send_message(message.chat.id, datapogoda)
    dataminuts = in_two_days.strftime(
        "%Y-%m-%d %H:%M:%S")
    chat_id = message.chat.id
    user = user_dict[chat_id]
    s1 = requests.get('https://sinoptik.ua/погода-' + str(user.gorod) + '/' + datapogoda)  # следущий день
    print(datapogoda)
    if s1:
        b = bs4.BeautifulSoup(s1.text, "html.parser")

        p3 = b.select('.temperature .p3')

        pogoda3 = p3[0].getText()

        p4 = b.select('.temperature .p4')

        pogoda4 = p4[0].getText()

        date = b.select('#bd7 .date')
        date1 = date[0].getText()

        month = b.select('#bd7 .month')
        month1 = month[0].getText()

        daylink = b.select('#bd7 .day-link')
        daylink1 = daylink[0].getText()

        answer2 = daylink1 + ' ' + date1 + ' ' + month1 + "\n\n"

        answer2 += 'Утром :' + pogoda3 + ' ' + pogoda4 + "\n\n"



        #p = b.select('.rSide .description')

        pico1 = b.select('.rSide .ico-stormWarning-1')  # предупреждение град, гроза, пожарность
        pico3 = b.select('.rSide .ico-stormWarning-3')  # ветер
        pw = b.select('.wDescription')  # прогноз погоды описание
        p = b.select('.oDescription .rSide .description')  # Народный прогноз погоды
        answer2 += "Тут может быть ваша реклама. Контакт: @Arganaft\n\n"

        if (pico1):  # предупреждение град, гроза, пожарность
            pogoda = pico1[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pico3):  # ветер
            pogoda = pico3[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (pw):  # прогноз погоды описание
            pogoda = pw[0].getText()
            answer2 += pogoda.strip() + "\n\n"
        else:
            answer2 += ""

        if (p):  # Народный прогноз погоды
            pogoda = p[0].getText()
            answer2 += pogoda.strip()
        else:
            answer2 += ""

        pogoda = p[0].getText()

        answer2 += pogoda.strip()
        return answer2

    else:
        today3(message)

# Добавление user_id в базу если нету
def proverka_user_id(message):
    try:
        global user_id
        user_id = message.from_user.id
        conn = mysql.connector.connect(user=user1, password=passwords1, host=host1, database=database1)
        cursor = conn.cursor(buffered=True)
        cursor.execute("INSERT INTO user (IDIS) VALUES ('%s')" % (user_id))
        conn.commit()
    except mysql.connector.errors.IntegrityError:
        pass
    finally:
        if (conn.is_connected()):
            conn.close()
            print("MySQL connection is closed")



def send_sms():  # Отправа смс заказа надом в канал
    try:
        conn = mysql.connector.connect(user=user1, password=passwords1, host=host1, database=database1)
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        i = 1
        for j in rows:
            if '{user_id}'.format(user_id=user_id) == j[1]:
                # print("ID: ", j[1])
                # print("ID: ", j[2])
                # print("ID: ", j[3])
                idj = j[1]
                namej = j[2]
                phonej = j[3]
                peoplej = j[6]
                streetj = j[8]

        i += i
        temp = i
    finally:
        if (conn.is_connected()):
            conn.close()
            print("MySQL connection is closed")
    bot.send_message(chat_id=277296176, text='Количество: ' + str(temp))
    #bot.send_message(chat_id=-1001224043774, text='ID: ' + str(idj) + '\n' + 'Имя: ' + str(namej) + '\n' + 'Телефон: ' + str(phonej) + '\n' + 'Адрес Доставки: ' + str(streetj) + '\n' + 'Количество Людей: ' + str(peoplej) + '\n')


def admin_id(message):
    try:
        global userchat_id
        userchat_id = message.from_user.id
        conn = mysql.connector.connect(user=user1, password=passwords1, host=host1, database=database1)
        cursor = conn.cursor(buffered=True)
        cursor.execute('SELECT * FROM user WHERE IDIS = {IDIS}'.format(IDIS=userchat_id))
        rows = cursor.fetchall()
        for j in rows:
            if '{Admin}'.format(Admin=1) == j[9]:
                userchat_id = message.from_user.id
                return userchat_id
    except mysql.connector.errors.ProgrammingError:
        pass
    finally:
        if (conn.is_connected()):
            conn.close()


bot.polling(none_stop=True)
