from flask import Flask, request, make_response, jsonify
from flask_restful import Resource
from config import app, db

from models import Athlete

with app.app_context():
    db.create_all()

class AthleteResource(Resource):
    def get(self):
        try:
            athletes = Athlete.query.all()

            response = [athlete.to_dict() for athlete in athletes]
            return response, 200
        except Exception as e:
            return {"error": f"Error: {e}"}, 400
           

if __name__ == '__main__':
    app.run(port=5555, debug=True)