from flask import Flask,url_for,request,render_template,redirect,abort, \
session
from blueprints.animals.functions import FUNCTIONS_API

SECRET_KEY = '\x90\xa6E\x8f\xf4\x81\xdd\xdd8u\x0c \x9c\xe4g\xe9\x16\xab\x93\xe4zVp\xd3'
app = Flask(__name__,)

app.register_blueprint(FUNCTIONS_API, url_prefix = "/animals")

if __name__ == "__main__":
	app.secret_key = SECRET_KEY
	app.run(debug=True) 

