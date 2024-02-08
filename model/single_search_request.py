class SingleSearchRequest:
    def __init__(self, city_from, city_to, date_start, date_end, days_min, days_max, id=None):
        self.city_from = city_from
        self.city_to = city_to
        self.date_start = date_start
        self.date_end = date_end
        self.days_min = days_min
        self.days_max = days_max
        self.id = id

    def __str__(self):
        return f"SingleSearchRequest(city_from={self.city_from}, city_to={self.city_to}, " \
               f"date_start={self.date_start}, date_end={self.date_end}, days_min={self.days_min}, " \
               f"days_max={self.days_max}, id={self.id})"
