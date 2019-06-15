import telebot
import requests, bs4
import datetime


bot = telebot.TeleBot("842277315:AAGYaZV9kRdrvGUdpVLmONUaT-qUYyJvB5o")
@bot.message_handler(content_types=['text', 'document', 'audio'])
def send_echo(message):
    s=requests.get('https://sinoptik.com.ru/погода-луцк')

    b=bs4.BeautifulSoup(s.text, "html.parser")

    p3=b.select('#bd1c .temperature .p3')

    pogoda1=p3[0].getText()

    p4=b.select('.temperature .p4')

    pogoda2=p4[0].getText()

    p5=b.select('.temperature .p5')

    pogoda3=p5[0].getText()

    p6=b.select('.temperature .p6')

    pogoda4=p6[0].getText()

    p7=b.select('.temperature .p7')

    pogoda5=p7[0].getText()

    p8=b.select('.temperature .p8')

    pogoda6=p8[0].getText()

    date=b.select('#bd1 .date')
    date1=date[0].getText()

    month=b.select('#bd1 .month')
    month1=month[0].getText()

    daylink=b.select('#bd1 .day-link')
    daylink1=daylink[0].getText()

    answer1 = daylink1 + ' ' + date1 + ' ' + month1

    answer2 = 'Утром :' + pogoda1 + ' ' + pogoda2

    answer3 = 'Днём :' + pogoda3 + ' ' + pogoda4

    answer4 = 'Вечер :' + pogoda5 + ' ' + pogoda6

    p=b.select('.rSide .description')

    pogoda=p[0].getText()

    answer5 = pogoda.strip()
    answer0 = "\n\n"

    now = datetime.datetime.now()

    year0 = str(now.year)
    day0 = str(now.day+1)
    if(now.month <= 9):
        month0=str(now.month)
        month0=('0'+month0)
    if(now.day <= 9):
        day0=str(now.day)
        day0=('0'+day0)
        
    datapogoda=(year0+'-'+month0+'-'+day0)

    s1=requests.get('https://sinoptik.com.ru/погода-луцк/'+datapogoda)

    b=bs4.BeautifulSoup(s1.text, "html.parser")

    p3=b.select('.temperature .p3')

    pogoda3=p3[0].getText()

    p4=b.select('.temperature .p4')

    pogoda4=p4[0].getText()

    p5=b.select('.temperature .p5')

    pogoda5=p5[0].getText()

    p6=b.select('.temperature .p6')

    pogoda6=p6[0].getText()

    p7=b.select('.temperature .p7')

    pogoda7=p7[0].getText()

    p8=b.select('.temperature .p8')

    pogoda8=p8[0].getText()

    date=b.select('#bd2 .date')
    date1=date[0].getText()

    month=b.select('#bd2 .month')
    month1=month[0].getText()

    daylink=b.select('#bd2 .day-link')
    daylink1=daylink[0].getText()

    answer6 = daylink1 + ' ' + date1 + ' ' + month1
    
    answer7 = 'Утром :' + pogoda3 + ' ' + pogoda4

    answer8 = 'Днём :' + pogoda5 + ' ' + pogoda6

    answer9 = 'Вечер :' + pogoda7 + ' ' + pogoda8

    p=b.select('.rSide .description')

    pogoda=p[0].getText()

    answer10 = pogoda.strip()
    
    bot.send_message(message.chat.id, answer1)
    bot.send_message(message.chat.id, answer2)
    bot.send_message(message.chat.id, answer3)
    bot.send_message(message.chat.id, answer4)
    bot.send_message(message.chat.id, answer5)
    bot.send_message(message.chat.id, '==================================================================================================================')
    bot.send_message(message.chat.id, answer6)
    bot.send_message(message.chat.id, answer7)
    bot.send_message(message.chat.id, answer8)
    bot.send_message(message.chat.id, answer9)
    bot.send_message(message.chat.id, answer10)
    

    

bot.polling(none_stop=True)
