# Restaurant API
# Sample input - name: Jollibee, branch: 5th Ave. BGC, operating_hours: 24hours, classification: fine dining
from flask import Flask, Blueprint, url_for, request, abort, json, Response
from pymongo import MongoClient

RESTAURANT_API = Blueprint('RESTAURANT_API', __name__)

client = MongoClient()
db = client.entity #db
restaurant = db.restaurant #collection

@RESTAURANT_API.route('/list')
def get_restaurants():

	#display auto incremented number(_uid) instead of ObjectId(_id)
	restaurants = restaurant.find({}, {'_id':0})
	restaurant_list = [i for i in restaurants]

	return Response(json.dumps(restaurant_list),  mimetype='application/json')

@RESTAURANT_API.route('/add', methods = ['POST'])
def add_restaurant():
	if request.form:
		#required http body
		name = request.form['name']
		branch = request.form['branch']
		operating_hours = request.form['operating_hours']
		classification = request.form['classification']

		# name and branch must be unique
		if restaurant.find_one({'name': name, 'branch': branch}):

 			return Response(json.dumps({"Duplicate error": "Data cannot be repeated."}),  mimetype='application/json')

 		else:

 			#set _uid to auto incremented numbers
			db.counters.insert(
			   {
			      "_uid": "userid",
			      "seq": 0
			   }
			)

			ret = db.counters.find_and_modify(
		        query = { "_uid": "userid" },
		        update = { "$inc": { "seq": 1 } },
		        new = True
		   	).get('seq')

			result = restaurant.insert_one({ "_uid": ret, "name": name, "branch": branch, "operating_hours": operating_hours, "classification": classification})

			# insert_one returns acknowledged = true else false
			if(result.acknowledged):
				response = json.dumps({"http_status_code": [ 201, "Created" ],"message": "The "+name+" restaurant was successfully added."})
				return Response(response,  mimetype='application/json')
			else:
			    response = json.dumps({"message": "Failed to add restaurant."})
			    return Response(response,  mimetype='application/json')
	else:
		return Response(json.dumps({"error": "Please input data."}),  mimetype='application/json')

@RESTAURANT_API.route('/edit', methods = ['POST'])
def edit_restaurant():
	if request.form:
		# required http body
		name = request.form['name']
		branch = request.form['branch']
		operating_hours = request.form['operating_hours']
		classification = request.form['classification']

		#check if data exist
		if restaurant.find_one({'name': name, 'branch': branch}):

			# update data from unique name and branch
			result = restaurant.update_one({"name": name, "branch": branch}, {"$set": { "operating_hours": operating_hours, "classification": classification}})

			# update_one returns acknowledged = true else false
			if(result.acknowledged):
				response = json.dumps({"http_status_code": [ 200, "OK" ],"message": "The "+name+" restaurant was successfully updated."})
				return Response(response,  mimetype='application/json')
			else:
			    response = json.dumps({"message": "Failed to update restaurant."})
			    return Response(response,  mimetype='application/json')

		else:
			return Response(json.dumps({"error": "Data do not exist."}),  mimetype='application/json')

	else:
		return Response(json.dumps({"error": "Please input data."}),  mimetype='application/json')

@RESTAURANT_API.route('/delete', methods = ['POST'])
def delete_restaurant():

	if request.form:
		#required http body
		name = request.form['name']
		branch = request.form['branch']

		#check if data exist
		if restaurant.find_one({'name': name, 'branch': branch}):

			# delete data from unique name and branch
			result = restaurant.delete_one({'name' : name, 'branch': branch})

			# delete_one returns acknowledged = true else false
			if(result.acknowledged):
				response = json.dumps({"http_status_code": [ 200, "OK" ],"message": "The "+name+" restaurant was successfully deleted."})
				return Response(response,  mimetype='application/json')
			else:
			    response = json.dumps({"message": "Failed to delete restaurant."})
			    return Response(response,  mimetype='application/json')
		else:
			return Response(json.dumps({"error": "Data do not exist."}),  mimetype='application/json')

	else:
		return Response(json.dumps({"error": "Please input data."}),  mimetype='application/json')

