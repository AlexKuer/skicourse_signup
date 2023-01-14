from flask import Flask, request
import pandas as  pd 

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    return '<p>Hello World!<p>'

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)