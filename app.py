from flask import Flask

app = Flask(__name__,)

# Register blueprints

if __name__ == "__main__":
	app.run(debug=True)