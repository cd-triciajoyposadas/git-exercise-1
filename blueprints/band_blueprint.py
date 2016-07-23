from flask import Flask, Blueprint, request, abort, session, jsonify, redirect, url_for
import pymongo
from pymongo import MongoClient
import json


BAND_API = Blueprint('BAND_API', __name__)

#KEYS
DATA = 'data'
BAND_NAME = 'band_name'
BAND_GENRE = 'band_genre'
BAND_MEMBERS = 'band_members'
BAND_BIRTHYEAR = 'band_birthyear'

#CREATE CONNECTION
client = MongoClient()
db = client[DATA]

@BAND_API.route('/list/')
def get_band_list():

	cursor = db.bands.find()

	output = [{
		BAND_NAME : attr[BAND_NAME],
		BAND_GENRE : attr[BAND_GENRE], 
		BAND_MEMBERS : attr[BAND_MEMBERS],
		BAND_BIRTHYEAR : attr[BAND_BIRTHYEAR]
		} for attr in cursor]


	return jsonify(output)


@BAND_API.route('/add/', methods = ["POST"])
def add_band():

	if request.form:
		band_name = request.form[BAND_NAME]
		band_genre = request.form[BAND_GENRE]
		band_members = request.form[BAND_MEMBERS]
		band_birthyear = request.form[BAND_BIRTHYEAR]

		if db.bands.find_one({BAND_NAME : band_name}):
			return jsonify(response = band_name + " band already exists.")
		else:
			post_band = {
				BAND_NAME: band_name,
				BAND_GENRE: band_genre,
				BAND_MEMBERS: band_members,
				BAND_BIRTHYEAR: band_birthyear
				}

			result_post = db.bands.insert_one(post_band)

			return jsonify(http_status_code = (201, "Created"), message = "The "+band_name+" band was successfully added")\
			if result_post else jsonify(message = "failed adding new band")
	else:
		return jsonify(response = "NO DATA RECIEVED")


@BAND_API.route('/edit/', methods = ["POST"])
def edit_band_info():

	if request.form:
		band_name = request.form[BAND_NAME]
		band_genre = request.form[BAND_GENRE]
		band_members = request.form[BAND_MEMBERS]
		band_birthyear = request.form[BAND_BIRTHYEAR]

		result_post = db.bands.update_one(
			{BAND_NAME : band_name},
			{
			"$set": {
				BAND_GENRE: band_genre,
				BAND_MEMBERS: band_members,
				BAND_BIRTHYEAR: BAND_BIRTHYEAR
			}
			}
			)
		return jsonify(http_status_code = (200, "OK"), message = "The "+band_name+" band was successfully updated")\
			if result_post else jsonify(message = "failed to update band") 
	else:
		return jsonify(response = "NO DATA RECIEVED")


@BAND_API.route('/delete/', methods = ["POST"])
def delete_band_here():

	if request.form:
		band_name = request.form[BAND_NAME]

		result_post = db.bands.delete_one({BAND_NAME : band_name})

		return jsonify(http_status_code = (200, "OK"), message = "The "+band_name+" band was successfully deleted")\
			if result_post else jsonify(message = "failed to delete band") 
	else:
		return jsonify(response = "NO DATA RECIEVED")

