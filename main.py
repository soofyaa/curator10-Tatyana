import telebot

bot = telebot.TeleBot('6985769803:AAHTmx8MqrKUDSsJndmzcIX6VbVIaEqYbzs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['dalee'])
def main(message):
    bot.send_message(message.chat.id, 'Вы лучшие УМСКУЛ!!!')


@bot.message_handler(commands=['otzyv'])
def main(message):
    bot.send_message(message.chat.id, 'Спасибо большое вам за марофон!Всё очень легко и понятно объясняете.')


bot.infinity_polling()