import flask
from flask import Flask, render_template, request

import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/quote', methods=['GET'])
def random_quote():
    return main.get_random_thirukkural()


if __name__ == "__main__":
    app.run(debug=True)