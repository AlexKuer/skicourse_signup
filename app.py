from flask import Flask, request
import pandas as  pd 
import psycopg2
import os

app = Flask(__name__)
# Connect to your postgres DB
conn = psycopg2.connect(database="database",
                    host="app-e7eb027c-bde8-450a-8cc0-a27b07a097a2-do-user-13321347-0.b.db.ondigitalocean.com",
                    user=os.getenv('DB_USERNAME'),
                    password=os.getenv('DB_PASSWORD'),
                    port="25060")

@app.route('/', methods=['GET'])
def index():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("INSERT INTO testtable (spalte_1) VALUES ('I still have the highground')")
    conn.commit()
    cur.close()
    return '<p>I still have the high ground!</p>'

    

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
