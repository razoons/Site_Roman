from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

users = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajouter")
def ajouter():
    return render_template("ajouter.html")

@app.route("/liste")
def liste():
    return render_template("liste.html")

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    users.append(data)
    return data, 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
