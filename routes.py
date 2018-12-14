from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)
Bootstrap(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(2))
    name = db.Column(db.String(50))

class Form(FlaskForm):
    state = SelectField('state', choices=[('CA','California'),('NV','Nevada')])
    city = SelectField('city', choices=[])

@app.route('/', methods=['GET', 'POST'])
def home():
    # instantiate the Form.form
    form = Form()
    #set the Form.form.city.choices to be equal to all those in the db with state='CA'
    form.city.choices = [(city.id, city.name) for city in City.query.filter_by(state='CA').all()]

    # when <form> in html is <input type='submit'> is clicked, flask.request.method == 'POST'
    if request.method == 'POST':
        #if you hit submit, the website posts to flask.
        #new variable, City.city is created
        #City.city
        city = City.query.filter_by(id=form.city.data).first()
        return '<h1>State: {}, City: {}</h1><p><a href="/">Home</a></p>'.format(form.state.data, city.name)

    return render_template('home.html', form=form)

@app.route('/city/<state>')
def city(state):
    cities = City.query.filter_by(state=state).all()
    cityArray = []

    for city in cities:
        cityObj = {}
        cityObj['id']=city.id
        cityObj['name'] = city.name
        cityArray.append(cityObj)

    return jsonify({'cities':cityArray})

if __name__ == '__main__':
    app.run(debug=True)
