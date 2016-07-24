from flask import Flask,Blueprint,url_for,request,render_template,redirect,abort, \
session
from pymongo import MongoClient
c = MongoClient()
import json
from bson import json_util

FUNCTIONS_API = Blueprint('FUNCTIONS_API',__name__)


@FUNCTIONS_API.route('/add',methods = ["POST"])
def add():
		name = request.form['name']
		atype = request.form['type']
		color = request.form['color']
		age = request.form['age']

		c.entity.animals.insert_one({"Name" : name, "Type" : atype, "Color" : color, "Age" : age})

		return "Data has been added."
		# return render_template('add.html')
	
@FUNCTIONS_API.route('/delete',methods = ["POST"])
def delete():
	name = request.form['name']
	
	c.entity.animals.remove({"Name": name})

	return "Data has been deleted."
	# return render_template('delete.html')

@FUNCTIONS_API.route('/edit',methods = ["POST"])
def edit():
	name = request.form['name']
	atype = request.form['type']
	color = request.form['color']
	age = request.form['age']

	c.entity.animals.update ({"Name" : name},{"Name" : name, "Type" : atype, "Color" : color, "Age" : age})

	return "Data has been edited."
	# return render_template('edit.html')

@FUNCTIONS_API.route('/list')
def list():
	data = [i for i in c.entity.animals.find({}, {'_id': False})]
	
	return json.dumps(data,  sort_keys=True, indent=4, default=json_util.default)

