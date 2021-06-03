import flask
from flask import redirect
from flask import url_for
from MLv1.py import recognise

face = flask.Flask(__name__)
def hui(rr):
	return rr


@face.route("/")
def home():
	return """
<h1>
	Hello! Welcome to FACE!
</h1>
<h2>
	<ul>
	<li>Face-recognition</li>
	<li>AI for</li>
	<li>Communicating</li>
	<li>Emotions</li>
	</ul>
</h2>
<script>
alert("Looking for our app? Click on that link below!")
</script>
<a href="/app">Visit our app!</a>
	"""

@face.route("/app/")
def app():
	return "Work in progress"

@face.route("/<lost>")
def lostpage(lost):
	return """
<script>
alert("Looks like this webpage was eaten by our resident cat!")
</script>
<img src=https://www.flickr.com/photos/18090920@N07/4615840388 alt = "Meow?">
<style>
body {
  background-image: https://www.flickr.com/photos/18090920@N07/4615840388;
}
</style>
"""

if __name__ == "__main__":
	face.run()
#python FlaskTutorial.py
