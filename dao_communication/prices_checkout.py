import requests
from config import DAO_server_URL, DAO_search_result_URL

def get_best_prices(search_id) -> []:
    url=f'{DAO_server_URL}{DAO_search_result_URL.replace("search_id", str(search_id))}'
    x = requests.get(url)
    result_json = x.json()
    return result_json