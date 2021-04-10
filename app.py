 from flask import Flask, render_template, request, redirect

import templates
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:localhost/mysite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = SQLAlchemy(app)
class Mysite(db.Model):
    Sno = db.Column(db.Integer, primary_key=True )
    Email =  db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=True)

@app.route('/',methods=['POST', 'GET'])
def Home_Page():
    if request.method == 'POST':
        Email = request.form.get('Email')
        Password = request.form.get('Password')

        entry = Mysite(Email=Email,Password = Password ,date = datetime.now() )
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')
    
@app.route('/shop')
def page1():
    return render_template('shop.html')
if __name__=='__main__':
    app.run(debug = True)
