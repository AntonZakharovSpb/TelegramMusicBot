import telebot

bot = telebot.TeleBot('5153013937:AAGsMqjHU-4LIL3sixjkb0UawZYAwMlhXV0')


class Akkord():
 # 'в этот класс можно записывать аккорды'
    ton = 0
    subd = 0
    dom = 0
    namer = 0
    def __init__(self, Namer ='undefined', Notes = 3, Ton = 'La', Subd = 'Do', Dom = 'Mi' ):
        self.namer = Namer
        self.subd = Subd
        self.dom = Dom
        self.ton = Ton
        self.notes = Notes
        a = 0

    def show_notes(self):
        return f'аккорд {self.namer} состоит из нот {self.ton, self.subd, self.dom}'

Am = Akkord('Am - ля минор',  3,  'La',  'Do',  'Mi')
Dm = Akkord('Dm - ре минор',3,'Re','Fa','La')
E = Akkord('E - ми мажор',3,'Mi','Sol Diez','Si')
Em = Akkord('Em - ми минор',3,'Mi','Sol','Si')

AmText = ('Am','am','AM', 'ам', 'Ам','Ам','Ля минор','ля минор','ляминор','Ляминор','A m', 'a m')
DmText = ('Дм','дм','ДМ','Dm','dm','DM', 'ре минор','Ре минор','Реминор','Реминор','D m', 'd m', 'рэ минор','Рэ минор','Рэминор','Рэминор')
EText = ('Е','е','E','e', 'Ми мажор','ми мажор','мимажор','Мимажор','МИ','Ми','ми')
EmText = ('Em','em','EM', 'ем', 'Ем','Ем','Ми минор','ми минор','миминор','Миминор','E m', 'e m')

menu = '''- Отправьте мне название аккорда и я скажу из каких нот он состоит(в демо режиме только три блатных аккорда)
- Вы можете оставить свой вопрос, и я передам его Антону, для этого напишите сообщение
 co знаком вопроса?( Укажите в сообщении от кого вопрос)
 .
- Напишите натуральное число и я скажу, четное ли оно'''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, menu)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text == "Меню" or message.text == "меню" or message.text == "МЕНЮ":
            bot.send_message(message.from_user.id, menu)
        elif message.text in AmText:
            bot.send_message(message.from_user.id, Am.show_notes())
        elif message.text in DmText:
            bot.send_message(message.from_user.id, Dm.show_notes())
        elif message.text in EText:
            bot.send_message(message.from_user.id, E.show_notes())
        elif '?' in message.text:
            f = open(f'text1.txt', 'a')
            f.write('\n'+ message.text)
            f.close()
            bot.send_message(message.from_user.id, "Вопрос отправлен Антону")
          #  bot.send_message(message.from_user.id, menu)
        elif message.text.isdigit():
            if int(message.text) % 2 == 0:
                bot.send_message(message.from_user.id, "честное число")
            else:
                bot.send_message(message.from_user.id, "нечестное число")
           # bot.send_message(message.from_user.id, menu)
        else:
            bot.send_message(message.from_user.id, "Ваш запрос пока непонятен, и отправлен Антону для улучшения работы Бота. Напишите мне Меню и я отвечу, что я могу")
            f = open(f'text1.txt', 'a')
            f.write('\n'+ message.text)
            f.close()


bot.polling()
