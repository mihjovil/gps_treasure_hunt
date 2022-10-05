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

# region help for deployment
"""
requirements.txt is needed and pip freeze will create that file with all the packages in the environment
that might be an overkill, given that the project could use less packages than that.
Use the following command on your terminal
- pip install pipreqs

use the following command to create requiremetns.txt file
- pipreqs path/to/project

that should create the file in the selected path with only the required packages

"""
# endregion
