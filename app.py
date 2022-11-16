from flask import Flask, render_template, session, request, jsonify
import os
from logic.db_connector import MongoConnection

def create_app():
    app = Flask(__name__)
    app.db = MongoConnection(os.getenv("MONGO_STRING").client)
    connection_string = os.getenv("MONGO_STRING")
    @app.route('/')
    def login():
        form = request.form
        if "user" not in form or "password" not in form:
            return jsonify({
                "status": 500,
                "error": "failed to get user and password from the form"
            })
        user, password = form["user"], form["password"]
        # TODO get all users from DB and check that it belongs
        return render_template('index.html')

    return app
