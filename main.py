import telebot
from threading import Thread
import time

from config import BOT_TOKEN

from dao_communication.requests_checkout import check_done_requests, update_raw_request
from dao_communication.prices_checkout import get_best_prices

from message_parser import parse_raw_single_search_request
from processing.message_processing import process_raw_single_search_request
from processing.results_processing import best_prices_text




bot = telebot.TeleBot(BOT_TOKEN)

def background_check():
    while(True):
        done_requests = check_done_requests()
        for raw_request in done_requests:
            bot.send_message(raw_request["chat_id"], f'DONE: {raw_request["request"]}')
            update_raw_request(raw_request["id"], 'SENT', raw_request["search_id"])
            prices = get_best_prices(raw_request["search_id"])
            bot.send_message(raw_request["chat_id"], best_prices_text(prices))
        time.sleep(1)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, process_raw_single_search_request(message))

Thread(target=lambda: background_check()).start()
bot.infinity_polling()
