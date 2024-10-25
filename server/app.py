from flask import Flask, request, make_response, jsonify
from flask_restful import Resource
from config import app, db

from models import Athlete

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5555, debug=True)