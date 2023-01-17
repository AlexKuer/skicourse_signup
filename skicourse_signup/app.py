from flask import Flask, request, render_template, send_file
import pandas as  pd 
import psycopg2
import os

from functions import functions
functions.test()

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

@app.route("/anmeldung", methods=['GET', 'POST'])
def anmeldung():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('anmeldung.html', name=name)
    else:
        return render_template('anmeldung.html')

@app.route('/merkblatt', methods=['GET'])
def merkblatt():
    return render_template('merkblatt.html')
@app.route('/kontakte', methods=['GET'])
def kontakte():
    return render_template('kontakte.html')

@app.route("/download_merkblatt", methods=['GET', 'POST'])
def download_merkblatt():
    # Appending app path to upload folder path within app root folder
    path = os.path.join(os.getcwd(),'skicourse_signup/static/files/MERKBLATT_Skikurse_2022.pdf')
    # Returning file from appended path
    return send_file(path, as_attachment=True)



    

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
