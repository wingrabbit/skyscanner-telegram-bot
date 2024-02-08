from dateutil import parser

def convert_date_to_default_format(date_string):
    try:
        date_object = parser.parse(date_string)
        formatted_date = date_object.strftime("%Y-%m-%d")
        return formatted_date
    except ValueError:
        print("Error: Invalid date format")
        return None