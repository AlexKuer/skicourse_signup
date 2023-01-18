from flask import Flask, request, render_template, redirect, url_for, send_file
from flask_mail import Mail, Message
import pandas as  pd 
import psycopg2
import os

app = Flask(__name__)

# Config Mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Connect to your postgres DB
conn = psycopg2.connect(database="database",
                    host="app-722d3265-77eb-41ff-a19b-79383a130d38-do-user-13321347-0.b.db.ondigitalocean.com",
                    user=os.getenv('DB_USERNAME'),
                    password=os.getenv('DB_PASSWORD'),
                    port="25060")

@app.route("/mailtest")
def mailtest():
  msg = Message('Hello from the other side!', sender =   'alexander.kuermeier@web.de', recipients = ['alexander.kuermeier@web.de'])
  msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
  mail.send(msg)
  return "Message sent!"

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

@app.route('/')
def index():
    return redirect(url_for('anmeldung'))

@app.route("/anmeldung", methods=['GET', 'POST'])
def anmeldung():
    if request.method == 'POST':
        name = request.form['name']
        option = request.form['option']

        # Open a cursor to perform database operations
        cur = conn.cursor()
        cur.execute(f"INSERT INTO skikurs_demo (name, option) VALUES ('{name}', '{option}')")
        conn.commit()
        cur.close()
        return render_template('anmeldung_bestaetigung.html', name=name, option=option)
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
