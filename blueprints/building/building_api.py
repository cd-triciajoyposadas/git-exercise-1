from flask import Flask, url_for, request, render_template, redirect, abort, session, Blueprint
from pymongo import MongoClient
from flask import json

BUILDING_API = Blueprint('BUILDING_API', __name__)

# http_status = {'add':{'http_status_code':(201,'Created'), 'message': "The building was successfully added"},
#               'edit':{'http_status_code':(200,'OK'), 'message': "The building was successfully edited",},
#               'delete':{'http_status_code':(200,'OK'), 'message': "The building was successfully deleted"}}

#json_http_status = json.dumps(http_status)

client=MongoClient()
db = client.entity
#hmm convert siguro json or idk
#retrieve data from server
#convert to python
#add to dicts

@BUILDING_API.route('/list')
def list_buildings():

    buildings = [word for word in db.entity.building.find( { type: '_id' }, { type:0 } )]
    return 'hahahaha'
    return json.dumps(buildings)

@BUILDING_API.route('/add', methods=['POST'])
def add_building():

    building_name = request.form['building_name']
    building_location = request.form['building_location']
    building_year = request.form['building_year']
    building_type = request.form['building_type']

    #add to database
    new_building = db.entity.building.insert_one({'building_name': building_name,
                    'building_location': building_location,
                    'building_year': building_year,
                    'building_type': building_type})

    response = {'http_status_code':(201,'Created'), 'message': "The building was successfully added"}
    if new_building.acknowledged:
        return json.dumps(response)

@BUILDING_API.route('/edit')
def edit_building():

    #find the shiz
    #edit the shiz

    response = {'http_status_code':(200,'OK'), 'message': "The building was successfully edited",}

    return json.dumps(response)

@BUILDING_API.route('/delete')
def delete_building():



    #find the shiz
    #delete the shiz
    response = {'http_status_code':(200,'OK'), 'message': "The building was successfully deleted"}

    return json.dumps(response)
