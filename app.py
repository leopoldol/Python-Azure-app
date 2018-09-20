from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<center><h1>Hola mundo!</h1><br><h2>LASO Consulting SA de CV</h2></center>"