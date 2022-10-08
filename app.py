from flask import Flask, render_template, session, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def login():
        form = request.form
        # TODO
        return render_template('index.html')

    if __name__ == '__main__':
        app.run()
    return app
