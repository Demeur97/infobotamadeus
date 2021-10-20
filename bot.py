import telebot
import config
from telebot import TeleBot, types
import kz
import slovo

bot = telebot.TeleBot(config.TOKEN)




# меню start
@bot.message_handler(commands=['start'])
def start(message):
    photo = open ('Ссылки/2.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption = 'Привет, {0.first_name}!\n\nДанный бот создан для хранения информации по Age of Magic.\nЧтобы начать пользоваться ботом напишите команду: <strong>Меню</strong>'.format(message.from_user), parse_mode="html")

# 1 страница
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard = True)
        
        item1 = types.KeyboardButton('Рейд')
        item2 = types.KeyboardButton('События')
        item3 = types.KeyboardButton('Клановые задания')
        item4 = types.KeyboardButton('Полезные ссылки')
        item5 = types.KeyboardButton('❗Информация и другие проекты❗')

        markup.add(item1, item2, item3, item4, item5) 
        bot.send_message(message.chat.id, 'Выберите интересующий пункт меню:', reply_markup = markup)

# тык
    elif message.text == 'тык':
        gif = open ('Гиф/mp4.mp4', 'rb')
        bot.send_animation(message.chat.id, gif, caption = 'цап')

#рейд
    elif message.text == 'Рейд':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Клановый рейд')
        item2 = types.KeyboardButton('Гоблинус')
        item3 = types.KeyboardButton('ИК и Сунь Укун')
        back = types.KeyboardButton('⬅️ Меню')
           
        markup.add(item1, item2, item3, back)
           
        
        bot.send_message(message.chat.id, '⚔Рейд⚔', reply_markup = markup)

