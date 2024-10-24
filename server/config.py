# Import necessary libraries
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Create an instance of the Flask application
app = Flask(__name__)

# Configure the application settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///athletes.db'  # Specify your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources
app.json.compact = False  # Set JSON output to be more readable

# Define a metadata naming convention for the database
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # Foreign key naming convention
})

# Initialize the SQLAlchemy instance with the metadata
db = SQLAlchemy(metadata=metadata)

# Setup migration handling
migrate = Migrate(app, db)

# Initialize the API for RESTful routes
api = Api(app)

# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app)

# Initialize the database with the app
db.init_app(app)
