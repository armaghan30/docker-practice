from flask import Flask 

app = Flask (__name__)

@app.route("/")
def home():
	return "Hello I am Armaghan and this my first container!"

app.run(host="0.0.0.0", port=5000)
