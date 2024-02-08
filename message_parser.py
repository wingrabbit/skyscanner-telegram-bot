from model.single_search_request import SingleSearchRequest
from processing.dates_processing import convert_date_to_default_format

def parse_raw_single_search_request(message) -> SingleSearchRequest:
    try:
        parts = message.text.split()
        return SingleSearchRequest(parts[0], 
                                   parts[1], 
                                   convert_date_to_default_format(parts[2]), 
                                   convert_date_to_default_format(parts[3]), 
                                   parts[4], 
                                   parts[5],
                                   message.chat.id)
    except:
        return None