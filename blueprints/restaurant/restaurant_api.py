# Restaurant API
from flask import Flask, Blueprint, url_for, request, abort

RESTAURANT_API = Blueprint('RESTAURANT_API', __name__)

@RESTAURANT_API.route('/list/')
def get_restaurants():

	return "LIST ENDPOINT"

@RESTAURANT_API.route('/add/')
def add_restaurant():

	return 'ADD ENDPOINT'

@RESTAURANT_API.route('/edit/')
def edit_restaurant():

	return 'EDIT ENDPOINT'

@RESTAURANT_API.route('/delete/')
def delete_restaurant():

	return 'DELETE ENDPOINT'