# события 
    elif message.text == 'События':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        item1 = types.KeyboardButton('Все события')
        item2 = types.KeyboardButton('Бальтазар')
        item3 = types.KeyboardButton('Сандариэль')
        item4 = types.KeyboardButton('Гоблушка')
        back = types.KeyboardButton('⬅️ Меню')

        markup.add(item1, item2, item3, item4, back)

        bot.send_message(message.chat.id, '⚔События⚔', reply_markup = markup)

    elif message.text == 'Все события':
        photo = open ('События/Все.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, "Информация по всем событиям")

    elif message.text == 'Бальтазар':
        photo = open ('События/Бальтазар.jpg', 'rb')
        photo1 = open ('События/Бальтазар1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1, caption = "Таблица по сбору Бальтазара")

    elif message.text == 'Сандариэль':
        photo = open ('События/Сандариэль.jpg', 'rb')
        photo1 = open ('События/Сандариэль1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_photo(message.chat.id, photo1, caption = "Таблица по сбору Сандариэль")

    elif message.text == 'Гоблушка':
        photo = open ('События/Гоблушка.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

#информация
    elif message.text == '❗Информация и другие проекты❗':
        keyboard = types.InlineKeyboardMarkup(row_width=1)  
        url_button1 = types.InlineKeyboardButton(text="Бот по 6 рейду", url="https://t.me/aom6raid_bot")
        url_button2 = types.InlineKeyboardButton(text="Канал с видео по 6 рейду", url="https://t.me/aom6raid")
        url_button3 = types.InlineKeyboardButton(text="Беседа для обсужд", url="https://t.me/aom6raidchat")
        url_button4 = types.InlineKeyboardButton(text="Автор бота", url="https://t.me/demeur97")
        photo = open ('Ссылки/2.jpg', 'rb')
        keyboard.add(url_button1, url_button2, url_button3, url_button4)
        bot.send_photo(message.chat.id, photo, '⚔Если у Вас есть полезная информация, которую можно добавить в бот, то просьба обращаться на @Demeur97', reply_markup=keyboard)

#Полезные ссылки
    elif message.text == 'Полезные ссылки':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        item1 = types.KeyboardButton('Внешние ресурсы')
        item2 = types.KeyboardButton('Каналы в Telegram')
        back = types.KeyboardButton('⬅️ Меню')
           
        markup.add(item1, item2, back)
           
        bot.send_message(message.chat.id, 'Выберите вариант ссылок:', reply_markup = markup)

 #Внешние ресурсы
    elif message.text == 'Внешние ресурсы':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="Официальная группа Вконтакте", url="https://vk.com/ageofmagicgame")
        url_button2 = types.InlineKeyboardButton(text="Приложение по использованию меток(анл.)", url="aom-spellbook.firebaseapp.com/#/")
        url_button3 = types.InlineKeyboardButton(text="Age of Magic WIKI(англ.)", url="ageofmagicgame.fandom.com/wiki/Age_of_Magic_Wiki")
        url_button4 = types.InlineKeyboardButton(text="Планировщик ClanWar", url="aomcw.com")
        keyboard.add(url_button1, url_button2, url_button3, url_button4)
        photo = open ('Ссылки/1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, "<strong>⚔Полезные ссылки:</strong>", parse_mode="html", reply_markup=keyboard)

 # Каналы в Telegram
    elif message.text == 'Каналы в Telegram':
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button1 = types.InlineKeyboardButton(text="Age Of Magic – Новости", url="t.me/age_of_magic_news")
        url_button2 = types.InlineKeyboardButton(text="Мемы от Нимфы, Ярги, VICTORY и Ко!", url="t.me/NimfaAndJargaAOMmem")
        url_button3 = types.InlineKeyboardButton(text="Отзывы о кланах", url="t.me/joinchat/S1VR7u0omDE_Kywu")
        url_button4 = types.InlineKeyboardButton(text="AomSOCIAL", url="t.me/aomSocial")
        keyboard.add(url_button1, url_button2, url_button3, url_button4)
        photo = open ('Ссылки/2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, "<strong>⚔Список каналов AoM в Telegram:</strong>", parse_mode="html", reply_markup=keyboard)

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
        item1 = types.KeyboardButton('Рейд')
        item2 = types.KeyboardButton('События')
        item3 = types.KeyboardButton('Клановые задания')
        item4 = types.KeyboardButton('Полезные ссылки')
        item5 = types.KeyboardButton('❗Информация и другие проекты❗')
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, '⬅️ Меню', reply_markup = markup)


# клановый рейд
    elif message.text == 'Клановый рейд':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard = True)
        item1 = types.KeyboardButton('Схема 1 рейда')
        item2 = types.KeyboardButton('Схема 2 рейда')
        item3 = types.KeyboardButton('Схема 3 рейда')
        item4 = types.KeyboardButton('Схема 4 рейда')
        item5 = types.KeyboardButton('Схема 5 рейда')
        item6 = types.KeyboardButton('Схема 6 рейда')
        raid = types.KeyboardButton('⬅ Рейд')
        markup.add(item1, item2, item3, item4, item5, item6, raid)
        bot.send_message(message.chat.id, 'Какая схема Вас интересует?', reply_markup = markup)
    elif message.text == 'Схема 1 рейда':
        photo = open ('raid/Клановый рейд/1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Схема 1 рейда')
    elif message.text == 'Схема 2 рейда':
        photo = open ('raid/Клановый рейд/2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Схема 2 рейда')
    elif message.text == 'Схема 3 рейда':
        photo = open ('raid/Клановый рейд/3.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Схема 3 рейда')
    elif message.text == 'Схема 4 рейда':
        photo = open ('raid/Клановый рейд/4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Схема 4 рейда')
    elif message.text == 'Схема 5 рейда':
        photo = open ('raid/Клановый рейд/5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Схема 5 рейда')
    elif message.text == 'Схема 6 рейда':
        photo = open ('raid/Клановый рейд/6.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Схема 6 рейда')

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
#амадеус
    elif message.text == 'Амадеус':
        bot.send_message(message.chat.id, '⚔Раздел находится в разработке')
    elif message.text == 'Amadeus':
        bot.send_message(message.chat.id, '⚔Раздел находится в разработке')

bot.polling(none_stop=True)
