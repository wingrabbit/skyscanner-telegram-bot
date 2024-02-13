import requests
from config import DAO_server_URL, DAO_raw_requests_URL
from message_parser import parse_raw_single_search_request
from model.single_search_request import SingleSearchRequest

def process_raw_single_search_request(message):
    if parse_raw_single_search_request(message) is not None:
        url=f'{DAO_server_URL}{DAO_raw_requests_URL}'
        request_json = {"chat_id": message.chat.id, "request":message.text, "status": "NEW"}
        x = requests.post(url, json=request_json)
        print(x)
    return "Sent to the server"