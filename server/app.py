from flask import Flask, request, make_response, jsonify
from flask_restful import Resource
from config import app, db, api


if __name__ == '__main__':
    app.run(port=5555, debug=True)