import telebot
from threading import Thread
import time

from config import BOT_TOKEN
from message_parser import parse_raw_single_search_request
from processing.message_processing import process_raw_single_search_request

def background_check():
    while(True):
        time.sleep(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, process_raw_single_search_request(message))

Thread(target=lambda: background_check()).start()
bot.infinity_polling()
