from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

menu = {0: 'Tacos', 1: 'Fajitas', 2: 'Enchiladas'}
types = {0: ['Beef', 'Chicken', 'Brisket'], 1: ['Chicken', 'Cheese'], 2: ['Beef', 'Chicken', 'Cheese and Cream']}
Cals = {0: 200, 1: 350, 2: 300}

@app.route('/')
@app.route('/shop')
def shop():
    shopTitle = "Taco Shop"
    return render_template("shop.html", menu = menu, shopTitle = shopTitle)

@app.route("/index/<int:id>")
def index(id):
    return render_template("index.html", menu = menu[id], types = types[id])

@app.route("/nutrition")
def nutrition():
    return render_template("nutrition.html", menu = menu, types = types, Cals = Cals)