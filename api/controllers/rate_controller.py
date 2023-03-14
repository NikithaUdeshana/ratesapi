from flask import request
from flask_restful import Resource
from services.rate_service import Rates

class RateList(Resource):

    def get(self):
        self.date_from = request.args.get('date_from', None)
        self.date_to = request.args.get('date_to', None)
        self.origin = request.args.get('origin', None)
        self.destination = request.args.get('destination', None)

        if not (self.date_from and self.date_to and self.origin and self.destination):
            return {"error": "Missing one or more required parameters."}, 400 
        rates = Rates(self.date_from, self.date_to, self.origin, self.destination).get_average_rates()
        if rates is None:
            return {"error": "Internal Server Error"}, 500
        return rates