from flask import Flask, render_template, request, jsonify
import os
from pymongo import MongoClient
from bson import Binary, Code, ObjectId
from bson.json_util import dumps

client = MongoClient()

client = MongoClient('localhost', 27017)
db = client.creature_feature


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('homepage.html')

@app.route("/register")
def getRegister():
    return render_template('register.html')

@app.route("/register", methods=['POST'])
def register():
    data = request.get_json(force=True)
    print data
    data['monster'] = {}
    data['monster']['status'] = 1
    data['goal'] = 0
    data['completed'] = 0
    _id = db.user.insert(data)
    if _id:
        user = db.user.find_one({'_id': ObjectId(_id)})
        return dumps(user)
    else:
        return dumps({'status': 'failed'})

@app.route("/login")
def getLogin():
    return render_template('user.html')

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json(force=True)
    print data
    user = db.user.find_one({'email': data['email'], 'password': data['password']})
    return dumps({'user': user})

@app.route("/goal")
def getGoal():
    return render_template('goal.html')

@app.route("/setgoal/<id>", methods=['POST'])
def setgoal(id):
    data = request.get_json(force=True)
    goal = int(data['goal'])
    db.user.update_one({'_id': ObjectId(id)}, {'$set': {'goal': goal}})
    return jsonify({'status': 'ok'})

@app.route("/user/<id>")
def user(id):
    user = db.user.find_one({'_id': ObjectId(id)})
    if user:
        return render_template('dashboard.html', dumps({'user': user}))

@app.route("/action/<id>")
def action(id):
    import pdb; pdb.set_trace()
    db.user.update_one({'_id': ObjectId(id)}, {'$inc': {'completed': 1}})
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
