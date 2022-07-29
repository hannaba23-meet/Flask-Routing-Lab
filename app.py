from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('helloflask.html')
 
@app.route('/product')
def hello():
    return render_template('product.html')

@app.route('/cart')
def hello():
    return render_template('cart.html') 
app.run(debug = True)