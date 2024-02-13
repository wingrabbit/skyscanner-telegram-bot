import requests
from config import DAO_server_URL, DAO_raw_requests_URL, DAO_raw_requests_status_URL

def check_done_requests() -> [dict]:
    url=f'{DAO_server_URL}{DAO_raw_requests_status_URL}/DONE'
    x = requests.get(url)
    result_json = x.json()
    return result_json

def update_raw_request(id, status, search_id):
    url = f"{DAO_server_URL}{DAO_raw_requests_URL}/{id}/update?status={status}&search_id={search_id}"
    attempt = requests.get(url)
    result_json = attempt.json()
    return result_json