from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def return_data():
    result = jsonify(users)
    return result


@app.route("/status")
def return_status():
    return ("OK")


@app.route("/users/<username>")
def return_users(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data["username"]
    users[username] = data
    return jsonify(data)


if __name__ == "__main__":
    app.run()
