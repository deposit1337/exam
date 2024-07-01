import telebot
import config
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет, добро пожаловать!')
def handle_aue(message):
    bot.reply_to(message, "Вы написали: " + message.text)


bot.polling()