from flask import Flask, request
import pandas as  pd 
import psycopg2

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(database="database",
                            host="app-e7eb027c-bde8-450a-8cc0-a27b07a097a2-do-user-13321347-0.b.db.ondigitalocean.com",
                            user="database",
                            password="AVNS_1ko_-bo8AxceK550H2u",
                            port="25060")

        # Open a cursor to perform database operations
        cur = conn.cursor()
        return '<p>Connected Succesfully!<p>'
    except Exception as e:
        return e
    

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
