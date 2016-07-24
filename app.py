from flask import Flask, Blueprint, url_for, render_template,request, abort, session, redirect, jsonify
import pymongo
from pymongo import MongoClient
import json
from blueprints.hero.superhero_api import SUPERHERO_API

SECRET_KEY = 'a\xa0\xad\xf5FuZ\x83\x04\xba'
app = Flask(__name__,)


#register a blueprint
app.register_blueprint(SUPERHERO_API, url_prefix='/hero')


if __name__ == "__main__":
	app.secret_key = SECRET_KEY
	app.run(debug=True)
