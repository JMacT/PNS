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
    product_group = SelectField('name', choices=[('OR','O-rings'),('OS','Oil Seals')])
    subcategory = SelectField('subcategory', choices=[])

@app.route('/', methods=['GET', 'POST'])
def home():
    # instantiate the Form.form
    form = Form()
    #default the page to all choices for product group "OR"
    form.subcategory.choices = [(subcategory.id, subcategory.subcategory) for subcategory in productgroup.query.filter_by(name='OR').all()]

    # when <form> in html is <input type='submit'> is clicked, flask.request.method == 'POST'
    if request.method == 'POST':
        #if you hit submit, the website posts to flask.
        chosen_catagory = productgroup.query.filter_by(id=form.subcategory.data).first()
        return '<h1>Product Group: {}, Subcategory: {}</h1><p><a href="/">Home</a></p>'.format(form.product_group.data, chosen_catagory.subcategory)

    return render_template('home.html', form=form)

@app.route('/subcategory/<chosen_catagory>')
def sub_category(chosen_catagory):
    name = chosen_catagory
    subcategories = productgroup.query.filter_by(name=name).all()
    subcatagoriesArray = []

    for subcategory in subcategories:
        sub_catObj = {}
        sub_catObj['id']=subcategory.id
        sub_catObj['subcategory'] = subcategory.subcategory
        subcatagoriesArray.append(sub_catObj)

    return jsonify({'subcategories':subcatagoriesArray})

if __name__ == '__main__':
    app.run(debug=True)
