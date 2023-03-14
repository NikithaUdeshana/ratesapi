from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from controllers.rate_controller import RateList

#loads environtment variables from .env file
load_dotenv()

app = Flask(__name__)
api = Api(app)

api.add_resource(RateList, "/rates/")

if __name__ == "__main__":
    app.run(debug=True)