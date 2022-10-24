from flask import Flask, render_template, session, request
import os
from logic.db_connector import MongoConnection

def create_app():
    app = Flask(__name__)
    app.db = MongoConnection(os.getenv("MONGO_STRING").client)

    @app.route('/')
    def login():
        form = request.form
        # TODO
        return render_template('index.html')

    return app
