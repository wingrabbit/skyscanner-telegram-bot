from dao_communication.prices_checkout import get_best_prices

stops_to_text = {0: 'direct', 1: '1 stop', 2: '2+ stops'}

def best_prices_text(src):
    result = f'{src[0][2]} - {src[0][3]} \n'
    for record in src:
        result+=f'${record[4]} {record[0]} - {record[1]} ({stops_to_text[record[5]]}) \n'
    return result