from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/shop')
def shop():
    menu = ['Taco', 'Fajita', 'Chips']
    return render_template("shop.html", menu = menu)

