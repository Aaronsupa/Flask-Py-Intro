from flask import Flask, render_template
app = Flask(__name__)
menu = {0: 'Tacos', 1: 'Fajitas', 2: 'Enchiladas'}
types = {0: ['Beef', 'Chicken', 'Brisket'], 1: ['Chicken', 'Cheese'], 2: ['Beef', 'Chicken', 'Cheese and Cream']}
@app.route('/')
@app.route('/shop')
def shop():
    shopTitle = "Taco Shop"
    return render_template("shop.html", menu = menu, shopTitle = shopTitle)

@app.route("/index/<int:id>")
def index(id):
    return render_template("index.html", menu = menu[id], types = types[id])
