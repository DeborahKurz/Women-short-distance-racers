#put the scraped data in the db (scraper.py)
from flask import Flask
from sqlalchemy_serializer import SerializerMixin
from config import db

class Athlete(db.Model, SerializerMixin):
    __tablename__='athletes'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.String)
    distance = db.Column(db.Integer)

    def __repr__(self):
        return f'<Athlete {self.id}, {self.name}, {self.rank}, {self.dob}, {self.distance}'