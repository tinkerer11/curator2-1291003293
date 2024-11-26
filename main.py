from telebot import TeleBot

bot = TeleBot('7640388122:AAEM9SoqVP6tmltaGW6R-vTsiuaDpvTnThE')


# обработка новой команды


@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id,  'Привет! Я цундере-бот!\nЯ могу поделиться сайтами для просмотра аниме!')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Напиши единицу, если нужен сайт, для просмотра аниме с субтитрами.\n'
                                               'Напиши двойку, если нужен сайт, где можно посмотреть аниме в русской озвучке')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')


@bot.message_handler(commands=['1'])
def subtitles(message):
    bot.send_message(message.chat.id, 'Приятного просмотра! https://animego.cx/anime/translator/subtitle/')

@bot.message_handler(commands=['2'])
def voice_acting(message):
    bot.send_message(message.chat.id, 'Держи! https://jut-su.sbs/')

bot.infinity_polling()