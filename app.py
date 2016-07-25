from flask import Flask, url_for, request, abort
from blueprints.restaurant.restaurant_api import RESTAURANT_API
from blueprints.band_blueprint import BAND_API

app = Flask(__name__,)

# Register blueprints

app.register_blueprint(RESTAURANT_API, url_prefix= '/restaurant')
app.register_blueprint(BAND_API, url_prefix = '/band')


if __name__ == "__main__":
	app.run(debug=True)

