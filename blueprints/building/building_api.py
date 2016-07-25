from flask import Flask, url_for, request, render_template, redirect, abort, session, Blueprint
from pymongo import MongoClient
from flask import json, jsonify
from bson import BSON, json_util

BUILDING_API = Blueprint('BUILDING_API', __name__)

# http_status = {'add':{'http_status_code':(201,'Created'), 'message': "The building was successfully added"},
#               'edit':{'http_status_code':(200,'OK'), 'message': "The building was successfully edited",},
#               'delete':{'http_status_code':(200,'OK'), 'message': "The building was successfully deleted"}}

#json_http_status = json.dumps(http_status)

client = MongoClient()
db = client.entity
# hmm convert siguro json or idk
# retrieve data from server
# convert to python
# add to dicts


@BUILDING_API.route('/list')
def list_buildings():

    # buildings = {}
    # _idman = 1
    # for word in
    #
    #
    #     buildings = word
    buildings = [json.loads(json_util.dumps(build, sort_keys=True, indent=4)) for build in db.building.find()]


#    return jsonify(buildings)

#    return jsonify(buildings)
#, sort_keys=True, indent=4, default=json_util.default)

@BUILDING_API.route('/add', methods=['POST'])
def add_building():

    building_name = request.form['building_name']
    building_location = request.form['building_location']
    building_year = request.form['building_year']
    building_type = request.form['building_type']

    # add to database
    new_building = db.building.insert_one(
        {'building_name': building_name,
         'building_location': building_location,
         'building_year': building_year,
         'building_type': building_type})

    response = {'http_status_code': (
        201, 'Created'), 'message': "The building was successfully added"}
    if new_building.acknowledged:
        return jsonify(response)


@BUILDING_API.route('/edit', methods=['POST'])
def edit_building():

    # find the shiz
    # edit the shiz

    building_name = request.form['building_name']
    building_location = request.form['building_location']
    building_year = request.form['building_year']
    building_type = request.form['building_type']


    db.building.update(
    {"building_name" : building_name},
    { "$set": { "building_year": building_year, "building_type": building_type, "building_location": building_location}})

    response = {'http_status_code': (200, 'OK'), 'message': "The building was successfully edited", }

    #modified = WriteResult.getN()
    if db.building.acknowledged:
        return jsonify(response)


@BUILDING_API.route('/delete', methods=['POST'])
def delete_building():

    # find the shiz
    # delete the shiz

    building_name = request.form['building_name']
    building_location = request.form['building_location']
    building_year = request.form['building_year']
    building_type = request.form['building_type']

    db.building.remove( { "building_name": building_name }, { 'justOne': 'True' } )

    response = {'http_status_code': (200, 'OK'), 'message': "The building was successfully deleted"}
    if db.building.acknowledged:
        return jsonify(response)
