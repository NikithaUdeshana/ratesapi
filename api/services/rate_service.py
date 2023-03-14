from datetime import datetime, timedelta
from utils.db_utils import Database
from utils.constants import DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT

class Rates():

    def __init__(self, date_from, date_to, origin, destination):
        self.date_from = date_from
        self.date_to = date_to
        self.origin = origin
        self.destination = destination

    def average(self, total, count):
        if count > 2:
            return round(total/count, 0)
    
    def get_date_range(self, date_from, date_to):
        start_date = datetime.strptime(date_from, '%Y/%m/%d')
        end_date = datetime.strptime(date_to, '%Y/%m/%d')
        return int((end_date - start_date).days) + 1
    
    def get_average_rates(self):
        rates = []
        rows = Database(DB_NAME, 
                        DB_USERNAME, 
                        DB_PASSWORD, 
                        DB_HOST, 
                        DB_PORT).fetch_rates(self.date_from, self.date_to, self.origin, self.destination)
        if rows is None:
            return None
        for i in range(self.get_date_range(self.date_from, self.date_to)):
            total = 0
            counts = 0
            date = (datetime.strptime(self.date_from, '%Y/%m/%d') + timedelta(days=i))
            for day, price in rows:
                if date.strftime("%Y-%m-%d") == day.strftime("%Y-%m-%d"):
                    total += price
                    counts += 1
            rates.append({"day" : date.strftime("%Y-%m-%d"), "average_price": self.average(total, counts)})
        return rates