import telebot

from config import BOT_TOKEN
from message_parser import parse_raw_single_search_request

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, parse_raw_single_search_request(message.text))

bot.infinity_polling()