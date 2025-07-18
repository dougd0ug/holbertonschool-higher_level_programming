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
    return jsonify(list(users.keys()))


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
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
