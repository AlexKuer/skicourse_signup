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

@app.route('/')
def index():
    return redirect(url_for('anmeldung'))

@app.route("/anmeldung", methods=['GET', 'POST'])
def anmeldung():
    if request.method == 'POST':
        name = request.form['name']
        vorname = request.form['vorname']
        jahrgang = request.form['jahrgang']
        email = request.form['email']
        telefon = request.form['telefon']
        
        strasse = request.form['strasse']
        ort = request.form['ort']
        
        kurs = request.form.get('kurs')
        tage = ['1','2','3','4']
        kurstaglist = [request.form.get(f'kurstag{tag}') for tag in tage ]
        kurstaglist = list(map(lambda x: 'y' if x == 'on' else 'n', kurstaglist))
        buslist = [request.form.get(f'bus{tag}') for tag in tage]
        buslist = list(map(lambda x: 'y' if x == 'on' else 'n', buslist))
        kartelist = [request.form.get(f'karte{tag}') for tag in tage]
        kartelist = list(map(lambda x: 'y' if x == 'on' else 'n', kartelist))

        # Open a cursor to perform database operation
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO draft (name, vorname, jahrgang, email, telefon, strasse, ort, kurs, kurstaglist, buslist, kartelist) VALUES ('{name}','{vorname}', '{jahrgang}','{email}','{telefon}','{strasse}','{ort}','{kurs}','{str(kurstaglist).replace("'","")}','{str(buslist).replace("'","")}','{str(kartelist).replace("'","")}')""")
        conn.commit()
        cur.close()

        # Send Confirmation Mail
        msg = Message('Bestaetigung Skikursanmeldung!', sender = 'skikurs.svhaiming@gmail.com', recipients = [email])
        msg.html = render_template('email.html', name=name, vorname=vorname, jahrgang=jahrgang, email=email, telefon=telefon, strasse=strasse, ort=ort, kurs=kurs, kurstaglist=kurstaglist, buslist=buslist, kartelist=kartelist)
        mail.send(msg)
        return render_template('anmeldung_bestaetigung.html', name=name, vorname=vorname, jahrgang=jahrgang, email=email, telefon=telefon, strasse=strasse, ort=ort, kurs=kurs, kurstaglist=kurstaglist, buslist=buslist, kartelist=kartelist)
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
