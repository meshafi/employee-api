from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/EmployeeDB'
mongo = PyMongo(app)

from app.routes.employee_routes import *
