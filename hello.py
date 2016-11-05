from flask import Flask
import os
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
db = client.creature_feature


app = Flask(__name__)

@app.route("/")
def hello():
    return "GRRRRRRRR"

@app.route("/register")
def register():
    return "SIGN UP"

@app.route("/login")
def login():
    return "LOGIN"

@app.route("/setgoal")
def setgoal():
    return "SET GOAL"

@app.route("/user/<id>")
def user(id):
    return "HELLO USER %s" % id

@app.route("/action")
def action():
    return "YOU DID AN ACTION"

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
