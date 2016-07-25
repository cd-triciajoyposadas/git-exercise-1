from flask import Flask, url_for, request, render_template, redirect, abort, session, Blueprint
import json
from pymongo import MongoClient

client = MongoClient()
db = client.building

http_status_code = {(201, 'Created'): "The building was successfully added",
                    (200, 'OK'): "The building was successfully edited",
                    (200, 'OK'): "The building was successfully deleted"}
http_stuff = {'add':{'code':[201,'Created'], 'message': "The building was successfully added"},
              'edit':{'code':[200,'OK'], 'message': "The building was successfully edited"},
              'delete':{'code':[200,'OK'], 'message': "The building was successfully deleted"}}
#http_stuff['delete']=['code': [200, 'OK'], 'message': "deleted"]
# http_stuff['delete']='code'[200, 'OK']
# http_stuff.message['delete']= "The building was successfully deleted"

building_list = {}

building_id = 1
new_building = db.building.insert_one({'name':'primus', 'locat': 'tarlac', 'year': '1996', 'type': 'pogi'})
buildings = db.building.find()
for word in buildings:
    print word

#
# building_list['1'] = new_building

# building_id = 2
# newer_building = {'name':'primus2', 'locat': 'tarlac2', 'year': '1997', 'type': 'mas pogi'}
# building_list[str(building_id)]= newer_building
#
# old_building_list = {}
# old_building_list = building_list
# building_id_delete = 2
#
# building_list = {}
# #search how to search name in this shit
# # for word in old_building_list['/name']:
# #     print old_building_list[str(i)]
# #     if i != building_id_delete:
# #
# #         building_list[str(i)] = old_building_list[str(i)]
# print building_list
#
# json_building_list = json.dumps(building_list)
#
# print type(json_building_list)
#
# json_http_stuff = json.dumps(http_stuff)
#
# #print type(http_stuff)
#
# #print http_status_code[201, 'Created']
# #print http_stuff['add']
# #print http_stuff['edit']
# #print http_stuff['delete']
# #print json_http_stuff
# #print json.loads(json_http_stuff)['add']
# #print json.loads(json_http_stuff)['edit']
# #print json.loads(json_http_stuff)['delete']
#
# #print building_list['1']
# print json.loads(json_building_list)
