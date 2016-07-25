#SUPERHERO
from flask import Flask, Blueprint, url_for, render_template,request, abort, session, redirect, jsonify
from pymongo import MongoClient
import json

SUPERHERO_API = Blueprint('SUPERHERO_API', __name__)

client = MongoClient()
db = client['entity']

@SUPERHERO_API.route('/')
def get_home():
	return render_template('hero_home.html')


@SUPERHERO_API.route('/list/',strict_slashes=False, methods=["POST"])
def get_superhero():

	ctr = db.hero.find()
 	output = [{
 		'realname' : items['h_realname'],
 		'allias' : items['h_allias'], 
 		'ability' : items['h_ability'],
 		'city' : items['h_city']
 		} for items in ctr]

 	return jsonify(output)

@SUPERHERO_API.route('/add/',strict_slashes=False, methods=["POST", "GET"])
def add_superhero():
	if request.method == 'GET':

		return render_template('add_superheroes.html')
	elif request.method == 'POST':

		if request.form:
 			h_realname = request.form['h_realname']
 			h_allias = request.form['h_allias']
 			h_ability = request.form['h_ability']
 			h_city = request.form['h_city']

 			if db.hero.find_one({'h_realname' : h_realname}):
 				return jsonify(response = h_realname + " hero na po sya.")
 			else:
 				post_hero = {
 					'h_realname': h_realname,
 					'h_allias': h_allias,
 					'h_ability': h_ability,
 					'h_city': h_city
 					}

 				result_post = db.hero.insert_one(post_hero)

 				return jsonify(http_status_code = (201, "Created"), message = h_realname+" as "+h_allias.upper()+" added")\
 					if result_post else jsonify(message = "can't add try again")
 		else:
 			return jsonify(response = "ERROR")
	#return 'add all heroes here :('
	#return render_template('add_superheroes.html')
@SUPERHERO_API.route('/edit/',strict_slashes=False, methods=["POST"])
def edit_superhero():
	if request.form:
 		h_realname = request.form['h_realname']
 		h_allias = request.form['h_allias']
 		h_ability = request.form['h_ability']
 		h_city = request.form['h_city']

 		result_post = db.hero.update_one(
 			{'h_realname' : h_realname},
 			{
 			"$set": {
 				'h_allias': h_allias,
 				'h_ability': h_ability,
 				'h_city': h_city
 			}
 			}
 			)
 		return jsonify(http_status_code = (200, "OK"), message = h_realname+" updated luhh..")\
 			if result_post else jsonify(message = "try again, can't updated") 
 	else:
 		return jsonify(response = "ERROR")

@SUPERHERO_API.route('/delete/',strict_slashes=False, methods = ["POST"])
def delete_superhero():

 	if request.form:
 		h_realname = request.form['h_realname']

 		result_post = db.hero.delete_one({'h_realname' : h_realname})

 		return jsonify(http_status_code = (200, "OK"), message = h_realname+" deleted luhh..")\
 			if result_post else jsonify(message = "can't delete.") 
 	else:
 		return jsonify(response = "ERROR")


