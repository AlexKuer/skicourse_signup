from flask import Flask, request, render_template
import pandas as  pd 
import psycopg2
import os

from functions import test
test()

app = Flask(__name__)
# Connect to your postgres DB
conn = psycopg2.connect(database="database",
                    host="app-722d3265-77eb-41ff-a19b-79383a130d38-do-user-13321347-0.b.db.ondigitalocean.com",
                    user=os.getenv('DB_USERNAME'),
                    password=os.getenv('DB_PASSWORD'),
                    port="25060")

@app.route('/cover', methods=['GET'])
def cover():
    return render_template('cover.html')

@app.route('/who', methods=['GET'])
def who():
    name = request.args.get('name')
    name = 'Alexander' if name is None else name
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute(f"INSERT INTO firsttest (spalte_1) VALUES ('{name} has the highground')")
    conn.commit()
    cur.close()
    return f"<p>{name} has the highground</p>"

@app.route("/first_test", methods=['GET'])
def first_test():
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
