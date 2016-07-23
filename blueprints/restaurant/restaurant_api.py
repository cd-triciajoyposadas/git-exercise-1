# Restaurant API
# name and branch must be unique
from flask import Flask, Blueprint, url_for, request, abort, json, make_response
from bson.objectid import ObjectId
from pymongo import MongoClient

RESTAURANT_API = Blueprint('RESTAURANT_API', __name__)

client = MongoClient()
db = client.entity

@RESTAURANT_API.route('/list')
def get_restaurants():

	restaurants = db.entity.find()

	restaurant_list = [i for i in restaurants]

	return json.dumps(restaurant_list)

@RESTAURANT_API.route('/add', methods = ['POST'])
def add_restaurant():
	if request.form:
		name = request.form['name']
		branch = request.form['branch']
		operating_hours = request.form['operating_hours']
		classification = request.form['classification']

		if db.entity.find_one({'name': name, 'branch': branch}):
 			return json.dumps({"Duplicate error": "Data cannot be repeated."})
 		else:
			db.counters.insert(
			   {
			      "_uid": "userid",
			      "seq": 0
			   }
			)

			ret = db.counters.find_and_modify(
		        query = { "_id": "userid" },
		        update = { "$inc": { "seq": 1 } },
		        new = True
		   	).get('seq')

			result = db.entity.insert_one({ "_id": ret, "name": name, "branch": branch, "operating_hours": operating_hours, "classification": classification})

			if(result.acknowledged):
				response = json.dumps({"http_status_code": [ 201, "Created" ],"message": "The "+name+" restaurant was successfully added."})
				return response
			else:
			    response = json.dumps({"message": "Failed to add restaurant."})
			    return response
	else:
		return json.dumps({"error": "Please input data."})

@RESTAURANT_API.route('/edit', methods = ['POST'])
def edit_restaurant():
	if request.form:
		name = request.form['name']
		branch = request.form['branch']
		operating_hours = request.form['operating_hours']
		classification = request.form['classification']

		result = db.entity.update_one({"name": name, "branch": branch}, {"$set": { "operating_hours": operating_hours, "classification": classification}})

		if(result.acknowledged):
			response = json.dumps({"http_status_code": [ 200, "OK" ],"message": "The "+name+" restaurant was successfully updated."})
			return response
		else:
		    response = json.dumps({"message": "Failed to update restaurant."})
		    return response

	else:
		return json.dumps({"error": "Please input data."})

@RESTAURANT_API.route('/delete', methods = ['POST'])
def delete_restaurant():

	if request.form:
		name = request.form['name']
		branch = request.form['branch']

		result = db.entity.delete_one({'name' : name, 'branch': branch})

		if(result.acknowledged):
			response = json.dumps({"http_status_code": [ 200, "OK" ],"message": "The "+name+" restaurant was successfully deleted."})
			return response
		else:
		    response = json.dumps({"message": "Failed to delete restaurant."})
		    return response

	else:
		return json.dumps({"error": "Please input data."})

