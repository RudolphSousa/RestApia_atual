
from flask import Flask
from flask_restful import Api
from Resources.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)


#class Hoteis(Resource):
#   def get(self):
#       return {'hoteis': hoteis}

api.add_resource(Hoteis,'/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/hoteis


