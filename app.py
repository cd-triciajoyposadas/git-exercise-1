from flask import Flask, Blueprint, url_for, request, render_template, redirect, abort, session
from pymongo import MongoClient
import json
from blueprints.fruits.fruits_api import FRUITS_API

SECRET_KEY = 'development key'


app = Flask(__name__,)

# Register blueprints


app.register_blueprint(FRUITS_API, url_prefix = '/fruits')


if name == "__main__":
	app.secret_key = SECRET_KEY
	app.run(debug=True)