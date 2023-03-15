import logging
from datetime import datetime
from flask import request
from flask_restful import Resource
from services.rate_service import Rates

class RateList(Resource):

    def validate_date(self, date):
        try:
            print(date)
            return datetime.strptime(date, '%Y/%m/%d')
        except ValueError:
            logging.error("Incorrect data format, should be YYYY/MM/DD")
            return None

    def get(self):
        self.date_from = request.args.get('date_from', None)
        self.date_to = request.args.get('date_to', None)
        self.origin = request.args.get('origin', None)
        self.destination = request.args.get('destination', None)

        if not (self.date_from and self.date_to and self.origin and self.destination):
            return {"error": "Missing one or more required parameters."}, 400 
        if not (self.validate_date(self.date_from) and self.validate_date(self.date_to)):
            return {"error": "Incorrect data format, should be YYYY/MM/DD"}, 400
        
        rates = Rates(self.date_from, self.date_to, self.origin, self.destination).get_average_rates()
        if rates is None:
            return {"error": "Internal Server Error"}, 500
        return rates