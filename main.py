from flask import Flask,redirect,url_for,render_template,request,flash,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

db.create_all()

class photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

@app.route("/")
def home():
    return render_template("index.html", photos=photos.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
         photo = photos(request.form['name'])
         db.session.add(photo)
         db.session.commit()
         return jsonify({'Succes' : 'Succes'})
   return jsonify({'error' : 'Missing data!'})

if __name__ == "__main__":
    db.create_all()
    app.run()