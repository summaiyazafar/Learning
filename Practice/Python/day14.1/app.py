from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///john.db'
db=SQLAlchemy(app)

#Model
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    password=db.Column(db.String(80), unique=True, nullable=False)
    contact=db.Column(db.String(80), nullable=False)
    role=db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()
@app.route("/")
def home():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)