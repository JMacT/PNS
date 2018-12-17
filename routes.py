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

class productgroup(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique=True)
    name = db.Column(db.String(2), unique = False, nullable=False)
    subcategory = db.Column(db.String(100))


    def __repr__(self):
        return f"productgroup('{self.name}', '{self.subcategory}')"

class Form(FlaskForm):
    product_group = SelectField('name', choices=[('OR','BossSeals'),('OR','AS568'), ('OS','Profile1')])
    subcategory = SelectField('subcategory', choices=[])

@app.route('/', methods=['GET', 'POST'])
def home():
    # instantiate the Form.form
    form = Form()
    #default the page to all choices for product group "OR"
    form.subcategory.choices = [(subcategory.name, subcategory.name) for subcategory in productgroup.query.filter_by(name='OR').all()]

    # when <form> in html is <input type='submit'> is clicked, flask.request.method == 'POST'
    if request.method == 'POST':
        #if you hit submit, the website posts to flask.
        #new variable, City.city is created
        #City.city
        chosen_catagory = productgroup.query.filter_by(id=form.subcategory.data).first()
        return '<h1>subcat: {}, City: {}</h1><p><a href="/">Home</a></p>'.format(form.subcategory.data, chosen_catagory.name)

    return render_template('home.html', form=form)

@app.route('/Product_Group/<subcatagories>')
def city(chosen_catagory):
    options = productgroup.query.filter_by(subcategory=chosen_catagory).all()
    subcatagoriesArray = []

    for subcategory in options:
        cityObj = {}
        cityObj['id']=subcategory.id
        cityObj['name'] = subcategory.name
        subcatagoriesArray.append(cityObj)

    return jsonify({'cities':subcatagoriesArray})

if __name__ == '__main__':
    app.run(debug=True)
