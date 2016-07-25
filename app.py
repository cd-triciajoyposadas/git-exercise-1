from flask import Flask, url_for, request, render_template, redirect, abort, session, Blueprint
from blueprints.building.building_api import BUILDING_API
from pymongo import MongoClient
from flask import json

app = Flask(__name__,)

# Register blueprints
app.register_blueprint(BUILDING_API, url_prefix = "/building")

if __name__ == "__main__":
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run(debug=True)
