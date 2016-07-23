from flask import Flask, url_for, request
from blueprints.band_blueprint import BAND_API

app = Flask(__name__,)

# Register blueprints
app.register_blueprint(BAND_API, url_prefix = '/band')


if __name__ == "__main__":
	app.run(debug=True)