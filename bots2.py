import telebot
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot('USE YOUR TOKEN HERE')

start = ''' Ссылка на мою статью "C чего начинать инветстиции":
https://zen.yandex.ru/media/id/5c76e41dd63c5600b3b97287/s-chego-nachinat-investicii-60192788d941687b70b19449


Вы можете задать мне вопрос по инвестициям(для этого напишите сообщение со знаком вопроса) - не забудьте представиться(!!!) -
Антон Захаров ответит на ваш вопрос как только сможет'''

def current_buck_price():
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    headers = {
        'YOU CAN GET YOUR HEADERS FROM GOOGLE'}
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": "2"})
    return convert[0].text

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, start)

@bot.message_handler(commands=['usd'])
def send_course(message):

    bot.reply_to(message, f'Текущий курс доллара - {current_buck_price()} рублей')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text == "Меню" or message.text == "меню" or message.text == "МЕНЮ":
            bot.send_message(message.from_user.id, 'Смотрите список команд')
        elif '?' in message.text:
            f = open(f'text1.txt', 'a')
            f.write('\n' + message.text)
            f.close()
            bot.send_message(message.from_user.id, "Вопрос анонимно отправлен Антону")
        else:
            bot.send_message(message.from_user.id, "А вот это интересно, даже и не знаю, что ответить, но тоже анонимно отправлю Антону")
            f = open(f'text1.txt', 'a')
            f.write('\n' + message.text + ' не вопрос и неизвестно что')
            f.close()


bot.polling()
