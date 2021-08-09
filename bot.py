import telebot
import config
from telebot import TeleBot, types
import kz
import x2
import time

 
bot = telebot.TeleBot(config.TOKEN)

# приветствие при входе
@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='Приветствую в клане!\nПросьба ознакомиться с правилами чата и клана.')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text=='Назад':
        bot.delete_message(message.chat.id, message.message_id)


# меню start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
    item1 = types.KeyboardButton('❗Правила❗')
    item2 = types.KeyboardButton('⚔Рейд⚔')
    item3 = types.KeyboardButton('⚔тык⚔')
    item4 = types.KeyboardButton('⚔Клановая война⚔')
    dalee = types.KeyboardButton('➡ Далее')
 
    markup.add(item1, item2, item3,item4, dalee)
 
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)
 
@bot.message_handler(content_types=['text'])
def bot_message(message):
# 1 страница расширенно
#клановая война
            if message.text == '⚔Клановая война⚔':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('тык')
                item2 = types.KeyboardButton('тык')
                item3 = types.KeyboardButton('тык')
                item4 = types.KeyboardButton('тык')
                item5 = types.KeyboardButton('тык')
                item6 = types.KeyboardButton('тык')
                back = types.KeyboardButton('⬅️ Назад')
 
                markup.add(item1, item2, item3, item4, item5, item6, back)

                bot.send_message(message.chat.id, '⚔ Раздел находится в разработке', reply_markup = markup)
                bot.delete_message(message.chat.id, message.message_id)
# рейд
            elif message.text == '⚔Рейд⚔':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Клановый рейд')
                item2 = types.KeyboardButton('Гоблинус')
                item3 = types.KeyboardButton('ИК и Сунь Укун')
                back = types.KeyboardButton('⬅️ Назад')
                markup.add(item1, item2, item3, back)

                bot.send_message(message.chat.id, '⚔Рейд⚔', reply_markup = markup)
                bot.delete_message(message.chat.id, message.message_id)

                

# 2 страница
            elif message.text == '➡ Далее':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Клановые задания')
                item2 = types.KeyboardButton('Полезные ссылки')
                item3 = types.KeyboardButton('Расписание✖2')
                back = types.KeyboardButton('⬅️ Назад')
 
                markup.add(item1, item2, item3, back)
                bot.send_message(message.chat.id, '➡ Далее', reply_markup = markup)
                bot.delete_message(message.chat.id, message.message_id)


# расписание х2
            elif message.text == 'Расписание✖2':
                photo = open ('2.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, x2.x2, parse_mode="html")

            elif message.text == '❗Правила❗':
                bot.send_message(message.chat.id, '⚔Раздел находится в разработке')
#Полезные ссылки
            elif message.text == 'Полезные ссылки':
                bot.send_message(message.chat.id, '[Английская база знаний AoM](https://www.aomdb.com/)', parse_mode='Markdown')
            

# клановыезадания

            elif message.text == 'Клановые задания':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton(text = 'Понедельник')
                item2 = types.KeyboardButton(text = 'Вторник')
                item3 = types.KeyboardButton(text = 'Среда')
                item4 = types.KeyboardButton(text = 'Четверг')
                item5 = types.KeyboardButton(text = 'Пятница')
                item6 = types.KeyboardButton(text = 'Суббота')
                item7 = types.KeyboardButton(text = 'Воскресение')
                back = types.KeyboardButton('⬅️ Меню')

                markup.add(item1,item2,item3,item4,item5,item6,item7, back)
                bot.send_message(message.chat.id, 'Выберите день недели:', reply_markup = markup)

#информация по клановым за пн-вс
            elif message.text == 'Понедельник':
                bot.send_message(message.chat.id, text = kz.pn, parse_mode="html")
            elif message.text == 'Вторник':
                bot.send_message(message.chat.id, text = kz.vt, parse_mode="html")
            elif message.text == 'Среда':
                bot.send_message(message.chat.id, text = kz.sr, parse_mode="html")
            elif message.text == 'Четверг':
                bot.send_message(message.chat.id, text = kz.cht, parse_mode="html")
            elif message.text == 'Пятница':
                bot.send_message(message.chat.id, text = kz.pt, parse_mode="html")
            elif message.text == 'Суббота':
                bot.send_message(message.chat.id, text = kz.sb, parse_mode="html")
            elif message.text == 'Воскресение':
                bot.send_message(message.chat.id, text = kz.vs, parse_mode="html")  

# меню

            elif message.text == '⬅️ Меню':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('❗Правила❗')
                item2 = types.KeyboardButton('⚔Рейд⚔')
                item3 = types.KeyboardButton('⚔тык⚔')
                item4 = types.KeyboardButton('⚔Клановая война⚔')
                dalee = types.KeyboardButton('➡ Далее')
 
                markup.add(item1, item2, item3, item4, dalee)
                bot.send_message(message.chat.id, '⬅️ Меню', reply_markup = markup)


     
# назад

            elif message.text == '⬅️ Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('❗Правила❗')
                item2 = types.KeyboardButton('⚔Рейд⚔')
                item3 = types.KeyboardButton('⚔тык⚔')
                item4 = types.KeyboardButton('⚔Клановая война⚔')
                dalee = types.KeyboardButton('➡ Далее')
 
                markup.add(item1, item2, item3, item4, dalee)
                bot.send_message(message.chat.id, '⬅️ Назад', reply_markup = markup)

# рейд
            elif message.text == 'Клановый рейд':
                photo = open ('p.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)
#  ИК

            elif message.text == 'ИК и Сунь Укун':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
                item1 = types.KeyboardButton('➢ Схема 3 рейда ')
                item2 = types.KeyboardButton('➢ Схема 4 рейда ')
                raid = types.KeyboardButton('⬅ Рейд')

                markup.add(item1, item2, raid)
                bot.send_message(message.chat.id, 'ИК и Сунь Укун', reply_markup = markup)

            elif message.text == '➢ Схема 3 рейда':
                photo = open ('raid/ИК и Сунь Укун/3.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption = 'Схема 3 рейда')

            elif message.text == '➢ Схема 4 рейда':
                photo = open ('raid/ИК и Сунь Укун/4.1.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption = 'Схема 4 рейда')

#Гоблинус
            elif message.text == 'Гоблинус':
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
                item1 = types.KeyboardButton('➣ Схема 3 рейда ')
                item2 = types.KeyboardButton('➣ Схема 4 рейда ')
                raid = types.KeyboardButton('⬅ Рейд')

                markup.add(item1, item2, raid)
                bot.send_message(message.chat.id, 'Гоблинус', reply_markup = markup)

            elif message.text == '➣ Схема 3 рейда':
                photo = open ('raid/Гоблинус/3.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption = 'Схема 3 рейда')

            elif message.text == '➣ Схема 4 рейда':
                photo = open ('raid/Гоблинус/4.jpg', 'rb')
                bot.send_photo(message.chat.id, photo, caption = 'Схема 4 рейда') 
                

# кнопка рейд назад

            elif message.text == '⬅ Рейд':
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                item1 = types.KeyboardButton('Клановый рейд')
                item2 = types.KeyboardButton('Гоблинус')
                item3 = types.KeyboardButton('ИК и Сунь Укун')
                back = types.KeyboardButton('⬅️ Меню')
                markup.add(item1, item2, item3, back)

                bot.send_message(message.chat.id, '⬅ Рейд', reply_markup = markup)


            
while True:
    try:
        bot.polling(none_stop = True)
    except Exception as e:
        time.sleep(2)

        


