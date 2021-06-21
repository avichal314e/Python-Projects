# Activating Virtual Environment
# python3 -m venv FlaskBasic
# . FlaskBasic/bin/activate

# Running Server
# export FLASK_APP=server.py
# export Flask_ENV=development
# flask run

# Main files/folders: static/ templates/ server.py

from flask import Flask, render_template, url_for
app = Flask(__name__)
# print(__name__) gives __main__
# print(url_for('static', filename='bolt.ico'))


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route('/')
def start():
    return "Hello"


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'Thoughts on blogs!!'


@app.route('/blog/2020/dogs')
def blog2():
    return 'Thoughts on Dogs!!'
