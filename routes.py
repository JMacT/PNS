from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

Bootstrap(app)

class Form(FlaskForm):
    product_catagory = SelectField('product_catagory', choices=[('OR','O-rings'), ('MFS', 'Metal Face Seals'), ('OS', 'Oil Seals')])
    subcatagory = SelectField('subcatagory', choices=[])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    form.subcatagory.choices = [(subcatagory.id, subcatagory.name) for subcatagory in subcatagory.query.filter_by(name = 'orings').all()] #NEED TO USE THE MASTER DB NOT AS568
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
