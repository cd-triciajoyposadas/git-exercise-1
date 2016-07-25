from flask import Flask, Blueprint, jsonify,  url_for, request, render_template, redirect, abort, session
from pymongo import MongoClient
import json
# from blueprints.fruits.fruits_api import FRUITS_API

FRUITS_API = Blueprint('FRUITS_API', name)

client = MongoClient()
db = client['fruity']

@FRUITS_API.route('/list/', methods=["POST"])
def get_fruits():

	ctr = db.fruits.find()
 	output = [{
 		'f_name' : items['f_name'],
 		'f_color' : items['f_color'], 
 		'f_price' : items['f_price'],
 		'f_weight' : items['f_weight']
 		} for items in ctr]

 	return jsonify(output)


@FRUITS_API.route('/add/', methods=["POST"])
def fruits_add():

	if request.form:

 		f_name = request.form['f_name']
 		f_color = request.form['f_color']
 		f_price = request.form['f_price']
 		f_weight = request.form['f_weight']

		if db.fruits.find_one({'f_name' : f_name}):
 			
 			return jsonify(response = f_name + " was successfully added.")

 		else:
 			show_fruits = {
 				'f_name': f_name,
 				'f_color': f_color,
 				'f_price': f_price,
 				'f_weight': f_weight
 				}

 			show_post = db.fruits.insert_one(show_fruits)

 			return jsonify( http_status_code = (201, "Created"), message = "The fruit was successfully added")\
 				if show_post else jsonify(message = "sorry can't add that! try again")
 	else:
 		return jsonify(response = "No Data Added Dude!!!")

@FRUITS_API.route('/edit/', methods=["POST"])
def edit_fruits():
	if request.form:
 		f_name = request.form['f_name']
 		f_color = request.form['f_color']
 		f_price = request.form['f_price']
 		f_weight = request.form['f_weight']

 		show_post = db.fruits.update_one(
 			{'f_name' : f_name},
 			{
 			"$set": {
 				'color': h_color,
 				'price': h_price,
 				'weight': h_weight
 			}
 			}
 			)
 		return jsonify(http_status_code = (200, "OK"), message = "Fruits information was successfully edited")\
 			if show_post else jsonify(message = "sorry can't edit that! try again") 
 	else:
 		return jsonify(response = "No Data Edited Dude!!!")

@FRUITS_API.route('/delete/', methods = ["POST"])
def delete_fruits():

 	if request.form:
 		f_name = request.form['f_name']

 		show_post = db.fruits.delete_one({'f_name' : f_name})

 		return jsonify(http_status_code = (200, "OK"), message = f_name+" successfully deleted!!!")\
 			if show_post else jsonify(message = "sorry can't delete that! try again") 
 	else:
 		return jsonify(response = "No Data Deleted Dude!!!")



